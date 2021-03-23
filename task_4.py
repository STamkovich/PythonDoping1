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

    print(f"Индекс массы тела: {round(bmi, 1)}")

    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " Имеет лишний вес"


a = (name1, height1, weight1)
k = {'name': name1, 'height': height1, 'weight': weight1}

bmi_calculator(name1, height1, weight1)
bmi_calculator(*a)

bmi_calculator(name=name1, height=height1, weight=weight1)
bmi_calculator(**k)
