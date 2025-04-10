def main() -> float:
    x, y, operator = input().split()
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
    return output
            

if __name__ == "__main__":
    print(main())