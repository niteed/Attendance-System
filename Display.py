
#not yet connected

import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Display():
    def __init__(self, root):
        self.rootd = root
        self.rootd.title("Display Window")
        self.rootd.minsize(500,500)
        self.rootd.geometry('1920x1080')

        #self.photod = ImageTk.PhotoImage(file=r"C:\Users\kishor\Desktop\Face_Recognition_Project\displaybg.png")
        #lblimg1=Label(image=self.photod,bg="white",borderwidth=0)
        #lblimg1.place(x=0,y=0,width=1920,height=1080)



        canvasd = Canvas(self.rootd, width = 1920, height = 1080)
        canvasd.pack(fill = "both", expand = True)
        #canvasd.create_image(0,0,image=self.photod,anchor = "nw")
        canvasd.create_text( 1150, 200, text = "WELCOME!", font = ("Segoe UI Black" , 40, "bold"), fill = "gray30")
        canvasd.create_text( 1150, 270, text = "TO", font = ("Segoe UI Black" , 40), fill = "gray30")
        canvasd.create_text( 1150, 380, text = "Vidyalankar", font = ("Elephant" , 40), fill = "peachpuff4")
        canvasd.create_text( 1150, 470, text = "Institute of", font = ("Elephant" , 40), fill = "peachpuff4")
        #canvas1.create_text( 1200, 540, text = "", font = ("Elephant" , 50), fill = "white")
        canvasd.create_text( 1150, 560, text = "Technology", font = ("Elephant" , 40), fill = "peachpuff4")
        canvasd.create_text( 400, 650, text = "Developers : Nitee Dhuri | Priti Patankar | Neelam Bisht", font = ('times', 10, 'bold'), fill = "white")
        canvasd.create_text( 400, 670, text = "Mentor : Prof. Mohit Gujar | Department of Electronics and Telecommunication Engineering VIT", font = ('times', 10, 'bold'), fill = "white")

        Display_btn = Button( self.rootd, text = "Show Results",command = self.display_function, bd = 0, bg = "black", fg = "white", font=("times new roman", 20)).place(x=1045, y=90, width = 210, height = 40)

        #WELCOME TEXT
        #Welcome = Label(self.root, text = "Welcome", font =("Impact", 40, "bold"), background = "misty rose", foreground = "dark slate gray").place(x = 90, y = 30)

    def display_function(self):

        if self.txt_user == 'priti.patankar@vit.edu.in':
            self.user = 'Priti'
        elif self.txt_user == 'nitee.dhuri@vit.edu.in':
            self.user = 'Nitee'
        elif self.txt_user == 'neelam.bisht@vit.edu.in':
            self.user = 'Neelam'
        conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognition")
        my_cursor=conn.cursor()
        

        query=("select * from entrycsv where Name=%s ")
        value=(self.user.get())
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid")
        else :
            messagebox.showinfo("Success","Here are your results")
            print(row)
            conn.commit()
            conn.close()






root= Tk()
obj = Display(root)
root.mainloop()


        
