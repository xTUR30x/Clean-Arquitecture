#KISS Principle Example

#Problem

def main() -> None:
    number = int(input("Ingrese un valor: "))

    if number < 0:
        print("Solo se puede calcular el factorial de numeros positivos")
    else:
        factorial = calculateFactorial(number)
        print(f"El factorial de { number } es { factorial }")


def calculateFactorial(number: int) -> int:
    factorial = 1

    if number == 0:
        return 1
    
    for i in range(1, number + 1):
        if i % 2 == 0:
            factorial *= i
        else:
            factorial *= i
    
    return factorial



if __name__ == '__main__':
    main()


#Solution

def main() -> None:
    number = int(input("Ingrese un valor: "))

    if number < 0:
        print("Solo se puede calcular el factorial de numeros positivos")
    else:
        factorial = calculateFactorial(number)
        print(f"El factorial de { number } es { factorial }")


def calculateFactorial(number: int) -> int:
    factorial = 1
    
    if number != 0:
        for i in range(1, number + 1):
            factorial *= i
    
    return factorial



if __name__ == '__main__':
    main()
