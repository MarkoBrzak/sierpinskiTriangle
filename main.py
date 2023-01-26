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



if __name__ == "__main__":
    # root window settings
    root = tk.Tk()
    root.geometry("305x330")
    root.title("Sierpinski Triangle")
    root.resizable(False, False)

    # frame for the canvas
    graphFrame = tk.LabelFrame(root)
    graphFrame.place(x=0, y=0)

    graphCanvas = Canvas(graphFrame, width=300, height=275)

    # original triangle color variable
    global triangleColor
    triangleColor = 'gray'

    # variables must be tk.Vars
    sliderValue = tk.IntVar()
    colorValue = tk.StringVar()

    
    slider = Scale(root, from_=0, to=7, length=100, sliderlength=20, troughcolor='gray', width=15, orient = HORIZONTAL, command=sliderChange, variable=sliderValue)
    slider.place(x=100, y=285)


    # starting method
    drawSierpinski(0)

    root.mainloop()