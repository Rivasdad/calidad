from tkinter import   *
from tkinter import ttk
from conexion import conectar_a_base_de_datos
from subprocess import call
from tkinter import messagebox
import psycopg2
import subprocess
import sys


Usuario = ''
Contraseña = ''
if __name__ == "__main__":
    # Recibir los datos de usuario y contraseña como argumentos
    Usuario = sys.argv[1]
    Contraseña = sys.argv[2]
    print(f"Usuario: {Usuario}")
    print(f"Contraseña: {Contraseña}")
    
#funcion para limpiar campos
#--------------------------------------------------------------------------------------------------------------
def prueba():
    cod_observacion_txt.delete(0, "end")    
    cod_tareas_txt.delete(0, "end")
    Responsable_txt.delete(0, "end")
    cedula_txt.delete(0, "end")
    descripcion.delete("1.0", "end")
#--------------------------------------------------------------------------------------------------------------


#funcion para modificar la tarea
#--------------------------------------------------------------------------------------------------------------
def modificar():
    try:
        conexion = conectar_a_base_de_datos()
        desc= descripcion.get("1.0", "end-1c")
        sql="update observacion set responsable = '"+Responsable_txt.get()+"', cedula_responsable ='"+Responsable_txt.get()+"', descripcion = '"+desc+"' where cod_observacion='"+cod_observacion_txt.get()+"'"
        cursor = conexion.cursor() 
        cursor.execute(sql)
        conexion.commit() 
        cursor.close()
        conexion.close()
        messagebox.showinfo("Observacion Modificada", "Su Observacion a sido Modificada correctamente")
    except (Exception, psycopg2.DatabaseError) as error: 
     messagebox.showwarning("Error al modificar", "Error al intentar modificar Observacion")
#--------------------------------------------------------------------------------------------------------------


#funcion para filtrar las observaciones en la tabla
#--------------------------------------------------------------------------------------------------------------
def capturar_campos():
    print("")
    
def filtro():
    cod_observacion_bd = cod_observacion_txt.get()
    cod_tareas_bd = cod_tareas_txt.get()
    descripcion_bd= descripcion.get("1.0", "end-1c")
    Responsable_db= Responsable_txt.get()
    cedula_bd= cedula_txt.get()
   
    if cod_observacion_bd:
        conexion = conectar_a_base_de_datos()
        sql="select * from observacion"
        cursor = conexion.cursor() 
        cursor.execute(sql)
        conexion.commit()  
        resultado = cursor.fetchone()

    if resultado:
        cod_observacion_bd, cod_tareas_bd, descripcion_bd, Responsable_db, cedula_bd= resultado
        prueba()
        cod_observacion_txt.insert(0,cod_observacion_bd)
        cod_tareas_txt.insert(0,cod_tareas_bd)
        Responsable_txt.insert(0,Responsable_db)
        cedula_txt.insert(0,cedula_bd)
        descripcion.insert(INSERT,descripcion_bd)
    else:
        messagebox.showwarning("Error", "error al intentar buscar informacion")
    cursor.close()
    conexion.close()
    print("Todo perfecto")


#funcion para regresar al modulo anterior
#--------------------------------------------------------------------------------------------------------------
def regresar():

    subprocess.Popen(['python', 'buscar_tareas.py', Usuario, Contraseña])
    ventana.destroy()
    



#funcion para capturar el numero d tarea cuando se da click en la tabla
#--------------------------------------------------------------------------------------------------------------
def capturar_numero_tarea(event):
    seleccion = tabla.selection()
    if seleccion:
        fila_seleccionada = seleccion[0]  # Obtiene la primera fila seleccionada
        numero_tarea = tabla.item(fila_seleccionada, "values")[0]  # El índice 0 representa la primera columna
        print(f"Número de Tarea seleccionado: {numero_tarea}")
        cod_observacion_txt.delete(0,"end")
        cod_observacion_txt.insert(0,numero_tarea)
#--------------------------------------------------------------------------------------------------------------        


#funcion para buscar una tarea especifica
#--------------------------------------------------------------------------------------------------------------
def Listar_tabla():
    conexion = conectar_a_base_de_datos()
    cursor = conexion.cursor()
    if cod_observacion_txt.get():
        cursor.execute("SELECT cod_observacion, observador, cedula_observador, nombre_responsable, fk_tareas, fk_cedula FROM observacion where cod_observacion = '"+cod_observacion_txt.get()+"'")
    elif cedula_txt.get():
        cursor.execute("SELECT cod_observacion, observador, cedula_observador, nombre_responsable, fk_tareas, fk_cedula FROM observacion FROM observacion where fk_cedula ='"+cedula_txt.get()+"'")
    else:
       cursor.execute("SELECT cod_observacion, observador, cedula_observador, nombre_responsable, fk_tareas, fk_cedula  FROM observacion") 
    tareas = cursor.fetchall()
    conexion.close()

    # Limpia la tabla existente, si la hay
    for fila in tabla.get_children():
        tabla.delete(fila)

    # Agregar las tareas a la tabla
    for tarea in tareas:
        tabla.insert("", "end", values=tarea)

ventana = Tk()
ventana.title("Observaciones o Incidencias")
#--------------------------------------------------------------------------------------------------------------


# Proporciones de la ventana
#--------------------------------------------------------------------------------------------------------------
ancho_ventana = 1200
alto_ventana = 720
ventana.geometry(f"{ancho_ventana}x{alto_ventana}")
ventana.config(bg="#002D64")
ventana.resizable(0,0)
#--------------------------------------------------------------------------------------------------------------


#funcion para centrar la interfaz grafica
#--------------------------------------------------------------------------------------------------------------
def center_window(window, width, height):
    # Obtén el ancho y alto de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcula las coordenadas para centrar la ventana
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Establece las coordenadas de la ventana
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(ventana,ancho_ventana, alto_ventana)
#--------------------------------------------------------------------------------------------------------------


# Crear un Treeview
#--------------------------------------------------------------------------------------------------------------
tabla = ttk.Treeview(ventana, columns=("N° Observacion", "Observador", "Cedula Observador", "Nombre Responsable", "N° tarea","N° Cedula"))

# Definir las columnas
tabla.heading("#1", text="N° Observacion")
tabla.heading("#2", text="Observador")
tabla.heading("#3", text="Cedula Observador")
tabla.heading("#4", text="Nombre Responsable")
tabla.heading("#5", text="N° tarea")
tabla.heading("#6", text="N° Cedula")


# Ajustar el ancho de las columnas
tabla.column("#0", width=0, stretch=NO)
tabla.column("#1", width=60)  # Número de Tarea
tabla.column("#2", width=100)  # Nombre de Tarea (más pequeño)
tabla.column("#3", width=100)  # Responsable
tabla.column("#4", width=100)  # Cédula del Responsable (más pequeño)
tabla.column("#5", width=100)
tabla.column("#6", width=100)

tabla.place(x=0,y=0,width=1200)
tabla.configure(height=13)
#--------------------------------------------------------------------------------------------------------------


# Botón para obtener las tareas de la base de datos y mostrarlas en la tabla
#--------------------------------------------------------------------------------------------------------------
listar_tabla = ttk.Button(ventana, text="Listar Tabla", cursor="hand2" ,command=Listar_tabla)
listar_tabla.place(x=0,y=600)

regresar_b = ttk.Button(ventana, text="Regresar", cursor="hand2",command=regresar)
regresar_b.place(x=100,y=600)

buscar = ttk.Button(ventana, text="buscar tarea", cursor="hand2",command=filtro)
buscar.place(x=200,y=600)

actualizar = ttk.Button(ventana, text="Actualizar Tarea", cursor="hand2",command=modificar)
actualizar.place(x=420,y=600)

limpiar = ttk.Button(ventana, text="Limpiar Campos", cursor="hand2",command=prueba)
limpiar.place(x=300,y=600)




tabla.bind("<<TreeviewSelect>>", capturar_numero_tarea)
#--------------------------------------------------------------------------------------------------------------


#labels
#--------------------------------------------------------------------------------------------------------------
cod_observacion_label = Label(ventana,text="Numero Tarea")
cod_tareas_label = Label(ventana,text="Nombre Tarea")
Responsable_label = Label(ventana,text="Responsable")
cedula_label = Label(ventana,text="Cedula")
descripcion_label = Label(ventana,text="Estatus")

#--------------------------------------------------------------------------------------------------------------


#configuracion labels
#--------------------------------------------------------------------------------------------------------------
cod_observacion_label.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13)) #numero tarea
cod_observacion_label.place(x=0,y=300)

cod_tareas_label.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
cod_tareas_label.place(x=150,y=300)

Responsable_label.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
Responsable_label.place(x=0,y=380)

cedula_label.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
cedula_label.place(x=180,y=380)

descripcion_label.config(fg="white",bg="#002D64",font=("Roboto condensed Light", 13))
descripcion_label.place(x=19,y=450)

#--------------------------------------------------------------------------------------------------------------


#campos de texto
#--------------------------------------------------------------------------------------------------------------
cod_observacion_txt = Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

cod_tareas_txt= Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))

Responsable_txt= Entry(ventana,width=12,justify="center",font=("Roboto condensed Light", 13))

cedula_txt = Entry(ventana,width=20,justify="center",font=("Roboto condensed Light", 13))




#--------------------------------------------------------------------------------------------------------------


# Conficuracion de campos de texto
#--------------------------------------------------------------------------------------------------------------
cod_observacion_txt.place(x=0,y=325)

cod_tareas_txt.place(x=118,y=325)

Responsable_txt.place(x=0,y=405)

cedula_txt.place(x=119,y=405)


#--------------------------------------------------------------------------------------------------------------



# textos de area

descripcion = Text(ventana,width=50,height=10)
descripcion.place(x=300,y=323)
scrollbar = Scrollbar(ventana, command=descripcion.yview)  #scroll
scrollbar.place(x=710,y=328,height=150) 
descripcion.config(yscrollcommand=scrollbar.set)





ventana.mainloop()
