#Menu principal
from tkinter import *
from subprocess import call
import subprocess
import sys

raiz = Tk()
raiz.title("Menu Principal")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
#-----------------------------------------------------------------------------------------------------
#Funciones
Usuario = ''
Contraseña = ''
if __name__ == "__main__":
    # Recibir los datos de usuario y contraseña como argumentos
    Usuario = sys.argv[1]
    Contraseña = sys.argv[2]
    print(f"Usuario main: {Usuario}")
    print(f"Contraseña: {Contraseña}")

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
    subprocess.Popen(['python', 'tareas.py', Usuario, Contraseña])
    raiz.destroy()
    

def funsalir(event):
    raiz.destroy()
    call(["python","Inicio.py"])
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#creacion de frames
frame_1 = Frame(raiz,bg="blue")
frame_1.config(width=1200,height=720)
frame_1.pack(fill="both",expand="True")

#frame izquierdo
frameIzquierdo = Frame(frame_1,bg="red")
frameIzquierdo.config(width=350)
frameIzquierdo.pack(side="left",fill="y")

#frame tareas
frameTareas = Frame(frameIzquierdo, bg="black")
frameTareas.config(width=350,height=80)
frameTareas.place(x=0,y=0)

#Fame
frame_2 = Frame(frameIzquierdo,bg="white")
frame_2.config(width=350,height=80)
frame_2.place(x=0,y=80)

#frame
frame_3 = Frame(frameIzquierdo,bg="black")
frame_3.config(width=350,height=80)
frame_3.place(x=0,y=160)

#frame
frame_4 = Frame(frameIzquierdo,bg="white")
frame_4.config(width=350,height=80)
frame_4.place(x=0,y=240)

#frame
frame_5 = Frame(frameIzquierdo,bg="black")
frame_5.config(width=350,height=80)
frame_5.place(x=0,y=320)

#frame
frame_6 = Frame(frameIzquierdo,bg="white")
frame_6.config(width=350,height=80)
frame_6.place(x=0,y=400)

#frame
frame_7 = Frame(frameIzquierdo,bg="black")
frame_7.config(width=350,height=80)
frame_7.place(x=0,y=480)

#frame
frame_8 = Frame(frameIzquierdo,bg="white")
frame_8.config(width=350,height=80)
frame_8.place(x=0,y=560)

#frame
frame_9 = Frame(frameIzquierdo,bg="black")
frame_9.config(width=350,height=80)
frame_9.place(x=0,y=640)
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#Definicion de labels
label_1 =   Label(frameTareas,text="Modulo De Tareas")
salir = Label(frame_9,text="Cerrar sesion")
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#configuracion de labels
label_1.config(bg="black",fg="white",cursor="hand2",font=("Roboto condensed",20))
label_1.place(x=80,y=40)

salir.config(bg="black",font=("Roboto condensed",20),fg="white",cursor="hand2")
salir.place(x=100,y=20)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#eventos de label
label_1.bind("<Button-1>",fun_1)

salir.bind("<Button-1>",funsalir)
#-----------------------------------------------------------------------------------------------------

raiz.mainloop()