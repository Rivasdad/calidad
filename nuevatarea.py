from tkinter import *
from subprocess import call
from tkinter import ttk

raiz = Tk()
raiz.title("Creacion de nueva tarea")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
raiz.config(bg="#002D64")
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

#frame 

frame_1 = Frame(raiz,bg="red")
frame_1.config(width=350,height=140)
frame_1.place(x=500,y=0)
#labels
#-----------------------------------------------------------------------------------------------------
label_1 = Label(raiz,text="Nombre de tarea")
label_2 = Label(raiz,text="Descripcion de la Tarea")
label_3 = Label(raiz,text="fecha de inicio")
label_4 = Label(raiz,text="Responsable")
label_5 = Label(raiz,text="Cedula del responsable")
label_6 = Label(raiz,text="Estatus")
#-----------------------------------------------------------------------------------------------------

#configuracion de labels
#-----------------------------------------------------------------------------------------------------
label_1.place(x=135,y=20)
label_1.config(font=("Roboto condensed Light", 13),fg="white",bg="#002D64")

label_2.place(x=800,y=500)
label_2.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_3.place(x=50,y=150)
label_3.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_4.place(x=50,y=200)
label_4.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_5.place(x=50,y=400)
label_5.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_6.place(x=50,y=450)
label_6.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
#-----------------------------------------------------------------------------------------------------

#campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea =Entry(raiz,width=35,justify="center",font=("Roboto condensed Light", 13))


ResponsableTarea = Entry(raiz,width=22,justify="center",font=("Roboto condensed Light", 13))
#-----------------------------------------------------------------------------------------------------

#configuracion de campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea.place(x=50,y=50,height=24)
ResponsableTarea.place(x=150,y=200,height=24) 
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#texto de area
descripcion = Text(raiz,width=10,height=5)
descripcion.place(x=50,y=240)
scrollbar = Scrollbar(raiz, command=descripcion.yview)  #scroll
scrollbar.place(x=140,y=240,height=100) 
descripcion.config(yscrollcommand=scrollbar.set)


#combo box
#-----------------------------------------------------------------------------------------------------
#combo box para la fecha
#ComboBox para el día
combo_dia = ttk.Combobox(frame_1, values=list(range(1, 32)))
combo_dia.set("Día")
combo_dia.place(x=100,y=0)

# ComboBox para el mes
combo_mes = ttk.Combobox(frame_1, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
combo_mes.set("Mes")
combo_mes.place(x=100,y=50)

# ComboBox para el año
combo_año = ttk.Combobox(frame_1, values=list(range(2000, 2031)))
combo_año.set("Año")
combo_año.place(x=100,y=100)
# #-----------------------------------------------------------------------------------------------------
raiz.mainloop()