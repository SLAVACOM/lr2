print('           (        1        )')
print('6. y(x)=SUM(----------------,),  |x|>=1 ')
print('           ( (2n+1)*x^(2n+1) )')
x = float(input("Введите x: "))

while (abs(x) <= 1):
    print('Нарушено условие! Введите x заново')
    x = float(input("Введите x: "))
summ = 1 / x

k = 1
element_posleovatelnosti = 1 / x
while True:
    element_posleovatelnosti = element_posleovatelnosti * k / ((k + 2) * x * x)
    summ += element_posleovatelnosti
    if element_posleovatelnosti < 0.000_001:
        break
    k += 2
print(f"Сумма: {summ} ")
