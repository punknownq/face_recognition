#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import face_recognition
import unittest
class Person(object):
    def __init__(self, name):
        self.name = name
    def get_encoding(self):
       try:
           unknown_image = face_recognition.load_image_file("./unknown_face/"+self.name+".bmp")
           self.encoding = face_recognition.face_encodings(unknown_image)[0]
       except IndexError:
           print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
           quit()

class TestPerson(unittest.TestCase):
    def test_who_am_i(self):
        s1 = Person('a0')
        s1.get_encoding()
        result = face_recognition.compare_faces(known_faces[0],s1.encoding)
        self.assertEqual(result, True)



# Load the jpg files into numpy arrays
know_person=[]
for x in range(15):
    know_person.append(face_recognition.load_image_file("./know_face/a"+str(x)+".bmp"))
# unknown_image = face_recognition.load_image_file("./unknown_face/jake2.bmp")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    known_faces=[]
    for x in range(15):
        known_faces.append(face_recognition.face_encodings(know_person[x])[0])
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

if __name__ == '__main__':
    unittest.main()

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
# results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# print("Is the unknown face a picture of bank? {}".format(results[0]))
# print("Is the unknown face a picture of jake? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))