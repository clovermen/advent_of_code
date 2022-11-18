def findOxygenGeneratorRating(input: list, position=0):
    if len(input) == 1:
         return int(''.join(input[0]), 2)
    
    zeros = 0
    ones = 0
    for binary in input:
        if binary[position] == '0':
            zeros += 1
        if binary[position] == '1':
            ones += 1

    fil = ''
    if zeros > ones:
        fil = '0'
    else:
        fil = '1'
    
    new_input = list(filter(lambda binary: binary[position] == fil, input))
    new_position = position+1

    return findOxygenGeneratorRating(new_input, new_position)

def findCO2ScrubberRating(input: list, position=0):
    if len(input) == 1:
        return int(''.join(input[0]), 2)
    
    zeros = 0
    ones = 0
    for binary in input:
        if binary[position] == '0':
            zeros += 1
        if binary[position] == '1':
            ones += 1

    fil = ''
    if ones < zeros:
        fil = '1'
    else:
        fil = '0'
    
    new_input = list(filter(lambda binary: binary[position] == fil, input))
    new_position = position+1

    return findCO2ScrubberRating(new_input, new_position)

input = open("./2021/Day3/input_part2.txt", "r")
content = list(map(lambda str: list(str), input.read().split('\n')))
input.close

length = len(content[0])


oxygenGeneratorRate = findOxygenGeneratorRating(content)
co2ScrubberRate = findCO2ScrubberRating(content)

print(oxygenGeneratorRate)
print(co2ScrubberRate)

print(oxygenGeneratorRate * co2ScrubberRate)