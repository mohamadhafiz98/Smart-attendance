from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #image besar
        img4=Image.open(r"C:\Users\hafiz\THE CODE\Project redesign\clg_img\img\backg.png")
        img4=img4.resize((1530,790),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(width=1530, height=790)


        #tajuk
        title_lbl=Label(self.root,text="TRAIN DATA SET" ,font=("times new roman",35,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=380,width=400,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

#train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset complete!")

                                                  


if __name__ == "__main__":
     root=Tk()
     obj=Train(root)
     root.mainloop()