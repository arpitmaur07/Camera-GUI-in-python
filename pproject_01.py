from tkinter import *
from PIL import Image, ImageTk
import cv2 as cv

root = Tk()
root.title('Camera App')
# root.geometry('640x520')
root.minsize(646,530)
root.maxsize(646,530)
root.configure(bg='#58F')

label =Label(root,bg='red')
label.pack()
label2 =Label(root,bg='#58F')
label2.pack()
cap= cv.VideoCapture(0)
temp=False
if (cap.isOpened() == False):
  print("Unable to read camera feed")

def show_frames():
   cv2image= cv.cvtColor(cap.read()[1],cv.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   label.after(20, show_frames)
show_frames()

def captureImage():
   while True:
      ret,frame=cap.read()
      if ret is True:
         cv.imwrite('image.png',frame)
         break
    
   cap.release()
   cv.destroyAllWindows()
   # root.destroy()
def exitWindow():
   cap.release()
   cv.destroyAllWindows()
   root.destroy()
   root.quit()
   
b1=Button(label2,bg='green',fg='white',activebackground='black',activeforeground='white',text='Capture Image 📷',relief=RIDGE,height=200,width=30,command=captureImage)
b1.pack(side=LEFT,padx=7,pady=5)
b2=Button(label2,fg='white',bg='red',activebackground='magenta',activeforeground='white',text='EXIT ❌ ',relief=RIDGE,height=200,width=20,command=exitWindow)
b2.pack(side=LEFT,padx=7,pady=5)

root.mainloop()