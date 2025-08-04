### Program to find the roots of quadratic equation

a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))
c = float(input("Enter the value of c:"))

sq = ((b ** 2)-(4 * a * c)) ** 0.5

res1 = (- b + sq ) / 2 * a
res2 = (- b - sq ) / 2 * a

print(f"The solution for quadratic equation are ({res1} & {res2})")