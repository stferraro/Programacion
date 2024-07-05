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
            sentence = 'DELETE FROM persona WHERE cedula = %s'
            cedula = input("ingrese la cedula: ")
            values = (cedula,)
            cursor.execute(sentence, values)
            registers = cursor.rowcount
            if registers != 0:
                print(f'los registros eliminados son: {registers}')
                sentence2 = 'select * from persona'
                cursor.execute(sentence2)
                registers2 = cursor.fetchall()
                for r in registers2:
                    print(r)
            else:
                print('la cedula indicada no existe en la base de datos')

except Exception as e:
    print(e)
finally:
    conexion.close()