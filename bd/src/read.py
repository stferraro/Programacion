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

print(''.center(50, "*"))
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
    
print(''.center(50, "*"))
    
#retornar un solo registro
try:
    with psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        ) as conn:
        with conn.cursor() as cursor:
            sentence = ('SELECT * FROM persona WHERE cedula = %s')
            cedula = 'V-15693289'
            cursor.execute(sentence, (cedula,))
            persona = cursor.fetchone()
            print(persona)
except Exception as e:
    print(e)
finally:
    conn.close()
    
print(''.center(50, "*"))
    
try:
    with psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        ) as conn:
        with conn.cursor() as cursor:
            sentence = ('SELECT * FROM persona WHERE cedula in %s')
            cedula1 = 'V-15693289'
            cedula2 = 'V-23456789'
            cedulas = ((cedula1, cedula2),)
            cursor.execute(sentence, (cedulas))
            personas = cursor.fetchall()
            for persona in personas:
                print(persona)
except Exception as e:
    print(e)
finally:
    conexion.close()
    
print(''.center(50, "*"))

try :
    with psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        ) as conn:
        with conn.cursor() as cursor:
            sentence = ('SELECT * FROM persona WHERE cedula IN %s')
            cedula1 = input("Ingrese la cedula: ")
            cedula2 = input("Ingrese la cedula: ")
            cedulas = (tuple([cedula1, cedula2]),)
            cursor.execute(sentence, (cedulas))
            persona = cursor.fetchall()
            for p in persona:
                print(p)
except Exception as e:
    print(e)
finally:
    conn.close()
            