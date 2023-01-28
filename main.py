import tkinter
import customtkinter

app=customtkinter.CTk()

#Initialize Variables
refreshRate = 500 #Main loop runs ~500 times a second

#Initialize Window Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app.title("Omniviewer")
app.geometry("750x450")

#Main Loop
def loop():
    
    app.attributes("-topmost", True) #bring to front
    app.after(round(1000/refreshRate), loop) #continuously run the loop

#Functions
def test():
    print(f"Width: {app.winfo_width()}\nHeight: {app.winfo_height()}")

#Initialize Items on Screen
fileSelector=customtkinter.CTkButton(master=app, text="Debugger", command=test)
fileSelector.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#Run the program
app.after(1, loop)
app.mainloop()
