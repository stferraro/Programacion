import psycopg2

conexion = psycopg2.connect(user = 'gerardo', 
                            password = 'desarrollo', 
                            host = 'localhost', 
                            port = '5432', 
                            database = 'pruebadb'
                        )

try :
    with conexion:
        with conexion.cursor() as cursor:
            sentence = 'UPDATE persona SET email = %s WHERE cedula = %s'
            cedula = input("ingrese la cedula: ")
            email = input("ingrese el nuevo email: ")
            values = (email, cedula)
            cursor.execute(sentence, values)
            sentence2 = 'select * from persona'
            cursor.execute(sentence2)
            registers = cursor.fetchall()
            for r in registers:
                print(r)
except Exception as e:
    print(e)
finally:
    conexion.close()