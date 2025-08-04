### Convert the time entered in hh,min and sec into seconds.

sec = int(input("Enter the number seconds:"))

hh = sec // 3600
sec = sec % 3600

min = sec // 60
sec = sec % 60

print(f"The time is {hh}hr {min}min {sec}sec")