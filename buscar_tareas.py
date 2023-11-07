from tkinter import   *
from tkinter import ttk
from conexion import conectar_a_base_de_datos
from subprocess import call


def regresar():
    ventana.destroy()
    call(["python", "tareas.py"])

def capturar_numero_tarea(event):
    seleccion = tabla.selection()
    if seleccion:
        fila_seleccionada = seleccion[0]  # Obtiene la primera fila seleccionada
        numero_tarea = tabla.item(fila_seleccionada, "values")[0]  # El índice 0 representa la primera columna
        print(f"Número de Tarea seleccionado: {numero_tarea}")
        NumeroTarea_txt.delete(0,"end")
        NumeroTarea_txt.insert(0,numero_tarea)

def obtener_tareas():
    # Obtener la conexión a la base de datos desde el archivo conexion.py
    conexion = conectar_a_base_de_datos()

    # Realizar una consulta para obtener los campos deseados
    cursor = conexion.cursor()
    cursor.execute("SELECT numero_tarea, nombre_tarea, responsable, cedula_responsable, estatus_tarea, porcentaje_avance, fecha_inicio, fecha_culminacion FROM tareas")
    tareas = cursor.fetchall()
    conexion.close()

    # Limpia la tabla existente, si la hay
    for fila in tabla.get_children():
        tabla.delete(fila)

    # Agregar las tareas a la tabla
    for tarea in tareas:
        tabla.insert("", "end", values=tarea)

ventana = Tk()
ventana.title("Tabla de Tareas")

# Proporciones de la ventana
ancho_ventana = 1200
alto_ventana = 720
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
ventana.config(bg="#002D64")
ventana.resizable(0,0)


# Crear un Treeview
tabla = ttk.Treeview(ventana, columns=("Número de Tarea", "Nombre de Tarea", "Responsable", "Cédula del Responsable", "Estatus de Tarea", "Porcentaje de Avance", "Fecha de Inicio", "Fecha de Culminación"))

# Definir las columnas
tabla.heading("#1", text="Número Tarea")
tabla.heading("#2", text="Nombre Tarea")
tabla.heading("#3", text="Responsable")
tabla.heading("#4", text="Cédula")
tabla.heading("#5", text="Estatus")
tabla.heading("#6", text="Porcentaje Avance")
tabla.heading("#7", text="Fecha Inicio")
tabla.heading("#8", text="Fecha Culminación")

# Ajustar el ancho de las columnas
tabla.column("#0", width=0, stretch=NO)
tabla.column("#1", width=60)  # Número de Tarea
tabla.column("#2", width=200)  # Nombre de Tarea (más pequeño)
tabla.column("#3", width=100)  # Responsable
tabla.column("#4", width=100)  # Cédula del Responsable (más pequeño)
tabla.column("#5", width=100)  # Estatus de Tarea (más pequeño)
tabla.column("#6", width=100)  # Porcentaje de Avance (más pequeño)
tabla.column("#7", width=150)  # Fecha de Inicio
tabla.column("#8", width=150)  # Fecha de Culminación


tabla.place(x=0,y=0,width=1200)
tabla.configure(height=5)



# Botón para obtener las tareas de la base de datos y mostrarlas en la tabla
boton = ttk.Button(ventana, text="Listar Tabla", cursor="hand2" ,command=obtener_tareas)
boton.place(x=0,y=600)

regresar_b = ttk.Button(ventana, text="Regresar", cursor="hand2",command=regresar)
regresar_b.place(x=100,y=600)

tabla.bind("<<TreeviewSelect>>", capturar_numero_tarea)

#labels
NumeroTarea = Label(ventana,text="Numero Tarea")
Nombretarea = Label(ventana,text="Nombre Tarea")
Responsable = Label(ventana,text="Responsable")
cedula = Label(ventana,text="Cedula")
Estatus = Label(ventana,text="Estatus")
Avance = Label(ventana,text="Avance")
FechaInicio = Label(ventana,text="Fecha Inicio")
FechaFin = Label(ventana,text="Fecha Culminacion")

#configuracion labels
NumeroTarea.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13)) #numero tarea
NumeroTarea.place(x=0,y=300)

Nombretarea.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
Nombretarea.place(x=150,y=300)

Responsable.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
Responsable.place(x=0,y=380)

cedula.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
cedula.place(x=180,y=380)

Estatus.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
Estatus.place(x=19,y=450)

Avance.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
Avance.place(x=173,y=450)

FechaInicio.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
FechaInicio.place(x=0,y=515)

FechaFin.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
FechaFin.place(x=130,y=515)

#campos de texto
NumeroTarea_txt = Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

Nombretarea_txt= Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))

Responsable_txt= Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

cedula_txt = Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))

Estatus_txt = Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

Avance_txt = Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))

FechaInicio_txt = Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

FechaFin_txt = Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))



# Conficuracion de campos de texto
NumeroTarea_txt.place(x=0,y=325)

Nombretarea_txt.place(x=118,y=325)

Responsable_txt.place(x=0,y=405)

cedula_txt.place(x=119,y=405)

Estatus_txt.place(x=0,y=475)

Avance_txt.place(x=119,y=475)

FechaInicio_txt.place(x=0,y=540)

FechaFin_txt.place(x=119,y=540)




# textos de area

descripcion = Text(ventana,width=50,height=10)
descripcion.place(x=300,y=323)
scrollbar = Scrollbar(ventana, command=descripcion.yview)  #scroll
scrollbar.place(x=710,y=328,height=150) 
descripcion.config(yscrollcommand=scrollbar.set)





ventana.mainloop()
