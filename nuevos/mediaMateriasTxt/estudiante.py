from materia import Materia


class estudiante:
    
    def __init__(self, codigo,cedula, nombre, apellido, materias):
        self._codigo = codigo
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._materias = materias

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def materias(self):
        return self._materias

    @materias.setter
    def materias(self, value):
        self._materias = value
        
    def add_materias(self, materia):
        self._materias.append(materia)
        
    def promedio_ponderado(self):
        total = 0
        for materia in self._materias:
            total += materia.valor_para_promedio()
        return total / sum(materia.credito for materia in self._materias)
        
    def __str__(self):
        materias_str = "\n".join([str(materia) for materia in self._materias])
        estudiante_str = f"Codigo: {self._codigo}, Cedula: {self._cedula}, Nombre: {self._nombre}, Apellido: {self._apellido}"
        str1 = ''.center(50, '*')
        total = self.promedio_ponderado()
        valor_final = ''.join([estudiante_str, "\n", str1, "\n", materias_str, "\n", "Promedio: " , "\t\t\t\t\t\t", str(round(total, 2))])
        return valor_final
    
    def crea_txt(self):
        with open('/home/gerardo/desarrollo/Programacion/nuevos/filesTxt/estudiante.txt', 'w') as f:
            try:
                f.write(self.__str__())
            except FileNotFoundError:
                print('No se encontro el archivo')

        
estudiante = estudiante('111', '111', 'Gerardo', 'Gonzales', [])
materia = Materia('111', 'Matematica', 20, 5)
materia1 = Materia('222', 'Fisica', 18, 3)
materia2 = Materia('333', 'Quimica', 19, 4)
materia3 = Materia('444', 'Biologia', 15, 5)
materia4 = Materia('555', 'Ingles', 20, 5)

estudiante.add_materias(materia)
estudiante.add_materias(materia1)
estudiante.add_materias(materia2)
estudiante.add_materias(materia3)
estudiante.add_materias(materia4)

print(estudiante.promedio_ponderado())
print(estudiante)
estudiante.crea_txt()