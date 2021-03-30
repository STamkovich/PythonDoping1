# написаль программу для подсчёта индекса массы тела при помощи функции
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
        return name + " имеет лишний вес"


bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)
out_string = ','.join([bmi1, bmi2, bmi3])
print(f'{out_string}.')

#  Индекс массы тела: 22.1606648199446
#  Индекс массы тела: 30.071168431955627
#  Индекс массы тела: 15.235457063711912
#  Tommi не имеет лишнего веса, Kati имеет лишний вес, Any не имеет лишнего веса.
