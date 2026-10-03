porog = float(input())
n = int(input())
error = 0
above = 0
temps = []

for i in range(n):
    x = input()
    if x == "error":
        error += 1
    else:
        x = float(x)
        temps.append(x)
        if x > porog:
            above += 1

max_temp = max(temps)
sr = sum(temps) / len(temps)

print(n)
print(error)
print(above)
print(f"{max_temp:.1f}")
print(f"{sr:.1f}")

<<<<<<< HEAD
=======
#Проверка:
>>>>>>> b35e076 (a log has been added)
# ввод:
# 25
# 5
# 24.5
<<<<<<< HEAD
=======
# 30.1
>>>>>>> b35e076 (a log has been added)
# error
# 19
# 27.3
# вывод:
# 5
# 1
# 2
# 30.1
# 25.2