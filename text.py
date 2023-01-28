import os
import tkinter
import customtkinter

def txt(filePath):
    with open(filePath, 'r') as file:
        return file.read()