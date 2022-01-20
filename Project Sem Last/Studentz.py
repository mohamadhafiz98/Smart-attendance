from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

#variable
        self.var_Id=StringVar()
        self.var_Name=StringVar()
        self.var_Class=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()
        # self.var_search_by=StringVar()
        # self.var_search_txt=StringVar()

#atas

       #image besar
        img4=Image.open(r"C:\Users\hafiz\THE CODE\Project redesign\clg_img\img\biru.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1530, height=710)

        #tajuk
        title_lbl=Label(self.root,text="Student Details" ,font=("Arial",35,"bold"),fg="Black")        
        title_lbl.place(width=1530,height=45)

        #image besar
        img4=Image.open(r"C:\Users\hafiz\THE CODE\Project redesign\clg_img\img\backg.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=70,width=1530, height=710)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=5,width=1500,height=600)

#left
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font =("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        # img_left=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\hitam.jpg")
        # img_left=img_left.resize((720,130),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(Left_frame,image=self.photoimg3)
        # f_lbl.place(x=5,y=0,width=720, height=130)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information", font =("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=0,width=720,height=500)

        #student id
        studentId_label=Label(class_student_frame,text="Student ID:", font =("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_Id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Student Name:", font =("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name, width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student class
        Class_div_label=Label(class_student_frame,text="Class:", font =("times new roman",13,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentClass_entry=ttk.Entry(class_student_frame,textvariable=self.var_Class, width=20,font=("times new roman",13,"bold"))
        studentClass_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #student email
        email_label=Label(class_student_frame,text="Student Email:", font =("times new roman",13,"bold"),bg="white")
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_label=ttk.Entry(class_student_frame,textvariable=self.var_Email, width=20,font=("times new roman",13,"bold"))
        roll_no_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #student Phone
        phone_label=Label(class_student_frame,text="Student Phone No:", font =("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone ,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)


    #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=400,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=365,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1) 


#right
        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font =("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=900,height=580)

        # img_right=Image.open(r"C:\Users\hafiz\THE CODE\fyp code\fyp 1\clg_img\img\hitam.jpg")
        # img_right=img_right.resize((720,130),Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=780, height=130)

#search 
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font =("times new roman",12,"bold"))
        Search_frame.place(x=5,y=5,width=890,height=455)

        search_label=Label(Search_frame,text="Search By:", font =("times new roman",15,"bold"),bg="lightgreen")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame, font =("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Class","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=1)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=1)

#table frame

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=100,width=740,height=500)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Id","Name","Class","Email","Phone","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Id",text="Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill =BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

 #   ===========function declaration=======
    def add_data(self):
        if self.var_Name.get()=="" or self.var_Id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_Id.get(),
                                                                                        self.var_Name.get(),
                                                                                        self.var_Class.get(),
                                                                                        self.var_Email.get(),
                                                                                        self.var_Phone.get(),
                                                                                        self.var_radio1.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}" , parent=self.root)

#fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data= my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#   # # def search_data(self):
    #     if self.var_search_txt.get()=="" or self.var_search_by.get()=="Select":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
    #             conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
    #             my_cursor=conn.cursor()
    #             my_cursor.execute("select * from student where " +str(self.var_search_by.get())+" LIKE '%"+str(self.var_search_txt.get())+"%'")
    #             rows=my_cursor.fetchall()
    #             if len(rows)!=0:
    #                  self.student_table.delete(*self.student_table.get_children())
    #                  for i in rows:
    #                      self.student_table.insert("",END,values=i)
    #                      if rows==None:
    #                          messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                          conn.commit()
    #                          conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # #betul
    # def search_data(self): 
    #     conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("select * from student where " +str(self.var_search_by.get())+" LIKE '%"+str(self.var_search_txt.get())+"%'")
    #     rows=my_cursor.fetchall()
    #     if len(rows)!=0:
    #             self.student_table.delete(*self.student_table.get_children())
    #             for i in rows:
    #                 self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #                     conn.close()


    #search
    # def search_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("select * from student where "+str(self.var_search_by.get())+" LIKE '%" +str(self.var_search_txt.get())+"%'")
    #     data= my_cursor.fetchall()
    #     if len(data)!=0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for i in data:
    #             self.student_table.insert("",END,values=i)
    #         conn.commit()
    #         conn.close()


#get cursor

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_Id.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_Class.set(data[2]),
        self.var_Email.set(data[3]),
        self.var_Phone.set(data[4]),
        self.var_radio1.set(data[5])    

#update function
    def update_data(self):
        if self.var_Name.get()=="" or self.var_Id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try: 
                Upadate=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Name=%s,Class=%s,Email=%s,Phone=%s,PhotoSample=%s where Id=%s",(
                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                self.var_Class.get(),
                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                self.var_Phone.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_Id.get()
                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)
                  
#delete function
    def delete_data(self):
        if self.var_Id.get()=="":
            messagebox.showerror("Error","Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor() 
                    sql="delete from student where id=%s"
                    val=(self.var_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)



#reset button
    def reset_data(self):
        self.var_Id.set(""),
        self.var_Name.set(""),
        self.var_Class.set(""),
        self.var_Email.set(""),
        self.var_Phone.set(""),
        self.var_radio1.set("") 

# generate data set or take photo sample
    def generate_dataset(self):
        if self.var_Name.get()=="" or self.var_Id.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Name=%s,Class=%s,Email=%s,Phone=%s,PhotoSample=%s where Id=%s",(


                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                self.var_Class.get(),
                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                self.var_Phone.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_Id.get()==id+1
                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

#           ===== Load predifiend data on frontal from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))            
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)            
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}" ,parent=self.root)


if __name__ == "__main__":
     root=Tk()
     obj=student(root)
     root.mainloop()