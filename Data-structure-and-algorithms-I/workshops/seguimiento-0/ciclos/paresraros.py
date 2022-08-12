num = int(input())

for i in range(2, num+1,2):
    if i <= num and i%2==0 and i != 6 and i != 8:
        print(i)