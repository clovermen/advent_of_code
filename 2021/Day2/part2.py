input = open("./2021/Day2/input_part2.txt", "r")
content = list(map(lambda str: str.split(' '), input.read().split('\n')))
input.close

horizontal = 0
depth = 0
aim = 0

for command in content:
    match command[0]:
        case 'forward':
            horizontal += int(command[1])
            depth += int(command[1]) * aim
        case 'up':
            #depth -= int(command[1])
            aim -= int(command[1])
        case 'down':
            #depth += int(command[1])
            aim += int(command[1])

print(depth)
print(horizontal)
print(depth * horizontal)
