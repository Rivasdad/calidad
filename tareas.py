from tkinter import *
from subprocess import call


raiz = Tk()
raiz.title("Menu de tareas")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
raiz.config(bg="white")


#funciones

#funcion para centrar la interfaz grafica
def center_window(window, width, height):
    # Obtén el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula las coordenadas para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Establece las coordenadas de la ventana
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(raiz,ancho_ventana, alto_ventana)


#frames 

#frame crear tarea
frame_1 = Frame(raiz,bg="blue")
frame_1.config(width=350,height=350)
frame_1.place(x=0,y=0)
#-----------------------------------------------------------------------------------------------------
#frame observar tarea
frame_2 =Frame(raiz,bg="orange")
frame_2.config(width=350,height=370)
frame_2.place(x=0,y=350)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#labels

#label tareas
label_1 = Label(frame_1,text="Agregar una Tarea")

#label observar tareas
label_2 =Label(frame_2,text="Buscar tareas")
#-----------------------------------------------------------------------------------------------------
#configuracion de labels
label_1.config(bg="blue",fg="white",font=("Roboto condensed",20),cursor="hand2")
label_1.place(x=80,y=150)

label_2.config(bg="orange",fg="white",font=("Roboto condensed",20),cursor="hand2")
label_2.place(x=90,y=180)
raiz.mainloop()