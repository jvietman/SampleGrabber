from tkinter import *
import requests, os

root = Tk()
root.title("SampleGrabber")
root.geometry("600x300")
root.resizable(True, False)
root.configure(bg="gray")

label1 = Label(root, text="name:", font=("arial", 15), bg="gray")
label1.place(anchor=CENTER, relx=0.5, rely=0.15)
label2 = Label(root, text="url:", font=("arial", 15), bg="gray")
label2.place(anchor=CENTER, relx=0.5, rely=0.4)

name = Entry(root, font=("arial", 15))
name.place(anchor=CENTER, relx=0.5, rely=0.25, relwidth=0.8)
url = Entry(root, font=("arial", 15))
url.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.8)

btn = Button(root, text="pull", font=("arial", 20), command=lambda: pull(url.get(), name.get()))
btn.place(anchor=CENTER, relx=0.5, rely=0.75, relwidth=0.2)
help = Button(root, text="help", font=("arial", 10), command=lambda: os.startfile("README.md"))
help.place(anchor=CENTER, relx=0.5, rely=0.9, relwidth=0.2)

def pull(url, name):
    response = requests.get(url)
    def filter(msg):
        filters = ['/', '\\', ':', '*', '"', '<', '>', '|']
        str = msg
        for f in filters:
            str = str.replace(f, '')
        return str
    with open(filter(name)+".mp3", "wb") as f:
        f.write(response.content)
        f.close()

root.mainloop()