# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print("Cómo te llamas")
	nom = input()
	print("Ingresa el numero de notas a calcular")
	n = float(input())
	acum = 0
	for i in range(1,n+1):
		print("ingresa el dato ",i,":")
		dato = float(input())
		acum = acum+dato
	prom = acum/n
	print("El promedio de ",nom,"es de: ",prom)

