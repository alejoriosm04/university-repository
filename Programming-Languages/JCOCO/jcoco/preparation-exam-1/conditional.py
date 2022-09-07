import disassembler

def main():
  a = int(input("Ingrese el primer valor: "))
  b = int(input("Ingrese el segundo valor: "))
  if a > b:
    print("a es mayor")
  else:
    print("b es mayor")


disassembler.disassemble(main)