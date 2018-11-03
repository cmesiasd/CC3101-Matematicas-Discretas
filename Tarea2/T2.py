from itertools import product

letras = "asjk"
letras_alf = ["a","jaj","sk",""]

def toString(List): 
    return '\n'.join(List)

def generaTexto(n):
	new = []
	keys = [''.join(i) for i in product(letras, repeat = n)]
	
	dic = [''.join(i) for i in product(letras_alf, repeat = n)]
	for j in keys:
		if j in dic:
			new.append(j)
	print "Se pueden generar en total " + str(len(keys)) + " palabras de largo " + str(n)
	print "Pero solo " + str(len(new)) + " pertencen en el lenguaje"
	return toString(new)

def cantidad_palabras(n):
	recurrencia = [1, 1, 2]
	for i in xrange(3,n+1):
		recurrencia.append(recurrencia[i-1]+recurrencia[i-2]+recurrencia[i-3])
	return recurrencia[n]


print "==============================="
print "PROGRAMA PARA GENERAR PALABRAS"
print "==============================="
n = input("Ingrese n (largo de las palabras): ")
print generaTexto(n)
print "======================================================="
print "PROGRAMA CONTADOR DE PALABRAS PERTENECIENTES AL LENGUJE"
print "======================================================="
m = input("Ingrese n (largo de las palabras): ")
print str(cantidad_palabras(m)) + " palabras de largo " + str(m) + " estan en el lenguaje"