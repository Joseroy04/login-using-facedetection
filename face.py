import face_recognition
from app1.models import students
known_image = face_recognition.load_image_file("vijay2.jpg")
unknown_image = face_recognition.load_image_file("vijay.jpeg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)

known_face_encodings = []
known_face_student_id = []
for face in students.objects.all():
    print(face.encoding)
    known_face_encodings.append(face.encoding)
    known_face_student_id.append(face.student_id)