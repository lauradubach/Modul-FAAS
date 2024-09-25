sum = 0

with open("first.txt", "r") as f:
    for line in f:
        i = 0
        while line[i] not in '0123456789':
            i+=1
        number1 = line[i]
        i = len(line) -1
        while line[i] not in '0123456789':
            i = i-1
        number2 = line[i]
        calibration = int(number1 + number2)
        sum += calibration
print(sum)





