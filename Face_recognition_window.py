from tkinter import*

window = Tk()

window.title("Face Recognition Window")
window.minsize(500,500)
window.geometry('1920x1080')


#BackGround CANVAS

BackGround = PhotoImage(file="wallpaper12.png")
CANVAS1 = Canvas(window, width = 1920, height = 1080)
CANVAS1.pack(fill = "both", expand = True)
CANVAS1.create_image(0,0,image=BackGround,anchor = "nw")

CANVAS1.create_text( 812, 150, text = "FACE RECOGNITION", font = ("Segoe UI Black" , 40, "bold"), fill = "SNOW")
CANVAS1.create_text( 812, 265, text = "Welcome to face recognition.", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")
CANVAS1.create_text( 812, 300, text = "The new way to speed up your life! Go paperfree and save nature!", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")
CANVAS1.create_text( 812, 330, text = "Click below button to recognize", font = ("Arial Unicode MS" , 15, ), fill = "SNOW")


Login_btn = Button( window, relief =RIDGE, text = "Recognize", bd = 0, bg = "ALICE BLUE", fg = "STEEL BLUE", font=("Microsoft YaHei UI Light", 20, "bold")).place(x=700, y=400, width = 210, height = 50)

CANVAS1.create_text( 812, 500, text = "INSTRUCTIONS", font = ("Arial Unicode MS" , 10), fill = "SNOW")
CANVAS1.create_text( 812, 520, text = "1. Keep your face straight in front of camera", font = ("Arial Unicode MS" , 10 ), fill = "SNOW")
CANVAS1.create_text( 812, 540, text = "2. Showing photo from mobile is not allowed, if done, it will be considered as misbehaviour", font = ("Arial Unicode MS" , 10 ), fill = "SNOW")


CANVAS1.create_text( 765, 750, text = "Developers : Nitee Dhuri | Priti Patankar | Neelam Bisht | Sakshi Padwal", font = ('times', 10, 'bold'), fill = "steelblue4")
CANVAS1.create_text( 760, 770, text = "Mentor : Prof. Mohit Gujar | Department of Electronics and Telecommunication Engineering VIT", font = ('times', 10, 'bold'), fill = "steelblue4")
