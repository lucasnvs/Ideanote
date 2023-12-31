import customtkinter as ctk
from Menu import Menu
from widgets.IdeiaWidget import IdeiaWidget
import data.data as dt
from tkinter import messagebox
import re

ctk.set_default_color_theme("./themes/myDark.json")

class Ideanote(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        
        self.currentFile = False

        self.title("Ideanote")
        self.geometry("1200x700")
        self.resizable(width= True, height= True)
        self.minsize(width=800, height=400)
        self._set_appearance_mode("dark")

        self.menu = Menu(self)
        self.config(menu=self.menu)

        # hotkey to save current file
        self.bind('<Control-s>', self.save_current)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.columnconfigure(0, minsize=300)

        self.frameSide = SideFrame(self)
        self.frameSide.grid(row=0, rowspan=2, column=0, padx=20, pady=20, sticky="nsew")

        self.frameMain = MainFrame(self)
        self.frameMain.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

    def save_current(self, event=False):
        file = self.currentFile
        if file:
            title = self.frameMain.getTitleBox().get("1.0", "end")
            text = self.frameMain.getTextBox().get("1.0", "end")
            title = re.sub(r"\n", "", title)
            text = re.sub(r"\n", "", text)
            file["title"] = title
            file["desc"] = text

        dt.update(file["id"], file)
        # messagebox.showinfo(message='File saved! (fake)' + str(file["id"]))
        
class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="transparent")

        self.titleBox = ctk.CTkTextbox(self, height=30)
        self.titleBox.configure(font=("size", 20), wrap="none")
        self.titleBox.pack(side=ctk.TOP, fill=ctk.X, pady=(0, 20))

        self.textbox = ctk.CTkTextbox(self, font=("size", 16), wrap="word")
        self.textbox.pack(side=ctk.BOTTOM, fill="both", expand=True, ipady=70, ipadx=70) #nao funciona o ipad :(
        
    def getTitleBox(self):
        return self.titleBox
    
    def getTextBox(self):
        return self.textbox

class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.columnconfigure(0, minsize=320)

        self.configure(bg_color="transparent")

        self.button = ctk.CTkButton(self, text="Adicionar nova ideia", cursor="hand2", command=self.new_idea)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.scrollFrame = IdeiaScrollFrame(self, fg_color="transparent")
        self.scrollFrame.grid(row=1, rowspan=2, column=0, sticky="nsew")


    def new_idea(self):
        self.master.title("Nova Ideia")

class IdeiaScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.data = dt.read()
        for ideia in self.data:
            IdeiaWidget(self, ideia, fg_color="#FFF").grid(row=self.data.index(ideia), column=0, pady=10, ipady=10, sticky="ew")

if __name__ == "__main__":
    ideanote = Ideanote()
    ideanote.mainloop()