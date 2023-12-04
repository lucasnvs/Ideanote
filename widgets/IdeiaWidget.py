import data as dt
import customtkinter as ctk


class IdeiaWidget(ctk.CTkFrame):
    def __init__(self, master, ideia, **kwargs):
        super().__init__(master, **kwargs)
        self.ideia = ideia

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.title = ctk.CTkLabel(self, text=ideia["title"], corner_radius=6, anchor="w", font=("size", 19))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.desc = ctk.CTkLabel(self, text=ideia["desc"], wraplength=250, anchor="w", justify="left")
        self.desc.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.removeBtn = ctk.CTkButton(self, text="Remover", cursor="hand2")
        self.removeBtn.grid(row=2, column=0, padx=5, sticky="ew")

        self.editBtn = ctk.CTkButton(self, text="Editar", cursor="hand2", command=self.edit)
        self.editBtn.grid(row=2, column=1, padx=5, sticky="ew")

    def get_root(self):
        frame = self
        while frame.master:
            frame = frame.master

        return frame
    
    def edit(self):  
        
        self.get_root().frameMain.getTitleBox().delete("1.0", "end")
        self.get_root().frameMain.getTextBox().delete("1.0", "end")

        idea = dt.findById(self.ideia.get("id"))

        self.get_root().title(idea.get("title"))
        self.get_root().frameMain.getTitleBox().insert("1.0", idea.get("title"))
        self.get_root().frameMain.getTextBox().insert("1.0", idea.get("desc"))
        self.get_root().currentFile = idea
    
    def printxa(param):
        print(param)