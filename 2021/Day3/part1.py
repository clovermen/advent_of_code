input = open("./2021/Day3/input_part1.txt", "r")
content = list(map(lambda str: list(str), input.read().split('\n')))
input.close

length = len(content[0])

gammaBin = ''
epsilonBin = ''

for i in range(length):

    zeros = 0
    ones = 0

    for binary in content:
        if binary[i] == '0':
            zeros += 1
        if binary[i] == '1':
            ones += 1
    

    if zeros > ones:
        gammaBin += '0'
        epsilonBin += '1'
    if ones > zeros:
        gammaBin += '1'
        epsilonBin += '0'


gamma = int(gammaBin, 2)
epsilon = int(epsilonBin, 2)

print(gamma * epsilon)