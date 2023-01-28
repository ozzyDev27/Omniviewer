import tkinter
import customtkinter
import os

app=customtkinter.CTk()

# --------------------------- Initialize Variables --------------------------- #
viewer=None #?will be replaced at later point in UX, just for now so that main loop doesnt bug
refreshRate = 500 #?Main loop runs ~500 times a second
sidebarPadding=163
defaultBackgroundColor="#242424"
defaultForegroundColor="#ffffff"

# ------------------------ Initialize Window Settings ------------------------ #
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app.title("Omniviewer")
app.geometry("750x450")
app.iconbitmap(r"assets\logo.ico") #TODO: Make this work - icon does not show

# --------------------------------- Functions -------------------------------- #
def test():
    print(f"Width: {app.winfo_width()}\nHeight: {app.winfo_height()}") #?prints size of window

def getFileType(fileName):
    return os.path.splitext(fileName)[1][1:]

def txt(filePath):
    with open(filePath, 'r') as file:
        return file.read()

def fileSelect():
    global viewer
    openFile=tkinter.filedialog.askopenfilename()
    print(getFileType(openFile))
    try:
        viewer.pack_forget() #?deletes the "viewer" widget from screen
    except:pass #?unless viewer hasnt been declared yet
    
    if getFileType(openFile)=="txt":
        viewer=tkinter.Text(app,bg=defaultBackgroundColor,fg=defaultForegroundColor,wrap=tkinter.WORD)
        viewer.insert(tkinter.INSERT,txt(openFile))
        viewer.pack(side=tkinter.RIGHT,expand=True,fill=tkinter.BOTH)
        viewer.config(state=tkinter.DISABLED)
        viewer.place(width=app.winfo_width()-sidebarPadding,height=app.winfo_height(),anchor=tkinter.E,relx=1,rely=0.5)

    

# --------------------------------- Main Loop -------------------------------- #
def loop():
    try:viewer.place(width=app.winfo_width()-sidebarPadding,height=app.winfo_height())
    except:pass

    app.lift() #?bring to front
    app.after(round(1000/refreshRate), loop) #?continuously run the loop

# ------------------------ Initialize Widgets on Screen ------------------------ #
#debugButton=customtkinter.CTkButton(master=app, text="Debugger", command=test)
#debugButton.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)

fileSelector=customtkinter.CTkButton(master=app, text="Select File", command=fileSelect)
fileSelector.place(x=10, y=10, anchor=tkinter.NW)

# ------------------------------ Run the program ----------------------------- #
app.after(1, loop)
app.mainloop()
