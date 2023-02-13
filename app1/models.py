from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import numpy as np
import face_recognition
from PIL import Image as Im
# class UserManager(BaseUserManager):
#     def create_user(self, student_id, email, password=None):
#         """
#         Creates and saves a User with the given student ID, email, and password.
#         """
#         if not student_id:
#             raise ValueError('Users must have a student ID')
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             student_id=student_id,
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, student_id, email, password):
#         """
#         Creates and saves a superuser with the given student ID, email, and password.
#         """
#         user = self.create_user(
#             student_id=student_id,
#             email=email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

class students(models.Model):
    name = models.CharField(max_length=30,null=True)
    student_id = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=False)
    photo = models.ImageField(upload_to='photos/',null=False)
    password = models.CharField(max_length=255)
    encoding = models.BinaryField(null=True)
    
    def set_encoding(self, encoding):
        print('encodeing time')
        self.encoding = np.array(encoding).tobytes()

    def get_encoding(self):
        return np.frombuffer(self.encoding, dtype=np.float64)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    # objects = UserManager()

    # USERNAME_FIELD = 'student_id'
    # REQUIRED_FIELDS = ['email']
    
    def save(self, *args, **kwargs):
        if self.encoding is not None:
            print('its the encoding',self.encoding)
        else:
            print('its the encoding',self.encoding)
            img = Im.open(self.photo)
            
            rgb_image = img.convert('RGB')
            # conver to np array    
            np_image = np.array(rgb_image)
            # Return the image
            # val = face_recognition.face_encodings(np_image)
            val = face_recognition.face_encodings(np_image)[0]
            self.encoding = np.array(val).tobytes()
            
            print('its the encoding 2 :',self.encoding)
        return super().save( *args, **kwargs)
            
    def __str__(self):
        return self.name+ " "+self.student_id
        # return self.student_id  
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
