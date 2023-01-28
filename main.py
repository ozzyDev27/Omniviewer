import tkinter
import customtkinter

omni=customtkinter.CTk()

#Initialize Variables
refreshRate = 500 #Main loop runs 500 times a second

#Initialize Appearance
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
omni.iconphoto(False, tkinter.PhotoImage(file=r"assets\logo.png"))

#Main Loop
def loop():

    omni.after(1000/refreshRate, loop)

#Functions
def fileSelect():
    print("button pressed lol")

#Initialize Items on Screen
fileSelector=customtkinter.CTkButton(master=omni, text="Select File", command=fileSelect)
fileSelector.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Run the program
omni.after(1, loop) #runs 1 millisecond after omni starts
omni.mainloop()
