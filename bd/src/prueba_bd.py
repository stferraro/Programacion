import psycopg2

conexion = psycopg2.connect(
    user = 'gerardo',
    password = 'desarrollo',
    host = '127.0.0.1',
    port = '5432',
    database = 'pruebadb'
)

cursor = conexion.cursor()
sentencia = 'select * from persona;'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)
cursor.close()
conexion.close()

