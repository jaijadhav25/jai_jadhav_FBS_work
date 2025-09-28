# 12. Write a program to create three lists of numbers, their squares
# and cubes

def square_cube(li):
    square = []
    cube = []
    for i in range(len(li)):
        m = li[i] ** 2
        n = li[i] ** 3
        square.append(m)
        cube.append(n)
    return square, cube

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li)
square , cube = square_cube(li)
print(square)
print(cube)