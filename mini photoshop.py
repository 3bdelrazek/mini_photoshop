import tkinter as tk
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
import pandas as pd



app = tk.Tk()
app.title("Edit Certificates ")
lb1 = Label(text=" Welcome  ❤  ",font= ("Tahoma",25),fg="#9720ff").pack()
canvas1 = tk.Canvas(app, width=200, height=100)
canvas1.pack()
label2 = tk.Label(app, text='Enter X Position🖌')
label2.config(font=('helvetica', 14),fg="#9720ff")
canvas1.create_window(-80, 40, window=label2)
label3 = tk.Label(app, text='Enter Y Position🖋')
label3.config(font=('helvetica', 14),fg="#9720ff")
canvas1.create_window(-80, 70, window=label3)


# open function
def selcet_names():
    global Names
    app.filename = filedialog.askopenfilename(initialdir="D:/", title="select your Names" ,filetypes=[("Text files","*.xlsx")])
    Names = app.filename

def select_image():
    global cert
    app.filename = filedialog.askopenfilename(initialdir="D:/", title="select Image", filetypes=[("image files","*.jpg")])
    cert = app.filename
    img = PIL.Image.open(cert)
    img_info = Label(text= "image size " + str(img.size) , font=("Tahoma", 15), fg="#6c61ff")
    canvas1.create_window(50, 100, window=img_info)


def choose_color():
    global color_code
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color🎨 ")


def edit_img():
    X = entry1.get()
    Y = entry2.get()
    # Open excel file
    data = pd.read_excel(Names)
    grd =0
    # Custom font style and font size
    name_Font = PIL.ImageFont.truetype('C:\Windows\Fonts\GOTHICB.TTF', 100)
    id_Font = PIL.ImageFont.truetype('C:\Windows\Fonts\GOTHIC.TTF', 40)
    date_Font = PIL.ImageFont.truetype('C:\Windows\Fonts\GOTHIC.TTF', 80)
    #  loop to wirte name on images
    for line in data['Names']:
        # Open an Image
        img = PIL.Image.open(cert)
        # Call draw Method to add 2D graphics in an image
        edit_img = PIL.ImageDraw.Draw(img)
        # Add Text to an image name , id and date
        # edit_img.text((1120, 1380), line , font=name_Font, fill=(255, 255, 255))
        edit_img.text((int(X), int(Y)), line , font=name_Font, fill=color_code[1])
        edit_img.text((780, 2300), str(data['ID'][grd]), font=id_Font, fill=(0, 23, 114))
        edit_img.text((650, 2100), data['Date'][0] , font=date_Font, fill=(0, 23, 114))
        # Add Text to an image "Grade"
        grd += 1
        # Save the edited image
        img.save(line.rstrip("\n") + ".pdf")





entry1 = tk.Entry(app)
canvas1.create_window(60, 40, window=entry1)
entry2 = tk.Entry(app)
canvas1.create_window(60, 70, window=entry2)
grid1 = Label(text="⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴",font= ("Tahoma",20),fg="#ff5166").pack()
button1 = Button(app, text="Select  Image",font= ("Lucida",20), command=select_image,fg="white", bg="#c481ff").pack()
# canvas1.create_window(0,0,window=button1)
buttoncolor = Button(app, text="Choose Color😉",font= ("Lucida",14), command=choose_color,fg="Red", bg="White")
canvas1.create_window(210,55,window=buttoncolor)
grid2 = Label(text="⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴",font= ("Tahoma",20),fg="#ff5166").pack()
button2 = Button(app, text="Select your Names ",font= ("Lucida",20), command=selcet_names,fg="white", bg="#c481ff").pack()
grid3 = Label(text="⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴⩴",font= ("Tahoma",20),fg="#ff5166").pack()
button3 = Button(app, text="Start Editing ",font= ("Lucida",20), command=edit_img,fg="white", bg="#c481ff")
button3.pack()
Name = Label(text="◉Designed By® Abdelrazek Elsayad  A ❤ W",font= ("Tahoma",15),fg="#6c61ff").pack()
linkedin = Label(text="▣ linkedin.com/in/abdelrazek-elsayad ",font= ("Tahoma",15),fg="#6c61ff").pack()

app.mainloop()

