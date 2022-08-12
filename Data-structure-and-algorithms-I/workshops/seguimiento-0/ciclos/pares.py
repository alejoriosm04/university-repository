num = int(input())

for i in range(0, num+1):
    i = i + 2
    if i <= num and i%2==0:
        print(i)