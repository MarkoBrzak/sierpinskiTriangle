import tkinter as tk
from tkinter import *
from tkinter import ttk

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
    w.create_polygon([MAB, MAC, MBC], fill='white')
    w.pack()
    sierpinski(A, MAB, MAC, depth-1)
    sierpinski(MAB, B, MBC, depth-1)
    sierpinski(MAC, MBC, C, depth-1)


def draw_sierpinski(depth):
    l = 300

    A, B, C = (0, 275), (l/2, 0), (l, 275)

    global w 

    w.create_polygon([A, B, C], outline='white')
    w.pack()

    sierpinski(A, B, C, depth)




if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("500x300")
    root.title("Sierpinski Triangle")
    root.resizable(False, False)

    frame = tk.LabelFrame(root, text='Sierpinski Triangle')
    frame.place(x=0, y=0)

    w = Canvas(frame, width=300, height=300)

    current_value = tk.IntVar()

    draw_sierpinski(0)

    slider = Scale(root, from_=0, to=6, orient = HORIZONTAL, command=slider_changed, variable=current_value)
    slider.place(x= 350, y =0)

    root.mainloop()