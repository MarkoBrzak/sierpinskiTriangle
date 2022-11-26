import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


    # MessageBox for Exit dialogue.
def ex():
    answer = tk.messagebox.askquestion('Exit', 'Do you wish to exit the program?')
    if answer == 'yes':
        exit()
    else:
        return

    # button method that changes the color
def colorChange():
    global triangleColor
    # gets color from entry box
    triangleColor = str(colorEntry.get())
    # draws new triangles after the color (global variable) is changed
    drawSierpinski(sliderValue.get())

    # slider Method which changes the depth/"density" of triangles
def sliderChange(event):
    # triangleColor = str(colorEntry.get())
    drawSierpinski(sliderValue.get())
    
    # method for calculating mid points for triangles.
def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2)/2, (y1+y2)/2

def sierpinski(A, B, C, depth):
    # base case of recursive function
    if depth == 0:
        return

    # coordinates of smaller triangles
    MAB = midpoint(A, B)
    MAC = midpoint(A, C)
    MBC = midpoint(B, C)
    # new smaller triangle is created
    graphCanvas.create_polygon([MAB, MAC, MBC], fill='black')
    graphCanvas.pack()
    # calling recursive methods, mid points are new coordinates of small triangles
    sierpinski(A, MAB, MAC, depth-1)
    sierpinski(MAB, B, MBC, depth-1)
    sierpinski(MAC, MBC, C, depth-1)


    # method for creating original triangle that calls the recursive method
def drawSierpinski(depth):

    # size of the initial triangle
    # fitted size is 300
    l = 300

    A, B, C = (0, l-25), (l/2, 0), (l, l-25)

    # cleares canvas to reduce memory leak
    graphCanvas.delete('all')
    #print("drawSierpinski" + color)
    graphCanvas.create_polygon([A, B, C], fill = triangleColor)
    graphCanvas.pack()

    sierpinski(A, B, C, depth)

    # language changer
def toggle():
    
    # print(languageButton.config('text'))
    # ('text', 'text', 'Text', '', 'Srpski')
    if languageButton.config('text')[-1] == 'English':
        # changes button text
        languageButton.config(text='Srpski')
        # changes about content
        about.config(text='The Sierpiński triangle is a fractal with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.')

    else:
        # changes button text
        languageButton.config(text='English')
        # changes about content
        about.config(text='Trougao Sjerpinjskog je fraktal u obliku jednakostraničnog trougla, podeljen rekurzivno u manje jednakostranične trouglove.')



if __name__ == "__main__":
    # root window settings
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Sierpinski Triangle")
    root.resizable(False, False)

    # frame for the canvas
    graphFrame = tk.LabelFrame(root, text='Sierpinski Triangle')
    graphFrame.place(x=0, y=0)

    graphCanvas = Canvas(graphFrame, width=300, height=275)

    # frame for about section
    aboutFrame = tk.LabelFrame(root, text='About')
    aboutFrame.place(x=310, y=0)

    about = tk.Label(aboutFrame, wraplength=190, justify=LEFT, text='The Sierpiński triangle is a fractal\nwith the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.')
    about.pack()

    # original triangle color variable
    global triangleColor
    triangleColor = 'white'

    # variables must be tk.Vars
    sliderValue = tk.IntVar()
    colorValue = tk.StringVar()

    # frame for Settings 
    settingsFrame = tk.LabelFrame(root, text= 'Settings', width=190, height=150)
    settingsFrame.place(x=310, y=100)
    
    # Color section
    colorText = Message(settingsFrame, text='Color:')
    colorText.place(x =0, y=0)

    colorEntry = Entry(settingsFrame, width=10)
    colorEntry.place(x=45, y=2)
    
    colorButton = ttk.Button(settingsFrame, width= 7,text='Submit', command = colorChange)
    colorButton.place(x=110, y=-1)
 
    # Depth section
    sliderText = Message(settingsFrame, text='Depth:')
    sliderText.place(x=0, y=45)

    slider = Scale(settingsFrame, from_=0, to=6, length=100, sliderlength=20, troughcolor='gray', width=15, orient = HORIZONTAL, command=sliderChange, variable=sliderValue)
    slider.place(x=45, y=27)

    # Language section
    languageText = Message(settingsFrame, text='Language:', width=60)
    languageText.place(x=0, y=90)

    languageButton = ttk.Button(settingsFrame, text="Srpski", width=10, command=toggle)
    languageButton.place(x=70, y=90)

    # Exit section
    exitButton = ttk.Button(root, text='Exit', command = ex)
    exitButton.place(x=370, y=265)
    
    # starting method
    drawSierpinski(0)

    root.mainloop()