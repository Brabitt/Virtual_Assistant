import tkinter as tk


window = tk.Tk()
window.geometry('900x600')

frame1 = tk.Frame(master=window, width=400, height=100, bg='red')
frame1.pack(fill=tk.BOTH, side=tk.LEFT)

test = tk.Button(text='hello').pack(side='bottom')

window.mainloop()
