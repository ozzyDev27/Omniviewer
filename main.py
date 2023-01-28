import tkinter
import customtkinter
import os

app=customtkinter.CTk()

#Initialize Variables
refreshRate = 500 #Main loop runs ~500 times a second

#Initialize Window Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app.title("Omniviewer")
app.geometry("750x450")
app.iconbitmap(r"assets\logo.ico") #TODO: Make this work - icon does not show

#Main Loop
def loop():
    
    app.lift() #?bring to front
    app.after(round(1000/refreshRate), loop) #?continuously run the loop

#Functions
def test():
    print(f"Width: {app.winfo_width()}\nHeight: {app.winfo_height()}")

def getFileType(fileName):
    return os.path.splitext(fileName)[1][1:]

def fileSelect():
    openFile=tkinter.filedialog.askopenfilename()
    print(getFileType(openFile))

#Initialize Items on Screen
debugButton=customtkinter.CTkButton(master=app, text="Debugger", command=test)
debugButton.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)

fileSelector=customtkinter.CTkButton(master=app, text="Select File", command=fileSelect)
fileSelector.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Run the program
app.after(1, loop)
app.mainloop()
