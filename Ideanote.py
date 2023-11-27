import customtkinter as ctk

# background_color = "#464646"
# principal_color = "#262626"
class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = ctk.CTkButton(self, text="Adicionar nova ideia")
        self.button.grid(row=0, column=0, padx=20, pady=20)
        
class Ideanote(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        
        self.title("Ideanote")
        # self.geometry("1200x700")
        self.geometry("800x400")
        self.resizable(width= True, height= True)
        self._set_appearance_mode("dark")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frameSide = SideFrame(self)
        self.frameSide.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.textbox = ctk.CTkTextbox(self, padx=20, pady=20)
        self.textbox.grid(row=0, column=1, columnspan=2,padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    ideanote = Ideanote()
    ideanote.mainloop()