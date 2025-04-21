def main():
    lista = list(map(int, input("ingrese una lista de numeros enteros\n").split()))
    sumas = []
    for i , e in enumerate(lista):
        if i == 0: continue
        sumas.append(e + lista[i-1])
    
    print(max(sumas))
    
if __name__ == "__main__":
    main()