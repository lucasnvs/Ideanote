import customtkinter as ctk

background_color = "#464646";
principal_color = "#262626";

# Função para chamar print
def call_print(value):
    return lambda: print(value)

# Criando Janela
window = ctk.CTk(fg_color=background_color)

# Configurando Janela
window.title("App")
window.geometry("1200x700")
window.resizable(width= False, height= False)

# Tema da Janela
window._set_appearance_mode("dark")

frameSide = ctk.CTkFrame(
    window, 
    width=300, 
    height=500, 
    fg_color=principal_color, 
    bg_color="transparent", 
    corner_radius=6
    ).place(x=20,y=(700 - 500 - 20))

framePrincipal = ctk.CTkFrame(
    window, 
    width=(1200 - 3*20 - 300), 
    height=660, 
    fg_color=principal_color, 
    corner_radius=6
    ).place(x=(2*20 + 300), y=20)

buttonNewIdea = ctk.CTkButton(
    master=window, 
    width=300, 
    height=60, 
    corner_radius=6, 
    fg_color=principal_color, 
    border_width=2, 
    border_color="blue", 
    text_color="blue",
    text="Nova Ideia", 
    command=call_print("Nova ideia")
    ).place(x=20, y=20)

window.mainloop();