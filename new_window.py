def new_window():
    new_window = ctk.CTkToplevel(window)
    new_window.geometry("200x200")


btnGotoNovaTela = ctk.CTkButton(master=window, text="Abrir nova tela", command=new_window).place(x=300, y=100)