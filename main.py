#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import face_recognition

# Load the jpg files into numpy arrays
unknown_person=[]
know_person=[]
for x in range(15):
    know_person.append(face_recognition.load_image_file("./know_face/a"+str(x)+".bmp"))
    unknown_person.append(face_recognition.load_image_file("./unknown_face/s" + str(x) + ".bmp"))
# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    min=1
    tag=15
    know_faces = []
    unknown_faces = []
    for x in range(15):
        know_faces.append(face_recognition.face_encodings(know_person[x])[0])
        unknown_faces.append(face_recognition.face_encodings(unknown_person[x])[0])

except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()
# results = face_recognition.compare_faces(know_faces, unknown_faces[3],0.4)
# print(results)
# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
for x in range(15):
    results = face_recognition.compare_faces(know_faces, unknown_faces[x])
    disdance=face_recognition.face_distance(know_faces, unknown_faces[x])
    for y in range(15):
        if results[y]==True:
            if disdance[y]<min:
                min=disdance[y]
                if tag!=15:
                    results[tag]=False
                tag=y
            else: results[y]=False
    min=1
    for y in range(15):
        if results[y]==True:
            print("s"+str(x)+"'s name is "+"a"+str(y)+" and their distance is "+str(disdance[y]))
        else:
            print("the unknown face is a new person that we've never seen before.")


