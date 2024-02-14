def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

def main():
    opcion = input("Selecciona una operación (+, -, *, /): ")

    if opcion not in ['+', '-', '*', '/']:
        print("Operación no válida.")
        return

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '+':
        print("El resultado de la suma es:", sumar(num1, num2))
    elif opcion == '-':
        print("El resultado de la resta es:", restar(num1, num2))
    elif opcion == '*':
        print("El resultado de la multiplicación es:", multiplicar(num1, num2))
    elif opcion == '/':
        print("El resultado de la división es:", dividir(num1, num2))

if __name__ == "__main__":
    main()
