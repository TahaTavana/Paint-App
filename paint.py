from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from comtypes.tools.codegenerator.packing import storage
from docutils.nodes import image, option
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageGrab
from PIL import Image
from tkinter import messagebox

# pip install opencv-python
# pip install numpy
#  pip install pyautogui
root=tk.Tk()
style = ttk.Style()
style.configure("MyButton.TButton")
root.title("paint")
root.geometry("1100x650+400+200")
##################
img = PhotoImage(file='allthings.how-how-to-use-the-new-paint-app-on-windows-11-microsoft-paint-logo.png')
root.iconphoto(False, img)
#################
###########MENU##############
menubar = Menu(root)
####################
def saveImage():
    try:
        fileLocation=filedialog.asksaveasfilename(title ="Save your Image !",defaultextension='jpg')
        x=root.winfo_rootx()+20
        y=root.winfo_rooty()+140#از بالا کم و به پایین اضافه
        img=ImageGrab.grab(bbox=(x,y,x+1000,y+490))
        img.save(fileLocation)
        ShowImage=messagebox.askyesno("Paint App","Doy want to see your image?")
        print(ShowImage)
        if ShowImage:
            img.show()
    except Exception as e:
        messagebox.showinfo("Error","I cant save your image")
def clear():
    clearfile=messagebox.askyesno("Paint Canvas App","Doy want to clear your Canvas?")
    if clearfile:
        canvas.delete("all")
def new():
    if messagebox.askyesno("Paint New Canvas App","Doy want to save your canvas befor  create a new Canvas ?"):
        saveImage()
        canvas.delete("all")
    else:
        canvas.delete("all")

def about():
    messagebox.showinfo("developer","paint App Developed by Mohammad taha tavana.")
def about_program():
    messagebox.showinfo("developer","Im Developed this program for :\ndrawing")

def writeText(event):
    x=textSize.get()
    color=Colortext.get()
    canvas.create_text(event.x , event.y , text=textValue.get(),font=("B Yekan+",x),fill=color)

def writeText_new(event):
    x = textSize.get()
    color=Colortext.get()
    canvas.create_text(event.x, event.y, text=textValue.get(), font=("B Yekan+", x),fill=color)
# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File   |', menu=file)
file.add_command(label='New Canvas',command=new)
file.add_command(label='Open...')
file.add_command(label='Save as File',command=saveImage)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)
###############edit###########################
Edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit   | ', menu=Edit)
Edit.add_command(label='Clear File',command=clear)
###################
About = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About   |', menu=About)
About.add_command(label='About me',command=about)
About.add_command(label='About my program',command=about_program)
##############################
def Help_m():
    messagebox.showinfo("help","If you want to type something on the screen, use these two ways:\nFirst, type your text in the typing field and then double-click the left mouse button on the screen.\n Or click the middle mouse button, which is called scroll, on the screen once.\nI hope the problem is solved. ")
Help = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help    ', menu=Help)
Help.add_command(label='Help to write on canvas',command=Help_m)
#####################END OF MENU##########################
#stroke_size.pencils#
stroke_size=IntVar()
stroke_size.set(1)
stroke_color=StringVar()
stroke_color.set('black')
#$$$$$$$$frame1:tools,size,...
frame1=Frame(root,height=90,width=1100)
frame1.grid(row=0,column=0,sticky=NW)
#########
toolsFrame=Frame(frame1,height=90,width=100,padx=5)
toolsFrame.grid(row=0,column=0)
def usePencil():
    stroke_color.set("black")
    canvas["cursor"]="pencil"
def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX
def use_default():
    stroke_size.set(2)
###############################buttons tools ##############################################################
def openwin():
    messagebox.showinfo("Text","please go to frame Text")
image=PhotoImage(file='pencil.png')
pencilbutton=ttk.Button(toolsFrame,image=image,command=usePencil)
pencilbutton.grid(row=0,column=0)
text=PhotoImage(file='text1.png')
textbutton=ttk.Button(toolsFrame,image=text,command=openwin,cursor='hand2')
textbutton.grid(row=0,column=2)
############eraser
eraser=PhotoImage(file='eraser.png')
eraserbutton=ttk.Button(toolsFrame,image=eraser,command=useEraser,cursor='hand2')
eraserbutton.grid(row=1,column=0)
########what_color
eyedroper=PhotoImage(file='what_color.png')
eyedroperbutton=ttk.Button(toolsFrame,image=eyedroper,cursor='hand2')
eyedroperbutton.grid(row=1,column=1)
###########zoom
zoom=PhotoImage(file='zoom.png')
zoombutton=ttk.Button(toolsFrame,image=zoom,cursor='hand2')
zoombutton.grid(row=1,column=2)
##########label tools
texttools=ttk.Label(toolsFrame,text='tools',font=("Arial",10))
texttools.grid(row=2,column=1)
##########
sizeFrame=Frame(frame1,height=90,width=100)
sizeFrame.grid(row=0,column=1,)
defaultButton=ttk.Button(sizeFrame,text="default",width=12,command=use_default,cursor='hand2')
defaultButton.grid(row=1,column=0)

Listsize=ttk.Combobox(sizeFrame,state='readonly',width=10,textvariable=stroke_size,values=["1","2","3","4","5","15"])
Listsize.grid(row=3,column=0,padx=20)
photo_image = ImageTk.PhotoImage(file='size.png')
# Create a label widget to hold the image
image_label = Label(sizeFrame, image=photo_image)
# Place the label in the frame
image_label.grid(row=0,column=0)
###########
textSize=ttk.Label(sizeFrame,text='Size',font=("Arial",10))
textSize.grid(row=5,column=0)
#####################################################
def select_color():
    selectedColor=colorchooser.askcolor("red",title="Select Color !")
    if selectedColor[1]==None:
        canvas["cursor"] = "pencil"
        stroke_color.set("black")
    else:
        canvas["cursor"] = "pencil"
        stroke_color.set(selectedColor[1])
colorBoxframe=Frame(frame1,height=100,width=100)
colorBoxframe.grid(row=0,column=2)
rounded_circle=PhotoImage(file='rounded color.png')
colorbutton=ttk.Button(colorBoxframe,image=rounded_circle,width=10,command=select_color,cursor='hand2')
colorbutton.grid(row=0,column=11,padx=20,pady=10)
###########
def color_black():
        fill = stroke_color.set('black')
        canvas["cursor"] = "pencil"
color2photo=PhotoImage(file='color 1  -2.png')
color2button=ttk.Button(colorBoxframe,image=color2photo,width=10,command=color_black,cursor='hand2')
color2button.grid(row=0,column=1)
####
def color_gray():
    fill = stroke_color.set('#7f7f7f')
    canvas["cursor"] = "pencil"
color3photo=PhotoImage(file='color 1  -3.png')
color3button=ttk.Button(colorBoxframe,image=color3photo,width=10,command=color_gray,cursor='hand2')
color3button.grid(row=0,column=2)
######
def color_red():
    fill = stroke_color.set('#880015')
    canvas["cursor"] = "pencil"
color4photo=PhotoImage(file='color 1  -4.png')
color4button=ttk.Button(colorBoxframe,image=color4photo,width=10,command=color_red,cursor='hand2')
color4button.grid(row=0,column=3)
########
def color_redsub():
    fill = stroke_color.set('#ed1c24')
    canvas["cursor"] = "pencil"
color5photo=PhotoImage(file='color 1  -5.png')
color5button=ttk.Button(colorBoxframe,image=color5photo,width=10,command=color_redsub,cursor='hand2')
color5button.grid(row=0,column=4)
#######
def color_orange():
    fill = stroke_color.set('#ff7f27')
    canvas["cursor"] = "pencil"
color6photo=PhotoImage(file='color 1  -6.png')
color6button=ttk.Button(colorBoxframe,image=color6photo,width=10,command=color_orange,cursor='hand2')
color6button.grid(row=0,column=5)
#########
def color_yellow():
    fill = stroke_color.set('#fff200')
    canvas["cursor"] = "pencil"
color7photo=PhotoImage(file='color 1  -7.png')
color7button=ttk.Button(colorBoxframe,image=color7photo,width=10,command=color_yellow,cursor='hand2')
color7button.grid(row=0,column=6)
#########
def color_green():
    fill = stroke_color.set('#3cb861')
    canvas["cursor"] = "pencil"
color8photo=PhotoImage(file='color 1 -8.png')
color8button=ttk.Button(colorBoxframe,image=color8photo,width=10,command=color_green,cursor='hand2')
color8button.grid(row=0,column=7)
############
def color_blue():
    fill = stroke_color.set('#00a2e8')
    canvas["cursor"] = "pencil"
color9photo=PhotoImage(file='color 1 -9.png')
color9button=ttk.Button(colorBoxframe,image=color9photo,width=10,command=color_blue,cursor='hand2')
color9button.grid(row=0,column=8)
################
def color_blueopacity80():
    fill = stroke_color.set('#3f48cc')
    canvas["cursor"] = "pencil"
color10photo=PhotoImage(file='color 1-10.png')
color10button=ttk.Button(colorBoxframe,image=color10photo,width=10,command=color_blueopacity80,cursor='hand2')
color10button.grid(row=0,column=9)
#################
def color_blueopacity96():
    fill = stroke_color.set('#a349a4')
    canvas["cursor"] = "pencil"
color11photo=PhotoImage(file='color 1 -11.png')
color11button=ttk.Button(colorBoxframe,image=color11photo,width=10,command=color_blueopacity96,cursor='hand2')
color11button.grid(row=0,column=10)
#########label#########################
text_color=ttk.Label(colorBoxframe,text='Colors',font=("Mj_Farsi",10))
text_color.grid(row=1,column=6)
###################################
def Change_background():
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1] )
#######################################
def msg_sub():
    messagebox.showinfo("Paint App","I submit your size ,\n if you cant find your size write in combobox")
bucket=PhotoImage(file='bucket_color.png')
bucketbutton=ttk.Button(toolsFrame,image=bucket,command=Change_background,cursor='hand2')
bucketbutton.grid(row=0,column=1)
######################
textframe=Frame(frame1,height=130,width=300)
textframe.grid(row=0,column=7)
###############part1####################
lblwrite=Label(textframe,text='Write your text in this input :',font=("B Yekan+",11),anchor='w')
lblwrite.place(x=0,y=5)
##############
textValue = StringVar()
entrywrite=Entry(textframe, text='Write your text', textvariable=textValue, font=("B Yekan+", 10),width=34)
entrywrite.place(x=0,y=40)
#############
clearimg=PhotoImage(file='./cl.png')
btn_clear_Entry=ttk.Button(textframe,image=clearimg,command=lambda :textValue.set(""))
btn_clear_Entry.place(x=250,y=30)

############
lblwrite_Size=Label(textframe,text='Size and color:',font=("B Yekan+",11))
lblwrite_Size.place(x=0,y=70)
textSize=IntVar()
ListSize_textwrite=ttk.Combobox(textframe,textvariable=textSize,width=10,values=["2","4","6","8","10","12"])
ListSize_textwrite.place(x=110,y=75)
ListSize_textwrite.current(2)
##########
Colortext=StringVar()
Listcolor_textwrite=ttk.Combobox(textframe,textvariable=Colortext,width=10,values=["green","blue","yellow","black","white","red","orange"])
Listcolor_textwrite.place(x=210,y=75)
Listcolor_textwrite.current(3)
#############
label_text_frame=Label(textframe,text='Text',font=("Arial",10))
label_text_frame.place(x=145,y=110)
################# canvas##############
frame2=Frame(root,height=560,width=1100,bg='white')
frame2.grid(row=1,column=0)
##################
canvas_width=1100
canvas_height=560
canvas=Canvas(frame2,height=canvas_height,width=canvas_width,bg='white')
canvas.grid(row=0,column=0)
stroke_color=StringVar()
stroke_color.set('black')
#################
prevpiont=[0,0]
currentpiont=[0,0]
def paint(event):
    global prevpiont
    global currentpiont
    x=event.x
    y=event.y
    currentpiont=[x,y]
    if prevpiont!=[0,0]:
        canvas.create_polygon(prevpiont[0],prevpiont[1],currentpiont[0],currentpiont[1],fill=stroke_color.get(),outline=stroke_color.get(),width=stroke_size.get())
    prevpiont=currentpiont
    if event.type=="5":
        prevpiont=[0,0]
def msg():
    messagebox.showinfo("Paint App Dotline","Please press and hold the right mouse button to\n draw a dotted line for you.")
dotline=PhotoImage(file='dotlinne.png')
btnDotline=ttk.Button(sizeFrame,image=dotline,command=msg,cursor='hand2')
btnDotline.grid(row=4,column=0)

def paint_dotline(event):
    x=event.x
    y=event.y
    canvas["cursor"]="pencil"
    canvas.create_oval(x, y, x + stroke_size.get(), y + stroke_size.get(), 
                       fill=stroke_color.get(), 
                       outline="")
canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', paint)
canvas.bind('<B3-Motion>',paint_dotline)
canvas.bind("<Button-2>", writeText)
canvas.bind("<Double-Button-1>", writeText_new)
####################################
root.config(menu = menubar)
root.mainloop()
