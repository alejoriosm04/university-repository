import disassembler

def main():
    x = 1 / 3
    y = x + 5
    z = x + y * 10
    print(z)
    print(y+5)

disassembler.disassemble(main)