from tkinter import *
from subprocess import call


raiz = Tk()
raiz.title("Inicio de sesion")
raiz.geometry("900x550")
raiz.resizable(0,0)
raiz.config(bg="orange")

frame_1 = Frame(raiz, width=900, height=500)
# opciones para expandir el frame en toda la raiz          #side="left", anchor="n"

#frame
frame_1.pack(fill="both", expand="true")        #colocar el frame dentro de la raiz



#color del frame
frame_1.config(bg="#002D64")


#Imagenes
imagen_1=PhotoImage(file="piton.png")
imagen_2=PhotoImage(file="avatar.png")
imagen_3=PhotoImage(file="candado.png")

#labels

Label_1= Label(frame_1,text="Usuario")      #texto
label_2 = Label(frame_1,image=imagen_1)     #imagen
label_3 = Label(frame_1,text="Contraseña")  #texto
label_4 = Label(frame_1,image=imagen_2)     #imagen
label_5 = Label(frame_1,image=imagen_3)     #imagen

#cuadros de texto
            
usuario_txt =Entry(frame_1,width=30,justify="center",font=("Roboto condensed Light", 13))
contraseña_txt=Entry(frame_1,width=30,justify="center",font=("Roboto condensed Light", 13),show="*")



#configuracion de labels
Label_1.config(bg="#002D64", font=("Roboto condensed",15),fg="White")  #usuario
Label_1.place(x=420, y=295)

label_3.config(bg="#002D64",font=("Roboto condensed",15), fg="White") #contraseña
label_3.place(x=404,y=380)


#Imagen
label_2.config(bg="#002D64")    #imagen de fondo
label_2.place(x=325,y=20)

label_4.config(bg="#002D64")    #imagen de usuario
label_4.place(x=250,y=288)

label_5.config(bg="#002D64")   #imagen de candado
label_5.place(x=250,y=375)



#configuracion de campos de texto


usuario_txt.place(x=332,y=324,height=27) #usuario


contraseña_txt.place(x=332,y=410,height=27) #contraseña

#Funcion para registrarme
def abrir_registro():
    # Cierra la ventana actual
    raiz.destroy()
    
    # Abre el archivo registro.py en una nueva ventana
    call(["python", "Registro_jefe.py"])

#botones

#boton iniciar sesion
Boton_IniciarSesion= Button(frame_1,width=25,font=("Roboto condensed", 13),text=("Iniciar sesion"))
Boton_IniciarSesion.place(x=353,y=448,height=33)
Boton_IniciarSesion.config(bg="#FFDE59",cursor="hand2")

#boton registrarme
Boton_Registrarme= Button(frame_1,width=25,font=("Roboto condensed", 13),text=("Registrarme"))
Boton_Registrarme.place(x=353,y=485,height=33)
Boton_Registrarme.config(bg="#FFDE59",cursor="hand2", command=abrir_registro)

raiz.mainloop()     

