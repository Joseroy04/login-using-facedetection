# myapp/face_recognition.py

import face_recognition
from .models import students
import numpy as np

def f():
    known_face_encodings = []
    known_face_student_id = []
    for face in students.objects.all():
        print(np.frombuffer(face.encoding, dtype=np.float64))
        known_face_encodings.append(np.frombuffer(face.encoding, dtype=np.float64))
        known_face_student_id.append(face.student_id)

def recognize_face(unknown_image):
    # load all known face encodings from the database
    # known_face_encodings = []
    # known_face_student_id = []
    for face in students.objects.all():
        # unface_load = face_recognition.load_image_file(unknown_image)
        # face_encodings = face_recognition.face_encodings(unface_load)[0]
        face_encodings = unknown_image[0]
        matches = face_recognition.compare_faces([np.frombuffer(face.encoding, dtype=np.float64)], face_encodings)
        print(matches)
        if matches[0]:
            return face.student_id
    return None
        # known_face_encodings.append(np.frombuffer(face.encoding, dtype=np.float64))
        # known_face_student_id.append(face.student_id)

    # find the face encodings in the unknown image
    
    # face_locations = face_recognition.face_locations(unknown_image)
    # face_encodings = face_recognition.face_encodings(unknown_image)[0]
    # matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
    # return matches
    # loop over the face encodings
    # for face_encoding in face_encodings:
    #     # see if the face is a match for the known face(s)
    #     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    #     student_id = "Unknown"
    #     return matches
        # use the known face with the smallest distance to the new face
        # face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        # best_match_index = np.argmin(face_distances)
        # if matches[best_match_index]:
        #     student_id = known_face_student_id[best_match_index]

    # return student_id
