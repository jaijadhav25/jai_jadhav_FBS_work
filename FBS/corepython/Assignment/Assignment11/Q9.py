# 9. Write a program to create three lists of numbers, their squares and cubes
def square_cube(li):
    square = []
    cube = []
    for i in range(len(li)):
        square.append(li[i] ** 2)
        cube.append(li[i] ** 3)
    return square, cube

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(li)
square , cube = square_cube(li)
print(square)
print(cube)