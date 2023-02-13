# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import students
import face_recognition
from .face_rec import f,recognize_face
from .forms import SignupForm,LoginForm
from .jpgconver import convert_to_jpeg,convert_base64_to_image

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        student_id = request.POST['student_id']
        email = request.POST['email']
        password = request.POST['password']
        photo = request.FILES['photo']
        # Load the image of the person you want to recognize
        known_image = face_recognition.load_image_file(photo)
        
        # Encode the face in the known image
        known_face_encoding = face_recognition.face_encodings(known_image)[0]
        # print(known_face_encoding)
        
        # Save the encoding to the database
        # face = Face(name=request.POST['name'], encoding=known_face_encoding)
        # face.save()
        studentsobj = students.objects.create(
            name=name,
            student_id=student_id,
            email=email,
            password=password,
            encoding=known_face_encoding
        )
        studentsobj.photo = photo
        studentsobj.save()
        return render(request,'sessesssignup.html',{'msg':"created scessfull"})
    form = SignupForm()
    return render(request, 'signup.html',{'form':form})
def login (request ):
    emptyform = LoginForm()
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            student_id = request.POST['student_id']
            password = request.POST['password']
            print(student_id,password)
            
            name = list(students.objects.filter(student_id=student_id,password=password).values('name'))
            try:
                print(name[0]['name'])
                # login(request, studentsobj)
                return render(request,'testpage.html',{'name':name[0]['name']})
            except:
                return render(request,"login.html",{'form':emptyform,'erorr':' try again password or id is wrong. or try face_recognition to login'}) 
    return render(request,"login.html",{'form':emptyform})
def login_face_recog(request):
    if request.method == 'POST':
        try:
            if request.POST.get('face_image'):
                # image = request.FILES['face_image']
                input_data =request.POST.get('face_image')  
                encode_data = convert_base64_to_image(input_data)
                result = recognize_face(encode_data)
                if result is not None:
                    name = list(students.objects.filter(student_id=int(result)).values('name'))
                    if name is not None:
                        print(name[0]['name'])
                        return render(request,'testpage.html',{'name':name[0]['name']})
                    else:
                        return render(request,'facelogin.html',{'erorr':'face not reconied try again'})
                        
                else :
                    return render(request,'facelogin.html',{'erorr':'face not reconied try again'})
                    
            else :
                return render(request,'facelogin.html',{'erorr':'face not reconied try again'})

        except:
            
            return render(request,'facelogin.html',{'erorr':' try again'})
        
    return render(request,'facelogin.html',{})
            # # face recognition
            # known_image = face_recognition.load_image_file(students.photo)
            # unknown_image = face_recognition.load_image_file(request.FILES['webcam_photo'])
            # face_encodings = face_recognition.face_encodings(known_image)

            # if len(face_encodings) == 0:
            #     return redirect('login')

            # match = face_recognition.compare_faces([face_encodings[0]], unknown_image)

            # if match[0]:
            #     students = students.objects.get(student_id=student_id)
            #     login(request, students)
            #     return redirect('home')
            # else:
            #     return redirect('login')
            # pass
    # form = LoginForm()
    # return render(request, 'login.html',{'form':form})

def home(request):
    # f()
    return render(request, 'homepage.html')


