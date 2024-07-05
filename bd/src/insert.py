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

            sentence = 'INSERT INTO persona(cedula, nombre, apellido, email) VALUES(%s, %s, %s, %s)'
            values = ('V-1234536789', 'Gerardo', 'Villa', 'gvv@gmail.com')
            values = ('V-113456723', 'Pedro', 'ddddd', 'pdd@gmail.com')
            cursor.execute(sentence, values)
            #conexion.commit()
            register = cursor.rowcount
            print(f'los registros insertados son: {register}')
            sentence2 = 'select * from persona'
            cursor.execute(sentence2)
            registers = cursor.fetchall()
            for r in registers:
                print(r)
except Exception as e:
    print(e)
finally:
    conexion.close()
        
        