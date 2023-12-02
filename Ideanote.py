import customtkinter as ctk
from Menu import Menu

# background_color = "#464646"
# principal_color = "#262626"
ctk.set_default_color_theme("./themes/myDark.json")

class Ideanote(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        
        self.title("Ideanote")
        self.geometry("1200x700")
        self.resizable(width= True, height= True)
        self.minsize(width=800, height=400)
        self._set_appearance_mode("dark")

        self.menu = Menu(self)
        self.config(menu=self.menu)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.columnconfigure(0, minsize=300)

        self.frameSide = SideFrame(self)
        self.frameSide.grid(row=0, rowspan=2, column=0, padx=20, pady=20, sticky="nsew")

        self.frameMain = MainFrame(self)
        self.frameMain.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")
        
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

        self.button = ctk.CTkButton(self, text="Adicionar nova ideia", cursor="hand2")
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.scrollFrame = IdeiaScrollFrame(self, fg_color="transparent")
        self.scrollFrame.grid(row=1, rowspan=2, column=0, sticky="nsew")


class IdeiaScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.range = range(0,6)
        for i in self.range:
            IdeiaWidget(self, fg_color="#FFF").grid(row=i, column=0, pady=10, ipady=10, sticky="ew")


class IdeiaWidget(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.title = ctk.CTkLabel(self, text="Tema Vscode", corner_radius=6, anchor="w", font=("size", 19))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.desc = ctk.CTkLabel(self, text="Fazer um tema personalizado para implementar no vscode.", wraplength=250, anchor="w", justify="left")
        self.desc.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.removeBtn = ctk.CTkButton(self, text="Remover", cursor="hand2")
        self.removeBtn.grid(row=2, column=0, padx=5, sticky="ew")

        self.editBtn = ctk.CTkButton(self, text="Editar", cursor="hand2")
        self.editBtn.grid(row=2, column=1, padx=5, sticky="ew")

if __name__ == "__main__":
    ideanote = Ideanote()
    ideanote.mainloop()