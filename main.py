import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox



def ex():
    answer = tk.messagebox.askquestion('Exit', 'Do you wish to exit the program?')
    if answer == 'yes':
        exit()
    else:
        return

def colorChange():

    triangleColor = str(colorEntry.get())
    print(triangleColor)
    drawSierpinski(currentValue.get(), triangleColor)

def sliderChange(event):
    triangleColor = str(colorEntry.get())
    drawSierpinski(currentValue.get(), triangleColor)
    

def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2)/2, (y1+y2)/2


def sierpinski(A, B, C, depth):
    if depth == 0:
        return

    MAB = midpoint(A, B)
    MAC = midpoint(A, C)
    MBC = midpoint(B, C)
    graphCanvas.create_polygon([MAB, MAC, MBC], fill='black')
    graphCanvas.pack()
    sierpinski(A, MAB, MAC, depth-1)
    sierpinski(MAB, B, MBC, depth-1)
    sierpinski(MAC, MBC, C, depth-1)



def drawSierpinski(depth, color='white'):

    l = 300

    A, B, C = (0, 275), (l/2, 0), (l, 275)

    graphCanvas.delete('all')
    print("drawSierpinski" + color)
    graphCanvas.create_polygon([A, B, C], fill = color)
    graphCanvas.pack()

    sierpinski(A, B, C, depth)

def toggle():
    
    #print(toggle_button.config('text'))
    #('text', 'text', 'Text', '', 'Srpski')
    
    if toggle_button.config('text')[-1] == 'English':
        toggle_button.config(text='Srpski')
        about.config(text='The Sierpiński triangle is a fractal with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.')

    else:
        toggle_button.config(text='English')
        about.config(text='Trougao Sjerpinjskog je fraktal u obliku jednakostraničnog trougla, podeljen rekurzivno u manje jednakostranične trouglove.')



if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("500x300")
    root.title("Sierpinski Triangle")
    root.resizable(False, False)

    graphFrame = tk.LabelFrame(root, text='Sierpinski Triangle')
    graphFrame.place(x=0, y=0)

    graphCanvas = Canvas(graphFrame, width=300, height=275)

    currentValue = tk.IntVar()
    colorValue = tk.StringVar()


    aboutFrame = tk.LabelFrame(root, text='About')
    aboutFrame.place(x=310, y=0)

    about = tk.Label(aboutFrame, wraplength=190, justify=LEFT, text='The Sierpiński triangle is a fractal\nwith the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.')
    about.pack()

    drawSierpinski(0)

    settingsFrame = tk.LabelFrame(root, text= 'Settings', width=190, height=150)
    settingsFrame.place(x=310, y=100)
    
    colorText = Message(settingsFrame, text='Color:')
    colorText.place(x =0, y=0)

    colorEntry = Entry(settingsFrame, width=10)
    colorEntry.place(x=45, y=2)
    
    colorButton = ttk.Button(settingsFrame, width= 7,text='Submit', command = colorChange)
    colorButton.place(x=110, y=-1)
 
    sliderText = Message(settingsFrame, text='Depth:')
    sliderText.place(x=0, y=45)

    slider = Scale(settingsFrame, from_=0, to=6, length=100, sliderlength=20, troughcolor='gray', width=15, orient = HORIZONTAL, command=sliderChange, variable=currentValue)
    slider.place(x=45, y=27)

    languageText = Message(settingsFrame, text='Language:', width=60)
    languageText.place(x=0, y=90)

    toggle_button = ttk.Button(settingsFrame, text="Srpski", width=10, command=toggle)
    toggle_button.place(x=70, y=90)

    exitButton = ttk.Button(root, text='Exit', command = ex)
    exitButton.place(x=370, y=265)
    
    root.mainloop()