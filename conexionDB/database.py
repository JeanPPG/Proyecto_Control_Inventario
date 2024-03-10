import psycopg2

def connect_to_database():
    # Datos de conexión a la base de datos
    database_info = {
        "database": "control_inventario",
        "user": "postgres",
        "password": "admin27",
        "host": "localhost",
        "port": "5432"
    }

    # Intentar establecer la conexión
    try:
        connection = psycopg2.connect(**database_info)
        return connection
    except psycopg2.Error as e:
        print("Error al conectar a PostgreSQL:", e)
        return None
