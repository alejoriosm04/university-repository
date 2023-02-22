zapatos = int(input())

if zapatos >= 50 and zapatos <= 100:
    print(45)
elif zapatos > 100:
    print(150)
elif zapatos < 50:
    print(0)
else:
    print("sin incentivo")