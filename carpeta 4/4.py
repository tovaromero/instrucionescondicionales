# programa que calcula el indice de masa corporal "IMC" de una persona por medio de su estatura 

# input

peso = int(input("ingrese su peso actual: "))
estatura = float(input("ingrese su estatura actual: "))

# processing 

IMC = peso/estatura**2
 
if IMC < 16 :
    resultado = " criterio de ingreso en hospital "
elif IMC <= 17:
    resultado = " infrapeso"
elif IMC <= 18.5:
    resultado = "bajo peso"
elif IMC <= 25:
        resultado = "peso normal (saludable)"
elif IMC <= 30:
            resultado = "sobrepeso (obesidad de grado 1)"

elif IMC <= 35:
    resultado = " sobrepeso cronico (obesidad de grado 2) "
elif IMC <= 40:
    resultado = " obesida premorbida (obesidad de grado 3) "
elif IMC > 40 :
    resultado = "obesida morbida (obesidad de grado 4) "

# output

print("si IMC es",IMC," y sus resultados son",resultado,)



 