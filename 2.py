def main(str:str)->bool:
    palindrome = True
    for i, chr in enumerate(str):
        evaluation_case = chr == str[-i-1]
        palindrome = palindrome and evaluation_case
    return palindrome

if __name__ == "__main__":
    string = input()
    print(string, "es un palindromo" if main(string) else "no es un palindromo")