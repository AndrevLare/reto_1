# Defino una función que retorne un float (el resultado)
def main() -> float:
    # Asigna a x, y & operador segun el input del usuario
    x, y, operator = input("ingrese dos numeros y la operacion deseada (*) (/) (+) (-) (**) (//)").split()
    x = int(x)
    y = int(y)
    
    # Defino la variable q contiene al output
    output: float
    
    # Segun el operador usado, opera x & y, luego lo añade a output y lo retorna
    match operator:
        case "*":
            output = x * y
        case "/":
            output = x / y
        case "+":
            output = x + y
        case "-":
            output = x - y
        case "//":
            output = x // y
        case "**":
            output = x ** y
        case "_":
            return "operacion no valida"
    return output
            
# Entrada del Programa que llama a main e imprime su resultado
if __name__ == "__main__":
    print(main())