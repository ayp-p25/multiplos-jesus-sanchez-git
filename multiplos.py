A = float(input(" Ingrese un numero : \n"))
B = float(input(" Ingrese un segundo numero : \n"))
if A== 0 or B == 0:
    print("El numero ",A, "no es multiplo de ", B)
elif (A % B) ==0 or ( B % A)== 0:
    print("El numero ",A, "es multiplo de ", B)
else:
    print("El numero ",A, "no es multiplo de ", B)
