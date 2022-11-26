import tkinter as tk
from tkinter import *

def get_current_value():
    return current_value.get()

def slider_changed(event):
    draw_sierpinski(get_current_value())
    

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


def draw_sierpinski(depth):
    l = 300

    A, B, C = (0, 275), (l/2, 0), (l, 275)

    graphCanvas.create_polygon([A, B, C], fill='red')
    graphCanvas.pack()

    sierpinski(A, B, C, depth)




if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("500x300")
    root.title("Sierpinski Triangle")
    root.resizable(False, False)

    graphFrame = tk.LabelFrame(root, text='Sierpinski Triangle')
    graphFrame.place(x=0, y=0)

    textFrame = tk.LabelFrame(root, text='About')
    textFrame.place(x=310, y=50)

    text = tk.Label(textFrame, wraplength=200, justify=LEFT, text='The Sierpiński triangle is a fractal\nwith the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles.')
    text.pack()

    graphCanvas = Canvas(graphFrame, width=300, height=300)

    current_value = tk.IntVar()

    draw_sierpinski(0)

    slider = Scale(root, from_=0, to=6, orient = HORIZONTAL, command=slider_changed, variable=current_value)
    slider.place(x= 350, y =0)

    root.mainloop()