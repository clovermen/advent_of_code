input = open("./2021/Day1/input_part1.txt", "r")
content = list(map(lambda str: int(str), input.read().split('\n')))
input.close


previous = 0
tracker = 0

for i in range(len(content)):

    measurement = content[i]

    if(i == 0):
        previous = measurement
    

    if previous < measurement:
        tracker += 1
    previous = measurement


print(tracker)