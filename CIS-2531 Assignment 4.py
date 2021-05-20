def main():
    testScores = [90,85,52,74,95,100,78]
    displayScores(testScores)
    print()
    minimum = findMin(testScores)
    print("Lowest Score: ", minimum)
    maximum = findMax(testScores)
    print("Highest Score: ", maximum)

    average = getMean(testScores)
    print("Average: ", average)
    print("")
    median = getMedian(testScores)
    print("Median: " + str(median))
    


    dropLowestScore(testScores)
    print("After dropping the lowest score. ")
    displayScores(testScores)
    print("")
    

    average = getMean(testScores)
    print("Average: ", average)
    print("")
    print("")
    print("Median: " + str(median))
    
    saveScores(testScores)
    #studentScores = getScores(getScores)
    #print("" + str(studentScores))
    

    

    


    
def displayScores(scoreArray):
    print("The current test scores are:")
    for i in range(len(scoreArray)-1):
        print(float(scoreArray[i]), end= "%, ")
    print(float(scoreArray[len(scoreArray)-1]), end = "%\n")
    


def findMin(scoreArray):
    count = 0
    smallScore = scoreArray[0]
    while count < len(scoreArray):
        if scoreArray[count] < smallScore:
            smallScore = scoreArray[count]
        count = count + 1
    return smallScore

def findMax(scoreArray):
    count2 = 0
    largerScore = scoreArray[1]
    while count2 < len(scoreArray):
        if scoreArray[count2] > largerScore:
            largerScore = scoreArray[count2]
        count2 = count2 + 1
    return largerScore
    
def dropLowestScore(scoreArray):
        scoreArray.remove(findMin(scoreArray))

def getMean(scoreArray):
    count = 0 
    total = 0 
    while count != len(scoreArray):
        total += scoreArray[count]
        count = count + 1
    average = total / count
    return average
        

def getMedian(scoreArray):
    scoreArray.sort()
    
    n = len(scoreArray) 
    if n % 2 == 0: 
        median1 = scoreArray[n//2] 
        median2 = scoreArray[n//2 - 1] 
        median = (median1 + median2)/2
    else: 
        median = scoreArray[n//2] 
    return median 



def getScores():
    student_scores = open("scores.txt", "r")
    for line in student_scores:
        print(line)
    student_scores.close()   
    

def saveScores(scoreArray):
    filename = "updatedFile.txt"
    count = 0
    new = open(filename, 'w')
    while count != len(scoreArray):
        new.write(str(scoreArray[count]))
        count = count + 1
    new.close()


# def saveScores(scoreArray):
#     L = [scoreArray]
 
#     # writing to file
#     file1 = open('scores.txt', 'w')
#     file1.writelines(L)
#     file1.close()
 
#     # Using readlines()
#     file1 = open('scores.txt', 'r')
#     Lines = file1.readlines()
 
#     count = 0
#     # Strips the newline character
#     for line in Lines:
#         count += 1
#         print("Line{}: {}".format(count, line.strip()))







# #def saveScores(scoreArray):
#     #index = 1
#     updateScores = open('updatedScores.txt', 'w')
#     studentscores = [scoreArray]

#     for index in range(0, len(scoreArray)):
#         if studentscores[0] > 6:
#             updateScores.write(""+ '\n' + scoreArray)
#             studentscores = studentscores + index

#         updateScores.close()
#     return updateScores
main()

