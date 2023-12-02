import re, sys

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

def openFileAndListLines(filePath):
    """This function will open an input file and will return a list of str lines
        - filePath : str
        Return : list formated (line1, line2, line3)
    """
    file = open(filePath, 'r')
    linesOfFile = file.readlines()
    file.close()
    return linesOfFile

def filterInputData(line):
    """This function will filter a str and will return a list formated
        - line : list
    Return :
        - gameId : int
        -  : list formated result (red(2,34,67),green(2,34,67),blue(2,34,67))
    """
    gameId = re.findall("(?<=Game ).\d*", line)

    red = re.findall("\d*.(?= red)", line)
    red = [int(nb) for nb in red]
    green = re.findall("\d*.(?= green)", line)
    green = [int(nb) for nb in green]
    blue = re.findall("\d*.(?= blue)", line)
    blue = [int(nb) for nb in blue]

    return int(gameId[0]), [red, green, blue]


def main():
    """resolve part 1 and part 2 but without creating that much functions and with keeping the code clear to debug it later if needed
    Mindset is to create python script with low constraint on efficiency and script that could be edited by people who's job isn't dev' and havn't time
    """
    filePath = "input.txt"
    maxRGB = [12, 13, 14] #Red, Green, Blue
    result1 = 0
    result2 = 0
    linesOfFile = openFileAndListLines(filePath)
    for line in linesOfFile :
        gameId, rgbList = filterInputData(line)
        #part2
        multiplication = 1
        for i in range(3):
            rgbList[i].sort()
            multiplication *= rgbList[i][-1]
        result2 += multiplication
        #part1
        for i in range(3):
            rgbList[i] = [j for j in rgbList[i] if j > maxRGB[i]]
        if not rgbList[0] and not rgbList[1] and not rgbList[2]:
            result1 += gameId

    print("Sum of all game ID values part 1:", bcolors.BOLD + bcolors.OKGREEN + str(result1) + bcolors.ENDC)
    print("Sum of factor of all lowest dice number per game part 2:", bcolors.BOLD + bcolors.OKGREEN + str(result2) + bcolors.ENDC)



if __name__ == '__main__':
    sys.exit(main())

#Architecture
#   open file
#   for each gameid f [gameid(r(2,45,64),g(2,45,64),b(2,45,64)),gameid()]
