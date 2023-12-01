import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

dictio = {
    #"zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

#function for part 2
def convertStrWithDictio(text, replaceDictio) :
    for tofind in replaceDictio :
        text = text.replace(tofind,tofind+replaceDictio[tofind]+tofind)
    return text

file = open('input.txt', 'r')
linesOfFile = file.readlines()
file.close()

#Part 1
result1 = 0

for line in linesOfFile:
    occurence = re.findall("\d", line)
    result1 += int(occurence[0] + occurence[-1])

result1 = str(result1)

#Part 2
result2 = 0

for line in linesOfFile:
    line = convertStrWithDictio(line,dictio)
    occurence = re.findall("\d", line)
    result2 += int(occurence[0] + occurence[-1])

result2 = str(result2)

#Display solutions
print("Sum of all calibration values part 1:", bcolors.BOLD + bcolors.OKGREEN + result1 + bcolors.ENDC)
print("Sum of all calibration values part 2:", bcolors.BOLD + bcolors.OKGREEN + result2 + bcolors.ENDC)
