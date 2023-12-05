from tkinter import *
from subprocess import call
import subprocess
import sys

raiz = Tk()
raiz.title("Menu de tareas")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
raiz.config(bg="white")


#funciones
Usuario = ''
Contraseña = ''
if __name__ == "__main__":
    # Recibir los datos de usuario y contraseña como argumentos
    Usuario = sys.argv[1]
    Contraseña = sys.argv[2]
    print(f"Usuario tareas: {Usuario}")
    print(f"Contraseña: {Contraseña}")

def fun_1(event):
    subprocess.Popen(['python', 'nuevatarea.py', Usuario, Contraseña])
    raiz.destroy()
    

def fun_2(event):
    raiz.destroy()
    subprocess.Popen(['python', 'main.py', Usuario, Contraseña])

def fun_3(event):
    raiz.destroy()
    subprocess.Popen(['python', 'buscar_tareas.py', Usuario, Contraseña])
    

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

label_3 = Label(frame_1,text="Regresar")
#-----------------------------------------------------------------------------------------------------
#configuracion de labels
label_1.config(bg="blue",fg="white",font=("Roboto condensed",20),cursor="hand2")
label_1.place(x=80,y=150)

label_2.config(bg="orange",fg="white",font=("Roboto condensed",20),cursor="hand2")
label_2.place(x=90,y=180)

label_3.config(bg="blue",fg="white",font=("Roboto condensed",20),cursor="hand2")
label_3.place(x=0,y=0)
#botones de label
label_1.bind("<Button-1>",fun_1)

label_3.bind("<Button-1>",fun_2)

label_2.bind("<Button-1>",fun_3)
raiz.mainloop()