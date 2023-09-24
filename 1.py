print('           (        1        )')
print('6. y(x)=SUM(----------------,),  |x|>=1 ')
print('           ( (2n+1)*x^(2n+1) )')
x=int(input('Введите число x: '))
while (abs(x) <= 1):
    print('Нарушено условие! Введите число x заново')
    x = int(input('Введите число x: '))
finish = int(input('Введите число n: '))
summ = 1/x
N = 1
if finish > 1:
    while finish > N:
        summ += (1 / ((2 * N + 1) * x ** (2 * N + 1)))
        N += 1
print(f"Сумма: {summ}")