s = input("Введите 6 целых чисел через запятые(х1, x2, x3, x4, x5, x6):\n").split(",")
len_s = len(s)
while len_s != 6:
    print("Вы ввели не 6 чисел")
    s = input("Введите 6 целых чисел через запятые(х1, x2, x3, x4, x5, x6):\n").split(",")
    len_s = len(s)
print("а) 4 элемент cписка:",s[3])
list.reverse(s)
print("б) Все элементы в обратном порядке: ",*s)
summ =0
for i in s:
    summ+=int(i)
print(f"в) Сумма всех элементов списка: {summ}"
      f"\nСреднее арифметическое {summ/6}")