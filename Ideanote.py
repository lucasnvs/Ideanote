import customtkinter as ctk
from Menu import Menu

# background_color = "#464646"
# principal_color = "#262626"

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

        self.frameSide = SideFrame(self)
        self.frameSide.grid(row=0, rowspan=2, column=0, padx=20, pady=20, sticky="ns")

        self.frameMain = MainFrame(self)
        self.frameMain.grid(row=1, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")
        
class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="transparent")

        self.titleBox = ctk.CTkTextbox(self, height=30)
        self.titleBox.configure(font=("size", 20), wrap="none")
        self.titleBox.pack(side=ctk.TOP, fill=ctk.X, pady=(0, 20))

        self.textbox = ctk.CTkTextbox(self, wrap="word")
        self.textbox.pack(side=ctk.BOTTOM, fill="both", expand=True, ipady=70, ipadx=70) #nao funciona o ipad :(
        
    def getTitleBox(self):
        return self.titleBox
    
    def getTextBox(self):
        return self.textbox

class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = ctk.CTkButton(self, text="Adicionar nova ideia")
        self.button.grid(row=0, column=0, padx=20, pady=20)


if __name__ == "__main__":
    ideanote = Ideanote()
    ideanote.mainloop()