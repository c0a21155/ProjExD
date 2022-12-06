import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""



def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if key == "w": my -= 2
    if key == "a": mx -= 2
    if key == "s": my += 2
    if key == "d": mx += 2
    if maze_lst[mx][my] == 1:
            if key == "Up": my += 1
            if key == "Down": my -= 1
            if key == "Left": mx += 1
            if key == "Right": mx -= 1
            if key == "w": my += 2
            if key == "a": mx += 2
            if key == "s": my -= 2
            if key == "d": mx -= 2
    cx, cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)
    if cx == 1350:
        if cy == 150:
            canvas.coords("kokaton2", cx, cy)
    if cx == 1350:
        if cy == 750:
            root.destroy()

    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15, 9)
    # print(maze_lst)
    mm.show_maze(canvas, maze_lst)


    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/4.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    tori1 = tk.PhotoImage(file="fig/1.png")
    canvas.create_image(1350, 750, image=tori1, tag="kokaton1")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()