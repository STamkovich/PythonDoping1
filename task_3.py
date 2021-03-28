# написать программу для подсчёта индекса массы тела
name = "Sergey"
height = 173
weight = 72

bmi = weight / (height ** 2)
print("ИНДЕКС МАССЫ ТЕЛА: " + str(bmi))

if bmi < 25:
    print("У " + name + " нет лишнего веса")
else:
    print("У " + name + " есть лишний вес")

# ИНДЕКС МАССЫ ТЕЛА: 0.00240569347455645
# У Sergey нет лишнего веса
