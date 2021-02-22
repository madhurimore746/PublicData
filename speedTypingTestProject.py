from tkinter import *
from timeit import default_timer as timer
import random

#To create window
window = Tk()
#To set window size
window.geometry("400x200")

x=0
def game():
    global x
    if x == 0:
        #to destroy initial window
        window.destroy()
        x = x+1
    def check_result():
        if entry.get()==words[word]:
            end = timer()
            print(end-start)
        else:
            print("Wrong Spelling")    
    words = ['programming','coding','youtube','chrome','MyNameIsMadhuri','sayali','ruta']
    #choose the random word from list
    word = random.randint(0,(len(words)-1))
    #to start timer
    start = timer()
    #create window
    windows = Tk()
    windows.geometry("500x300")
    #select one word from the words list
    x2 = Label(windows,text=words[word],font="times 13")
    x2.place(x=150,y=10)
    
    x3 = Label(windows,text="Lets see how fast you can write..",font="times 12")
    x3.place(x=10,y=50)
    entry = Entry(windows)
    entry.place(x=280,y=55)
    
    b2=Button(windows,text="Submit",command=check_result,width=15,bg='gray')
    b2.place(x=150,y=100)
    
    b3=Button(windows,text="wanna try again",command=game,width=15,bg='gray')
    b3.place(x=250,y=100)
    windows.mainloop()

x1 = Label(window,text="Let's start the game...",font="times 13")
x1.place(x=10,y=50)

b1=Button(window,text="Goo",command=game,width=15,bg='gray')
b1.place(x=150,y=100)
window.mainloop()
