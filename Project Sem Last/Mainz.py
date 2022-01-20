from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
from Menuz import Face_Recognition_System


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__ (self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

   
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\back.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
     
        #tajuk
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM" ,font=("Arial",35,"bold"),fg="Black")        
        title_lbl.place(width=1530,height=70)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=130,y=100)

        #label
        username=lbl=Label(frame,text="Staff Id",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #===========icon image
        img2=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\login.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\pass.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)

        #login Button
        loginbtn=Button(frame,command=self.login, text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register Button
        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpass
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    #--------------LOGIN
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="123" and self.txtpass.get()=="123":
            messagebox.showinfo("Success","Welcome to Attendance System Using Face Recognition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from user where UserID=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","inavalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                   
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #------reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            qury=("select * from user where UserID=%s and SecurityQ=%s and SecurityA=%s")
            vaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update user set Password=%s where UserID=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("info","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()
            

    #------forget password
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Staff ID to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from user where UserID=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)
            if row==None:
                messagebox.showerror("My Error","please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","School","First Pet","Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)

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
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=10,y=470,width=300)

        img1=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\loginbtn.png")
        img1=img1.resize((300,70),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
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

    def return_login(self):
        self.root.destroy()



if __name__ == "__main__":
    main()