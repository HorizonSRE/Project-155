from tkinter import *
import random
root=Tk()
root.title("Changing BG")
root.geometry("600x600")
color={"1":"red", "2":"blue", "3":"green"}
def changebg():
    randomno=random.randint(1,3)
    root.configure(background=color[str(randomno)])
btn=Button(root, text="Change Bg",command=changebg)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
    

