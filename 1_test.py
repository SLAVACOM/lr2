x = num = float(input("Введите x: "))
k = 1
while True:
    print(k,num)
    k+=2
    num=x*x*num
    if 1/(k*num)<0.000000001:
        break