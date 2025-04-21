from collections import Counter
def main():
    lista = input("ingrese una lista de palabras\n").split()
    resultado = set()
    
    for i, str in enumerate(lista):
        caracteres = []
        
        for chr in str: caracteres.append(chr)
        
        for j, str_j in enumerate(lista):
            if i == j: continue
            caracteres_2 = []
            
            for chr in str_j: caracteres_2.append(chr)
            
            if Counter(caracteres) == Counter(caracteres_2): resultado.update([str, str_j])
            
    print(list(resultado))
    
main()