from tkinter import *

root = Tk()
board = Canvas(root, width=400, height=400, bg="black")
board.create_rectangle(100, 100, 200, 250, fill="green")
board.pack()
mainloop()



board.create_line(0, 0, 200, 300, fill="green")
board.create_rectangle(150, 150, 250, 250, fill="blue")
board.create_oval(400, 50, 20, 20, fill="red")