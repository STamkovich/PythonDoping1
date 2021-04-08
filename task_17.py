# необходимо из существующего списка создать словарь
# a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
# словарь имеет один ключ и несколько значений

a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]
my_dict = {}
current_str = None
for e in a:
    if type(e) == str:
        my_dict[e] = []
        current_str = e
    else:
        my_dict[current_str].append(e)

for key, value in my_dict.items():
    print("КЛЮЧ: " + str(key) + " ,значения: " + str(value))

# КЛЮЧ: first ,значения: [1, 2, 3]
# КЛЮЧ: second ,значения: [10, 20]
# КЛЮЧ: third ,значения: [15, 56, 70]
# КЛЮЧ: fourth ,значения: [-50]
