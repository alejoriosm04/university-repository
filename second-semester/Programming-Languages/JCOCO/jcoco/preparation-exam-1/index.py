import disassembler

def main():
    tope = int(input("Ingrese la cantidad de numeros: "))
    total = 1
    for i in range(tope):
        n = int(input())
        total = total * n
        print(total)

disassembler.disassemble(main)