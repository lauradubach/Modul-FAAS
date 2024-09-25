reversed_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

sum = 0
with (open("first.txt", "r") as file):
    for line in file:

        i = 0
        number1 = None
        while not number1:
            for k,v in reversed_dict.items():
                if line[i:len(k)+i] == k:
                    number1 = v
                    break
            i+=1
        i = len(line) - 1
        number2 = None
        while not number2:
            for k,v in reversed_dict.items():
                if line[i-len(k):i] == k:
                    number2 = v
                    break
            i = i - 1

        calibration = int(f"{number1}" + f"{number2}")
        sum += calibration
print(sum)