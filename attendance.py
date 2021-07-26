import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import tkinter as tk
import mysql.connector
from tkinter import*

window = Tk()

window.title("Face Recognition Window")
window.minsize(500,500)
window.geometry('1920x1080')


BackGround = PhotoImage(file="wallpaper12.png")
CANVAS1 = Canvas(window, width = 1920, height = 1080)
CANVAS1.pack(fill = "both", expand = True)
CANVAS1.create_image(0,0,image=BackGround,anchor = "nw")

CANVAS1.create_text( 812, 150, text = "FACE RECOGNITION", font = ("Segoe UI Black" , 40, "bold"), fill = "SNOW")
CANVAS1.create_text( 812, 265, text = "Welcome to face recognition.", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")
CANVAS1.create_text( 812, 300, text = "The new way to speed up your life! Go paperfree and save nature!", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")
CANVAS1.create_text( 812, 330, text = "Click below button to recognize", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")

CANVAS1.create_text( 812, 500, text = "INSTRUCTIONS", font = ("Arial Unicode MS" , 10), fill = "SNOW")
CANVAS1.create_text( 812, 520, text = "1. Keep your face straight in front of camera", font = ("Arial Unicode MS" , 10 ), fill = "SNOW")
CANVAS1.create_text( 812, 540, text = "2. Showing photo from mobile is not allowed, if done, it will be considered as misbehaviour", font = ("Arial Unicode MS" , 10 ), fill = "SNOW")


CANVAS1.create_text( 765, 750, text = "Developers : Nitee Dhuri | Priti Patankar | Neelam Bisht | Sakshi Padwal", font = ('times', 10, 'bold'), fill = "steelblue4")
CANVAS1.create_text( 760, 770, text = "Mentor : Prof. Mohit Gujar | Department of Electronics and Telecommunication Engineering VIT", font = ('times', 10, 'bold'), fill = "steelblue4")


#reading images by giving path
path = 'images'
#list creation
images = []
classNames = []
myList = os.listdir(path)
print("Images components lists read successfully")
print(myList)

#cl is our current image
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    #list img inside the path is read
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    #name is 0th component and extension is first component
print("Students Names")
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        #img is in format of bgr bt cv2 reads only rgb
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        print(encodeList)
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            
          
        if name not in nameList and x not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{x},{dtString}')


            conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognition")
            my_cursor=conn.cursor()
            query=("insert into entrycsv values(%s,%s,%s)")
            value=(name,x,dtString)
            my_cursor.execute(query,value)
            conn.commit()
            conn.close()
 

now = datetime.now()
x = now.strftime('%d %B %Y')

encodeListKnown = findEncodings(images)
print('Encoding Complete Successfully')

#camera reading
def Recognize():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]
                print("Welcome "+name+"\nHave A Good Day!")
                CANVAS1.create_text( 785, 215, text = str(name), font = ("Arial Unicode MS" , 25 ), fill = "SNOW")

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('Face Recognition Attendance System', img)
        if cv2.waitKey(1) == 13 :
            break
    cap.release()
    cv2.destroyAllWindows()

recognizeButton = Button( window, relief =RIDGE,command= Recognize, text = "Recognize", bd = 0, bg = "ALICE BLUE", fg = "STEEL BLUE", font=("Microsoft YaHei UI Light", 20, "bold")).place(x=700, y=400, width = 210, height = 50)

    
window.mainloop()