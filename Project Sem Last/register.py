from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

#----------variable
        self.var_fname=StringVar()
        self.var_Phone=StringVar()
        self.var_userid=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_role=StringVar()

#------------bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\g.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#------------main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=350,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)

#---------label and entry

#-------row1
        fname=Label(frame,text="First Name", font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Phone No",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_Phone=ttk.Entry(frame,textvariable=self.var_Phone,font=("times new roman",15))
        self.txt_Phone.place(x=370,y=130,width=250)

#-------row2

        userid=Label(frame,text="Staff ID", font=("times new roman",15,"bold"),bg="white")
        userid.place(x=50,y=170)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_userid,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

#-------row3

        security_Q=Label(frame,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","School","First Pet","Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

#--------row4

        pswd=Label(frame,text="Password ", font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.confirm_pswd.place(x=370,y=340,width=250)

#--------row5


        role=Label(frame,text="Select role", font=("times new roman",15,"bold"),bg="white",fg="black")
        role.place(x=50,y=380)

        course_role=ttk.Combobox(frame,textvariable=self.var_role,font=("times new roman",15,"bold"),state="readonly")
        course_role["values"]=("Select","Admin","Teacher")
        course_role.place(x=50,y=410,width=250)
        course_role.current(0)

        # role=Label(frame,text="Role", font=("times new roman",15,"bold"),bg="white",fg="black")
        # role.place(x=50,y=380)

        # self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        # self.txt_pswd.place(x=50,y=410,width=250)
# #--------checkbutton
#         checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"))
#         checkbtn.place()

#-----buttons
        img=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\registerbtn.png")
        img=img.resize((300,70),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=10,y=470,width=300)

        img1=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\loginbtn.png")
        img1=img1.resize((300,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=330,y=470,width=300)



#----------function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from user where UserID=%s")
            value=(self.var_userid.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits,please try another ID")
            else:
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_userid.get(),
                                                                                        self.var_fname.get(),
                                                                                        self.var_Phone.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),
                                                                                        self.var_role.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
