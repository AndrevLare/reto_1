def main()->list:
    list = input("ingrese la lista de numeros separados por comas\n").split(",")
    
    output = []
    
    for e in list:
        prime = True
        for i in range(2, (int(e)//2)+1):
            prime = prime and int(e)%int(i) != 0
            if not(prime): break
        if (prime or int(e) == 2) and (int(e) > 1): output.append(e)
    
    return output
        
if __name__ == "__main__":
    print(main())