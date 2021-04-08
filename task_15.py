# найти сумму отрицательных чисел
# (подсказка) вы должны только расматривать только отрицательные числа
# рушить нужно двумя способами while, for
my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15, -18]
new_list = my_list[::-1]
total = 0
i = 0
while new_list[i] < 0:
    total += new_list[i]
    i += 1

total1 = 0
i2 = -4
while my_list[i2] < 0:
    total1 += my_list[i2]
    i2 += 1

total2 = 0
for e in new_list:
    if e >= 0:
        break
    total2 += e
print(total)
print(total1)
print(total2)

# apple
# banana
# grape
# some other word
# apple
# banana
# grape
# some other word

