import tkinter.font as tkFont
from tkinter import *

root = Tk()

frame = Frame(root, width=600, height=0)
frame.pack()

font = tkFont.Font(family='Helvetica', size=16, weight='normal')
result_font = tkFont.Font(family='Helvetica', size=22, weight='bold')

canvas_width = 600
canvas_height = 440

w = canvas_width // 2
h = canvas_height // 2

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
canvas.create_rectangle(30, 30, canvas_width-30, canvas_height, fill='grey')
canvas.create_text(w, 50, text="RED RIDING HOOD", fill='white', font=font)

# canvas.create_text(w-30, h+30, text=introduction, fill='white', justify='center', font=introFont)
