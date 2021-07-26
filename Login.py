from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


 

class Login:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Window")
        self.root.minsize(500,500)
        self.root.geometry('1920x1080')

        #BACKGROUND IMAGE
        #self.img = Image.open("wallpaper10.jpg")
        #self.photo = ImageTk.PhotoImage(self.img)
        self.photo = PhotoImage(file="wallpaper10.png")
        #self.BgImage = Label(self.root, image = self.photo, bd = 0).place(x=0, y=0, relwidth = 1, relheight =1)

        canvas1 = Canvas(self.root, width = 1920, height = 1080)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0,image=self.photo,anchor = "nw")
        canvas1.create_text( 1150, 200, text = "WELCOME!", font = ("Segoe UI Black" , 40, "bold"), fill = "gray30")
        canvas1.create_text( 1150, 270, text = "TO", font = ("Segoe UI Black" , 40), fill = "gray30")
        canvas1.create_text( 1150, 380, text = "Vidyalankar", font = ("Elephant" , 40), fill = "peachpuff4")
        canvas1.create_text( 1150, 470, text = "Institute of", font = ("Elephant" , 40), fill = "peachpuff4")
        #canvas1.create_text( 1200, 540, text = "", font = ("Elephant" , 50), fill = "white")
        canvas1.create_text( 1150, 560, text = "Technology", font = ("Elephant" , 40), fill = "peachpuff4")
        canvas1.create_text( 400, 650, text = "Developers : Nitee Dhuri | Priti Patankar | Neelam Bisht", font = ('times', 10, 'bold'), fill = "white")
        canvas1.create_text( 400, 670, text = "Mentor : Prof. Mohit Gujar | Department of Electronics and Telecommunication Engineering VIT", font = ('times', 10, 'bold'), fill = "white")


        #WELCOME TEXT
        #Welcome = Label(self.root, text = "Welcome", font =("Impact", 40, "bold"), background = "misty rose", foreground = "dark slate gray").place(x = 90, y = 30)

        #FRAME
        Frame_login = Frame(self.root, bg = "linen")
        Frame_login.place(x = 250, y = 120, height = 400, width = 500)

        title = Label(Frame_login, text = "LOGIN HERE", font =("Impact", 40, "bold"), background = "linen", foreground = "dark slate gray").place(x = 90, y = 30)
        desc = Label(Frame_login, text = "Student Login Area", font = ("Corbel Light", 17, "bold"), bg = "linen" , fg = "dark slate gray").place(x = 90, y = 100)

        Label_user = Label(Frame_login, text = "USERNAME", font = ("Goudy old style", 15, "bold"), bg = "linen" , fg = "dark slate gray").place(x = 90, y = 140)
        self.txt_user=Entry(Frame_login, font = ("times new roman", 15), bg = "misty rose" , fg = "dark slate gray" )
        self.txt_user.place(x=90, y=170, width = 350, height= 35)
              

        Label_password = Label(Frame_login, text = "PASSWORD", font = ("Goudy old style", 15, "bold"), bg = "linen" , fg = "dark slate gray").place(x = 90, y = 210)
        self.txt_password=Entry(Frame_login, font = ("times new roman", 15), bg = "misty rose" , fg = "dark slate gray" )
        self.txt_password.place(x=90, y=240, width = 350, height= 35)

        forget = Button(Frame_login, text = "Forget Password?", command = self.forget_password, bd = 0, bg = "linen", fg = "Dark slate gray", font=("times new roman", 12)).place(x=90, y=280)
        Login_btn = Button( Frame_login, text = "Login/Recognize",command = self.login_function, bd = 0, bg = "Dark slate gray", fg = "misty rose", font=("times new roman", 20)).place(x=150, y=330, width = 210, height = 40)



    def login_function(self):
        
        if self.txt_password.get()=="" or self.txt_user.get()=="":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            #messagebox.showinfo("Success","Welcome")
			#======sql connectivity====
            conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognition")

			#===to link and add data into mysql database=====
            my_cursor=conn.cursor()
			#validation for email to avoid multiple login from same email
            query=("select * from login_data where Email=%s and password=%s ")
            value=(self.txt_user.get(),self.txt_password.get())
			#executing cursor
            my_cursor.execute(query,value)
			#to fetch data from database
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else :
                messagebox.showinfo("Success","You have registered successfully")
                conn.commit()
                conn.close()
                root.destroy()
                import attendance
                #root= Tk()
                #obj = Display(root)
                #root.mainloop()
                


    def forget_password(self):
        messagebox.showinfo("Forget Password", "Please Email your details such as Name, RollNo, Branch and Year on our official email ID", parent = self.root)



root= Tk()
obj = Login(root)
root.mainloop()
        
