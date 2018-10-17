# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest

# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    new = formula[:] #Crea una lista copia de formula, donde se iran eliminando literales
    for i in formula: #Recorre el arreglo
        nuevo_i = list(i)
        for j in nuevo_i:
            if j == lit: #Si el literal esta en el arreglo, elimina toda su oracion
                new.remove(i)
            elif j == -1 * lit: #Si esta la negacion del literal, elimina ese literal
                i.remove(j)
    return new #Retorna la nueva lista


def IsSatisfiable(formula):
    if formula == []: #Si la formula es vacia Retorna True
        return True
    elif [] in formula: #Si la formula contiene un literal vacio, ie. Falso, retorna False
        return False
    else:
        elemento = formula[0][0] #Toma el primer elemento que pilla
        lit = elemento
        nuevo = SetLiteral(formula, lit) #Setea el valor a True y simplifica
        if nuevo == []: #Si la simplificacion es vacia, retorna True
            return True
        elif [] in nuevo: #Si hay un literal vacio en la nueva formula
            return IsSatisfiable(SetLiteral(formula,-lit)) #Retorna el caso recursivo seteando el litelar a falso
        else: #Retorna la recursividad sobre la nueva formula
            return IsSatisfiable(nuevo)


def BuildModel(formula):
    dic = {} 
    sat = IsSatisfiable(formula)
    if sat == False: #Si la formula no es SAT
        return (sat,dic) #Retorna False y un diccionario vacio
    else: #Si la formula es SAT
        literales = [] #Crea una LISTA 
        while len(formula) >= 1:
            lit = formula[0][0]
            if IsSatisfiable(SetLiteral(formula,lit)): #Ve si es SAT la simplificacion con el lit elegido
                literales.append([lit,True]) #Guarda una tupla con el valor del literal y su valuacion
                formula = SetLiteral(formula,lit) #Luego actualiza la formula
            else: #Analogo a lo anterior, pero con la negacion del literal 
                literales.append([-lit,True])
                formula = SetLiteral(formula,-lit)
        for i in literales: #Recorre la lista de tuplas
            if i[0] < 0: #Si el literal es negativo
                i[0] = abs(i[0]) #Cambia el signo del literal 
                i[1] = not i[1] #Cambia la valuacion 
        literales.sort() #Ordena los literales
        for i in literales: 
            dic[i[0]] = i[1] #Pasa la lista a un diccionario
        return (sat, dic) #Retorna el Booleano y el diccionario


class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_SetLiteral(self):
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], 1), [[-2, 4], [3, 4]])
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], -1), [[2, -3], [3, 4]])

    def test_IsSatisfiable(self):
        self.assertEqual(IsSatisfiable([[1, 2, -3], [-1, -2, 4], [3, 4]]), True)
        self.assertEqual(IsSatisfiable([[1, 2], [1, -2], [], [-1]]), False)
        self.assertEqual(IsSatisfiable([]), True)

    def test_BuildModel(self):
        self.assertEqual(BuildModel([[-2, 4], [1], [-4,-1]]), (True, {1: True, 2: False, 4: False}))
        self.assertEqual(BuildModel([[1,2], [-1,-2], [-1,2], [1,-2]]), (False, {}))

# Perform the tests when runing the file
if __name__ == '__main__':
    unittest.main()
