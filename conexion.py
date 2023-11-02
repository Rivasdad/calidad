import mysql.connector

def conectar_a_base_de_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prueba"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error en la conexión a la base de datos: {error}")
        return None