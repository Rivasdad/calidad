from tkinter import *
from tkinter import messagebox 
from conexion import conectar_a_base_de_datos
from subprocess import call
from tkinter import ttk
import psycopg2
raiz = Tk()
raiz.title("Registro")
raiz.geometry("900x550")
raiz.resizable(0,0)
raiz.config(bg="orange")


frame_1 = Frame(raiz, width=900, height=500)
frame_1.pack(fill="both", expand="true")  
frame_1.config(bg="#002D64")

frame_2= Frame(frame_1,width=540,height=550)

frame_2.pack(side="left")
frame_2.config(bg="#012269")


#Funciones


#Funcion para registrarme
def regresar():
    # Cierra la ventana actual
    raiz.destroy()
    
    # Abre el archivo registro.py en una nueva ventana
    call(["python", "Inicio.py"])
#-------------------------------------------------------------------------------------------------------
def entrar_registrar(event):
    registrar.config(bg="#B0E0E6")
    
def salir_registrar(event):
    registrar.config(bg="#87CEEB")
#-------------------------------------------------------------------------------------------------------
def entrar_limpiar(event):
    limpiar.config(bg="#B0E0E6")

def salir_limpiar(event):
    limpiar.config(bg="#87CEEB")
 #-------------------------------------------------------------------------------------------------------
def entrar_regresar(event):
    Regresar.config(bg="#B0E0E6")
    
def salir_regresar(event):
    Regresar.config(bg="#87CEEB")   

def validar_campos():
 #-------------------------------------------------------------------------------------------------------  
    # Obtener el contenido del campo "usuario"
    nombre = nombre_txt.get()
    ci = cedula_txt.get()
    departamento = combo_departamento.get()
    area = combo_area.get()
    cargo = combo_cargo.get()
    usuario = usuario_txt.get()
    contra = contraseña_txt.get()
    correo = correo_txt.get()
    
    # Verificar si el campo está vacío     
    if nombre== "" or ci =="" or departamento =="" or area=="" or cargo=="" or usuario=="" or contra=="" or correo=="":
        print("Campos vacios!")
    #verificar si en el campo solo hay numeros  
   # elif not re.match("^[A-Za-zñÑ\s]*$", nombre):
        #messagebox.showwarning("Nombre y apellido invalido", "Por favor, Solo ingresa letras para tu nombre")
#-------------------------------------------------------------------------------------------------------
    #elif not ci.isdigit():  #cedula
        #messagebox.showwarning("cedula invlida", "Por favor, ingresa una cedula valida")
#------------------------------------------------------------------------------------------------------- 
    #elif not re.match("^[A-Za-zñÑ\s]*$",departamento):
       # messagebox.showwarning("Nombre de departamento invalido", "Por favor, Solo ingresa letras para tu departamento")
#-------------------------------------------------------------------------------------------------------
    #elif not re.match("^[A-Za-zñÑ\s]*$",area):
        #messagebox.showwarning("Nombre de area invalido", "Por favor, Solo ingresa letras para tu area")
#-------------------------------------------------------------------------------------------------------
    #elif not re.match("^[A-Za-zñÑ\s]*$",cargo):
       # messagebox.showwarning("Nombre de cargo invalido", "Por favor, Solo ingresa letras para tu Cargo")
#-------------------------------------------------------------------------------------------------------
    #elif not re.match ("^[A-Za-zñÑ\s-]*$",usuario):
       # print("el usuario no comprende con los parametros")
#-------------------------------------------------------------------------------------------------------
    else:   #toda la validacion correcta
        def registrar():
         print("")
        try:
            conexion = conectar_a_base_de_datos()
            if conexion:
                 cursor = conexion.cursor()  
            if cargo == "Gerente":
                rol = "Gerente"   
            else:
                rol = "trabajador"                                                                                                      
            sql ="insert into usuario (usuario, contraseña, cedula, nombre, departamento, area, cargo, correo, rol) values('"+usuario+"','"+contra+"','"+ci+"','"+nombre+"','"+departamento+"','"+area+"','"+cargo+"', '"+correo+"', '"+rol+"' )"
            cursor.execute(sql)
            conexion.commit()
            cursor.close()
            conexion.close()
            messagebox.showwarning("Usuario Registrado", "Usuario Registrado Correctamente")
        except (Exception, psycopg2.DatabaseError) as error:
            messagebox.showwarning("Error", "Error al intentar registrar usuario") 
#------------------------------------------------------------------------------------------------------- 
def borrar_texto():
    nombre_txt.delete(0, 'end') 
    cedula_txt.delete(0, 'end')
    
    usuario_txt.delete(0, 'end')
    contraseña_txt.delete(0, 'end')
    correo_txt.delete(0, 'end')
#-------------------------------------------------------------------------------------------------------
#imagenes
imagen_1=PhotoImage(file="registro_im.png")
imagen_2 = PhotoImage(file ="logo.png")

#-----------------------------------------------------------------------------------------------------
# #labels

label_1=Label(frame_1,image=imagen_1)              #imagen a la derecha colocado
label_10 =Label(frame_2,image=imagen_2)
#-------------------------------------------------------------------------------------------------------
label_2=Label(frame_1,text="Nombre y Apellido")    #nombre y apellido   colocado
label_3 =Label(frame_2,text="Cedula")               #cedula              colocado
label_4=Label(frame_2,text="Departamento")          #departamento       colocado
label_5= Label(frame_2,text="Area")                 #area del departamento  colocado
label_6 =Label(frame_2,text="Cargo")                #cargo                     colcoado
label_7 =Label(frame_2,text="Usuario")              #usuario      colcoado          
label_8= Label(frame_2,text="Contraseña")           #contraseña         colcoado
label_9= Label(frame_2,text="Correo")               #correo electronico
Titulo = Label(frame_2,text="Calidad de Software")  #calidad de software
                #advertencia ante un texto no valido

#caja de texto
nombre_txt =Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
cedula_txt = Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
# departamento_txt =Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
# area_txt= Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
#cargo_txt= Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
usuario_txt= Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
contraseña_txt= Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
correo_txt= Entry(frame_2,width=22,justify="center",font=("Roboto condensed Light", 13))
#-------------------------------------------------------------------------------------------------------

#Botones

registrar = Button(frame_2,width=32,font=("Roboto condensed", 13),text=("Registrarme"),command=validar_campos)
registrar.place(x=5,y=320,height=31)
registrar.config(bg="#87CEEB",cursor="hand2")
#-------------------------------------------------------------------------------------------------------
limpiar = Button(frame_2,width=30,font=("Roboto condensed", 13),text=("Limpiar Campos"),command=borrar_texto)
limpiar.place(x=279,y=320,height=31)
limpiar.config(bg="#87CEEB",cursor="hand2")
#-------------------------------------------------------------------------------------------------------
Regresar= Button(frame_2,width=20,font=("Roboto condensed", 13),text=("Regresar"))
Regresar.place(x=170,y=518,height=33)
Regresar.config(bg="#87CEEB",cursor="hand2", command=regresar)

#configuracion de botones

registrar.bind("<Enter>", entrar_registrar)  
registrar.bind("<Leave>", salir_registrar) 

limpiar.bind("<Enter>", entrar_limpiar)  
limpiar.bind("<Leave>", salir_limpiar)

Regresar.bind("<Enter>", entrar_regresar)  
Regresar.bind("<Leave>", salir_regresar) 

#-------------------------------------------------------------------------------------------------------
 #configuracion de labels

Titulo.config(bg="#012269", font=("Roboto condensed",15),fg="White")
Titulo.place(x=370,y=520)



label_1.config(bg="#002D64")    #imagen de fondo
label_1.place(x=535,y=0)

label_10.config(bg="#012269")    #imagen de fondo
label_10.place(x=10,y=380)
#-------------------------------------------------------------------------------------------------------
label_2.config(bg="#012269", font=("Roboto condensed",15),fg="White")  #Nombre y apellido
label_2.place(x=59, y=10)

label_3.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #cedula
label_3.place(x=375, y=10)
#-------------------------------------------------------------------------------------------------------
label_4.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #departamento
label_4.place(x=78,y=85)

label_5.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #area
label_5.place(x=385,y=85)
#-------------------------------------------------------------------------------------------------------
label_6.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #cargo
label_6.place(x=109,y=160)

label_7.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #usuario
label_7.place(x=376,y=160)
#-------------------------------------------------------------------------------------------------------
label_8.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #contraseña
label_8.place(x=88,y=235)

label_9.config(bg="#012269",font=("Roboto condensed",15),fg="White")    #correo electronico
label_9.place(x=376,y=235)

#configuracion de caja de texto
nombre_txt.place(x=45,y=42,height=24)                                  #Nombre y apellido
cedula_txt.place(x=315,y=42,height=24)                                 #cedula
#-------------------------------------------------------------------------------------------------------
                                   #area
#-------------------------------------------------------------------------------------------------------
                                #cargo
usuario_txt.place(x=315,y=192,height=24)                                #usuario 
#-------------------------------------------------------------------------------------------------------
contraseña_txt.place(x=45,y=267,height=24)                                 #contraseña
correo_txt.place(x=315,y=267,height=24)                             #correo


# combo box
# ComboBox para el departamkento
combo_departamento = ttk.Combobox(frame_2, values="Tecnologia",justify="center")
combo_departamento.set("")
combo_departamento.place(x=48,y=120,width=180,height=25)

# ComboBox para el area
combo_area = ttk.Combobox(frame_2, values=["Calidad de Software"],justify="center")
combo_area.set("")
combo_area.place(x=315,y=120,width=180,height=25)

# ComboBox para el cargo
combo_cargo = ttk.Combobox(frame_2, values=["Gerente","Contratado","Farservice","Becario","ince"],justify="center")
combo_cargo.set("")
combo_cargo.place(x=48,y=195,width=180,height=25)
raiz.mainloop()
