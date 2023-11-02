import psycopg2

def conectar_a_base_de_datos():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="CalidadSoftware",
            user="postgres",
            password="root"
            
        )
        return conexion
    except psycopg2.Error as error:
        print(f"error al intentar conectarse a la abse de datos {error}")
        return None