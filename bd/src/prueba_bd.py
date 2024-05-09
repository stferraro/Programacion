import psycopg2

conexion = psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        )


#conexion sencilla
try :
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM persona')
    for persona in cursor.fetchall():
        print(persona)

except Exception as e:
    print(e)

finally:
    cursor.close()
    conexion.close()
    
#conexion con with
try:
    with psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        ) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM persona')
            for persona in cursor.fetchall():
                print(persona)

except Exception as e:
    print(e)
finally:
    conn.close()