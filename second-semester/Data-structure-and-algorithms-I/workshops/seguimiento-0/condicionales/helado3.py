temperatura_actual = int(input())
edad = int(input())

if temperatura_actual > 27 and edad >= 18:
    dinero = int(input())
    if dinero > 5:
        print("Comprar helado cerveza")
    else:
        print("Lo sentimos estas pobre")
else:
    print("Lo sentimos juventud")