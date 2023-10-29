#Menu principal
from tkinter import *
raiz = Tk()
raiz.title("Menu Principal")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
#-----------------------------------------------------------------------------------------------------
#Funciones

#-----------------------------------------------------------------------------------------------------
#funcion para centrar la pestaña
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
#-----------------------------------------------------------------------------------------------------


#funcion para los label
def fun_1(event):
    frame_1.config(bg="red")
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#creacion de frames
frame_1 = Frame(raiz,bg="blue")
frame_1.config(width=1200,height=720)
frame_1.pack()

#frame izquierdo
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#Definicion de labels
label_1 =   Label(frame_1,text="Menú de Tareas")
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#configuracion de labels
label_1.config(bg="blue",fg="white",cursor="hand2")
label_1.place(x=500,y=200)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#eventos de label
label_1.bind("<Button-1>",fun_1)
#-----------------------------------------------------------------------------------------------------

raiz.mainloop()