# написаль программу для подсчёта индекса массы тела при помощи фуункции
name1 = "Tommi"
height1 = 1.90
weight1 = 80

name2 = "Kati"
height2 = 1.73
weight2 = 90

name3 = "Any"
height3 = 1.90
weight3 = 55


def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)

    print("Индекс массы тела: " + str(bmi))

    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " Имеет лишний вес"


bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)

print(bmi1)
print(bmi2)
print(bmi3)
