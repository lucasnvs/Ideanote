import tkinter as tk
from tkinter import filedialog

class Menu(tk.Menu):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create a file menu
        file_menu = tk.Menu(self)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Create an edit menu
        edit_menu = tk.Menu(self)
        self.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
    

    def new_file(self):
        self.master.frameMain.getTextBox().delete("1.0", "end")
        self.master.title("Ideanote")

    def open_file(self):
        file = filedialog.askopenfile(parent=self.master, mode="rb", title="Open a file")

        if file:
            contents = file.read()
            self.master.frameMain.getTextBox().delete("1.0", "end")
            self.master.frameMain.getTextBox().insert("1.0", contents)
            file.close()
            self.master.title(file.name + " - Ideanote")
            self.master.frameMain.getTitleBox().delete("1.0", "end")

            fileNameFormat = file.name.split("/")
            fileNameFormat = fileNameFormat[len(fileNameFormat) - 1]
            fileNameFormat = fileNameFormat.split(".")
            fileNameFormat = fileNameFormat[0]
            self.master.frameMain.getTitleBox().insert("1.0", fileNameFormat)

    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])

        if file:
            contents = self.master.frameMain.getTextBox().get("1.0", "end")
            file.write(contents)
            file.close()
            self.master.title(file.name + " - Ideanote")

    def cut(self):
        self.master.text.event_generate("<<Cut>>")
    def copy(self):
        self.master.text.event_generate("<<Copy>>")
    def paste(self):
        self.master.text.event_generate("<<Paste>>")