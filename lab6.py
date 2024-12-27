# # №1
# rept = {"python" : " питон",
#  "anaconda" : "анаконда",
#  "tortoize" : " черепаха",}

# rept["snake"] = "Змея"
# rept["tortoise"] = rept["tortoize"]
# del rept["tortoize"]

# for key in rept:
#     print(f"Phone: {key}  User: {rept[key]} ")
# print(rept)


# # №2
# cnt = ["Andorra", "Belarus", "Denmark",
#  "Kenya", "Jamaica", "Romania"]
# fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]

# country = {}

# for i in range(len(cnt)):
#     country[cnt[i]] = fh[i]
# print(country)


# №3
# pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
# math = {}
# for i in pairs:
#     math[i] = i[0] * i[1]
# print(math)


# №4
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
 'Ursula': 4, 'Viktor': 5}

bad = []
satisf = []
good = []
excel = []

for key, value in grades.items():
    print(f"У студента {key} оценка {value}")
    if value == 2:
        bad.append(key)
    elif value == 3:
        satisf.append(key)
    elif value == 4:
        good.append(key)
    elif value == 5:
        excel.append(key)

print(f"Оценка 5:{excel}")
print(f"Оценка 4:{good}")
print(f"Оценка 3:{satisf}")
print(f"Оценка 2:{bad}")