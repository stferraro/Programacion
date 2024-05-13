from psycopg2 import connect
from psycopg2 import OperationalError

class Connection:
    
    def __init__(self):
        try:
            with open('resource/.env', 'r') as f:
                data = f.readlines()
                for line in data:
                    if line.startswith('DB_HOST'):
                        host = line.split('=')[1].strip()
                    elif line.startswith('DB_PORT'):
                        port = line.split('=')[1].strip()
                    elif line.startswith('DB_NAME'):
                        dbname = line.split('=')[1].strip()
                    elif line.startswith('DB_USER'):
                        user = line.split('=')[1].strip()
                    elif line.startswith('DB_PASSWORD'):
                        password = line.split('=')[1].strip()
            self.conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
            print('Conexión exitosa')
        except OperationalError as e:
            print(e)
            print('Conexión fallida')
            
            
    def write(self, data):
        with self.conn.cursor() as cur:
            sentence = """INSERT INTO estudiantes (nombres, apellidos, cedula, email, telefono) VALUES (%(nombres)s, %(apellidos)s, %(cedula)s, %(email)s, %(telefono)s)"""
            cur.execute(sentence, data) 
        self.conn.commit()
        
    def read_all(self):
        with self.conn.cursor() as cur:
            sentence = """SELECT * FROM estudiantes"""
            cur.execute(sentence)
            return cur.fetchall()
        
    def read_by_id(self, id):
        with self.conn.cursor() as cur:
            sentence = """SELECT * FROM estudiantes WHERE id = %(id)s"""
            cur.execute(sentence, {'id': id})
            return cur.fetchone()
        
    def delete(self, id):
        with self.conn.cursor() as cur:
            sentence = """DELETE FROM estudiantes WHERE id = %(id)s"""
            cur.execute(sentence, {'id': id})
        self.conn.commit()
        
    def update(self, data):
        with self.conn.cursor() as cur:
            sentence = """UPDATE estudiantes SET nombres = %(nombres)s, apellidos = %(apellidos)s, cedula = %(cedula)s, email = %(email)s, telefono = %(telefono)s WHERE id = %(id)s"""
            cur.execute(sentence, data)
        self.conn.commit()
        
                         
    def __def__(self):
        self.conn.close() #destructor
        
        