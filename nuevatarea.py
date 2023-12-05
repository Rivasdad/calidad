from tkinter import *
from subprocess import call
from tkinter import ttk
from tkinter import messagebox
from conexion import conectar_a_base_de_datos
import subprocess
import sys
import psycopg2

#-----------------------------------------------------------------------------------------------------
raiz = Tk()
raiz.title("Creacion de nueva tarea")
ancho_ventana = 1200
alto_ventana = 720
raiz.resizable(0,0)
raiz.config(bg="#002D64")
#-----------------------------------------------------------------------------------------------------


ResponsableTarea = Entry(raiz,width=35,justify="center",font=("Roboto condensed Light", 13))
CedulaResponsable = Entry(raiz,width=35,justify="center",font=("Roboto condensed Light", 13))
#funciones
#-----------------------------------------------------------------------------------------------------
Usuario = ''
Contraseña = ''
if __name__ == "__main__":
    # Recibir los datos de usuario y contraseña como argumentos
    Usuario = sys.argv[1]
    Contraseña = sys.argv[2]
    try:
        conexion = conectar_a_base_de_datos()
        if conexion:
            cursor = conexion.cursor() 
            sql ="select cedula, nombre from usuario where usuario = '"+Usuario+"'"
            cursor.execute(sql)
            conexion.commit()  
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            
            nombre_bd =''
            cedula_bd =''
            if resultado:
                nombre_bd,cedula_bd= resultado
                ResponsableTarea.insert(0,cedula_bd)
                CedulaResponsable.insert(0,nombre_bd)
        
    except (Exception, psycopg2.DatabaseError) as error:  
         messagebox.showwarning("Usuario no encontrado", "El usuario no ha sido encontrado")
        
#-----------------------------------------------------------------------------------------------------
   

#-----------------------------------------------------------------------------------------------------
def regresar():
    subprocess.Popen(['python', 'tareas.py', Usuario, Contraseña])
    raiz.destroy()
    

#boton pararegresar
regresar = Button(raiz,text="Regresar",command=regresar)
regresar.config(height=1,width=20, cursor="hand2")
regresar.place(x=300,y=650)
#-----------------------------------------------------------------------------------------------------    


#funcion para centrar la interfaz grafica
#-----------------------------------------------------------------------------------------------------
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


#funion para obtener la fecha
#-----------------------------------------------------------------------------------------------------
def obtener_fecha():
   
    dia = combo_dia.get()
    mes = combo_mes.get()
    año = combo_año.get()
    fecha_seleccionada = f"{año}-{mes}-{dia}"

    nombre_tarea_bd = NombreTarea.get()
    responsable_bd = ResponsableTarea.get()
    cedula_bd = CedulaResponsable.get()
    estatus_bd= combo_estatus.get()
    descripcion_bd= descripcion.get("1.0", "end-1c")

    dia_fin = combo_dia_fin.get()
    mes_fin = combo_mes_fin.get()
    año_fin = combo_año_fin.get()
    fecha_seleccionada_fin = f"{año_fin}-{mes_fin}-{dia_fin}"
    
#-----------------------------------------------------------------------------------------------------
    if not dia.isnumeric():
        messagebox.showwarning("Dia invalido", "Ingresa un dia de tarea valido")
    elif not mes.isnumeric():
        messagebox.showwarning("Mes invalido", "Ingresa un Mes de tarea valido")
    elif not año.isnumeric():
        messagebox.showwarning("Año invalido", "Ingresa un Año de tarea valido")

    elif not dia_fin.isnumeric():
        messagebox.showwarning("dia de culminacion invalido", "Ingresa un dia de culminacion valido")
    elif not mes_fin.isnumeric():
        messagebox.showwarning("mes de culminacion invalido", "Ingresa un mes de culminacion  valido")
    elif not año_fin.isnumeric():
        messagebox.showwarning("año de culminacion invalido", "Ingresa un Año de culminacion valido")
    else:   #toda la validacion correcta
        print("hola")
        conexion = conectar_a_base_de_datos()
        if conexion:
            cursor = conexion.cursor() 
            sql ="insert into tareas (nombre_tarea, responsable, cedula_responsable, estatus_tarea, descripcion_tarea, porcentaje_avance, fecha_inicio, fecha_culminacion) values('"+nombre_tarea_bd+"','"+responsable_bd+"','"+cedula_bd+"','"+estatus_bd+"','"+descripcion_bd+"','0','"+fecha_seleccionada+"', '"+fecha_seleccionada_fin+"' )"
            cursor.execute(sql)
            conexion.commit()  # Es importante hacer commit para guardar los cambios en la base de datos
            cursor.close()
            conexion.close()
            print("Todo perfecto")
#-----------------------------------------------------------------------------------------------------


#frame 
#-----------------------------------------------------------------------------------------------------
frame_1 = Frame(raiz,bg="red") #fecha de inicio tarea
frame_1.config(width=240,height=140)
frame_1.place(x=700,y=50)

frame_2 = Frame(raiz,bg="red") #fecha de fin tarea
frame_2.config(width=240,height=140)
frame_2.place(x=950,y=50)
#-----------------------------------------------------------------------------------------------------

#labels
#-----------------------------------------------------------------------------------------------------
label_1 = Label(raiz,text="Nombre de tarea")
label_2 = Label(raiz,text="Descripcion de la Tarea")
label_3 = Label(raiz,text="fecha de inicio")
label_4 = Label(raiz,text="Responsable")
label_5 = Label(raiz,text="Cedula del responsable")
label_6 = Label(raiz,text="Estatus")
label_7 = Label(raiz,text="fecha Culminacion")
#-----------------------------------------------------------------------------------------------------


#configuracion de labels
#-----------------------------------------------------------------------------------------------------
label_1.place(x=135,y=20)
label_1.config(font=("Roboto condensed Light", 13),fg="white",bg="#002D64")

label_2.place(x=48,y=205)  #descripcion de tarea
label_2.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_3.place(x=770,y=20)   #fecha de inicio
label_3.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_4.place(x=500,y=20)
label_4.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_5.place(x=110,y=95)   #cedula responsable
label_5.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_6.place(x=500,y=95)   #estatus
label_6.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))

label_7.place(x=1000,y=20)   #estatus
label_7.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
#-----------------------------------------------------------------------------------------------------


#campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea =Entry(raiz,width=35,justify="center",font=("Roboto condensed Light", 13))



#-----------------------------------------------------------------------------------------------------


#configuracion de campos de texto
#-----------------------------------------------------------------------------------------------------
NombreTarea.place(x=50,y=50,height=24)
ResponsableTarea.place(x=400,y=50,height=24) 
CedulaResponsable.place(x=50,y=127)
#-----------------------------------------------------------------------------------------------------


# Desabilitar campos de texto
#-----------------------------------------------------------------------------------------------------
ResponsableTarea.config(state="readonly")
CedulaResponsable.config(state="readonly")
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#texto de area
descripcion = Text(raiz,width=137,height=20)
descripcion.place(x=50,y=240)
scrollbar = Scrollbar(raiz, command=descripcion.yview)  #scroll
scrollbar.place(x=1155,y=240,height=325) 
descripcion.config(yscrollcommand=scrollbar.set)


#combo box
#-----------------------------------------------------------------------------------------------------
#combo box para la fecha inicio

#ComboBox para el día
combo_dia = ttk.Combobox(frame_1, values=list(range(1, 32)))
combo_dia.set("Día")
combo_dia.place(x=50,y=0)

# ComboBox para el mes
combo_mes = ttk.Combobox(frame_1, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
combo_mes.set("Mes")
combo_mes.place(x=50,y=50)

# ComboBox para el año
combo_año = ttk.Combobox(frame_1, values=list(range(2023, 2100)))
combo_año.set("Año")
combo_año.place(x=50,y=100)

#combo box para el estatus
combo_estatus = ttk.Combobox(raiz,values="Iniciada")
combo_estatus.set("Estatus Tarea")
combo_estatus.place(x=400,y=130,height=28)
combo_estatus.config(width=33,justify="center",font=("Roboto condensed Light", 13))
# -------------------------------------------------------------------------------------------------------


#combo box para la fecha fin
#-----------------------------------------------------------------------------------------------------
#ComboBox para el día
combo_dia_fin = ttk.Combobox(frame_2, values=list(range(1, 32)))
combo_dia_fin.set("Día")
combo_dia_fin.place(x=50,y=0)

# ComboBox para el mes
combo_mes_fin = ttk.Combobox(frame_2, values=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"])
combo_mes_fin.set("Mes")
combo_mes_fin.place(x=50,y=50)

# ComboBox para el año
combo_año_fin = ttk.Combobox(frame_2, values=list(range(2023, 2100)))
combo_año_fin.set("Año")
combo_año_fin.place(x=50,y=100)
#-----------------------------------------------------------------------------------------------------


#botones.
#-----------------------------------------------------------------------------------------------------
#boton para agregar tareas
agregar = Button(raiz,text="agregar Tarea",command=obtener_fecha)
agregar.config(height=1,width=20, cursor="hand2")
agregar.place(x=500,y=650)


#-----------------------------------------------------------------------------------------------------

raiz.mainloop()