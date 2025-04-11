def main() -> float:
    x, y, operator = input("ingrese dos numeros y la operacion deseada (*) (/) (+) (-) (**) (//)").split()
    x = int(x)
    y = int(y)
    output: float
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
            

if __name__ == "__main__":
    print(main())