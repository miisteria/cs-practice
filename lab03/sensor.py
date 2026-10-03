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