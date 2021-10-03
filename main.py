import webbrowser
from tkinter import *
root = Tk()
root.title("Web")
root.geometry("300x300")
def google():
    webbrowser.open("www.google.com")
mygoogle = Button(root, text="Abre Google", bg="yellow", fg="black", command=google).pack(pady=20)
def Youtube():
    webbrowser.open("www.youtube.com/guerrerosdelaredmichelylopez")
myyoutube = Button(root, text="Abre Guerreros de la Red", bg="blue", fg="white", command=Youtube).pack(pady=20)
def Facebook():
    webbrowser.open("www.facebook.com")
myface = Button(root, text="Abre Facebook", bg="red", fg="white", command=Facebook).pack(pady=20)
root.mainloop()
