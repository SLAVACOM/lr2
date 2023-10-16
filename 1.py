print('           (        1        )')
print('6. y(x)=SUM(----------------,),  |x|>=1 ')
print('           ( (2n+1)*x^(2n+1) )')
x = num = float(input("Введите x: "))
while (abs(x) <= 1):
    print('Нарушено условие! Введите число x заново')
    x = num = float(input("Введите x: "))
summ = 1/x
k = 1
while True:
    k += 2
    num = x * x * num
    posled = 1/(k*num)
    if posled < 0.000_001:
        break
    summ+=posled
print(f"Сумма: {summ}")