len_s = 0
while len_s < 10:
    s = input("Введите фразу от 10 символов: ")
    len_s = len(s)
    if len_s>=10:
        print("а) Первые 4 символа фразы: ",s[0:4],
              "\nб) Последние 4 символа фразы: ",s[-4:])
        if(len_s%2):
            print("в) Символ посередине в фразе: ", s[len_s // 2])
        else:
            print("в) Число символов во фразе четное. Два символа посередине: ", s[len_s//2-1:len_s//2+1])
        print("г) Символы с 3 по 8 позицию в этой фразе: ",s[2:8])
    else:
        print("Фраза должна содержать не менее 10 символов!")
