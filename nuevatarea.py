from tkinter import *
from subprocess import call

raiz = Tk()
raiz.title("Creacion de nueva tarea")
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


#labels
#-----------------------------------------------------------------------------------------------------
label_1 = Label(raiz,text="Nombre de tarea")
label_2 = Label(raiz,text="Descripcion de la Tarea")
label_3 = Label(raiz,text="fecha de inicio")
label_4 = Label(raiz,text="Responsable")
#-----------------------------------------------------------------------------------------------------

#configuracion de labels
#-----------------------------------------------------------------------------------------------------
label_1.place(x=50,y=50)
label_2.place(x=50,y=100)
label_3.place(x=50,y=150)
label_4.place(x=50,y=200)
#-----------------------------------------------------------------------------------------------------

#campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea =Entry(raiz,width=22,justify="center",font=("Roboto condensed Light", 13))


ResponsableTarea = Entry(raiz,width=22,justify="center",font=("Roboto condensed Light", 13))
#-----------------------------------------------------------------------------------------------------

#configuracion de campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea.place(x=150,y=50,height=24)
ResponsableTarea.place(x=150,y=200,height=24) 
#-----------------------------------------------------------------------------------------------------

raiz.mainloop()