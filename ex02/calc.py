import tkinter as tk
import tkinter.messagebox as tkm




# 練習３
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else:
        #tkm.showinfo("", f"{num}ボタンがクリックされました")
        # 練習６
        entry.insert(tk.END, num)

def click_delete(event2):            #"="を右クリックすると、
    click_right = event2.widget      #表示文字列を削除する。
    num = click_right["text"]
    if num == "=":        
        entry.delete(0,tk.END)

    


# 練習１
root = tk.Tk()
root.geometry("300x500")



# 練習４
entry = tk.Entry(root, justify="right", width=10, font=("",40))
entry.grid(row=0, column=0, columnspan=3)


# 練習２
r, c = 1, 2                  #ボタンの順番を並び変える。
for num in range(9,-1,-1):
    button = tk.Button(root, text=f"{num}", width=4, height=2, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c -= 1
    if c == -1:
          
        if r < 3:
            r += 1  
            c = 2
        else:
            r += 1
            c = 0
            r = 4





# 練習５
operators = ["+", "="]
for ope in operators:
    c += 1
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    button.bind("<3>", click_delete) #click_deleteのイベント紐づけ
    if c%3 == 0:
        r += 1
        c = 0






root.mainloop()