import numpy as np
from datetime import datetime, date, timedelta

#Exercice 1
def ex1():
    mainList = ["Red", "Green","White", "Black", "Pink", "Yellow"]
    print("Original array:")
    print(mainList)
    altList = mainList[1:4]
    print("After removing first and last elements from the said array:")
    print(altList)

    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    print(' '.join(map(str, list2)) in ' '.join(map(str, list1*2)))

    numList = [33, 56, 4, 80, 23, 100, 1, 0, 40, 11]
    print("Original array:")
    print(numList)
    print(numList[0:7])
    print(numList[-1])
    print(numList[::-1][0:3])

    def takeSecond(elem):
        return elem[1]
    def sortList(list):
        list.sort(key=takeSecond)
        print(list)
        return list
    tupleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sortList(tupleList)

#Exercice 2
def ex2():
    lambdaList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    power2 = lambda x: x**2
    power3 = lambda x: x**3
    print("Original list:")
    print(lambdaList)
    print("Square every number of the said list:")
    print(list(map(power2, lambdaList)))
    print("Cube every number of the said list:")
    print(list(map(power3, lambdaList)))

#Exercice 3
def ex3():
    mdict = {'a': 1, 'b': 2, 'c': 3}
    altDict = {'n': 5}
    def checkDict(mdict, key):
        if key in mdict.keys():
            print("True")
        else:
            print("False")
    checkDict(mdict, 'a')
    checkDict(mdict, 'z')

    for key in mdict.keys():
        print(key)
    for value in mdict.values():
        print(value)
    for key, value in mdict.items():
        print(key, value)

    for i in range(1, altDict['n']+1):
        altDict[i] = i**2
    altDict.pop('n')
    print(altDict)

    mapList1 = [1, 2, 3]
    mapList2 = [10, 20, 30]
    mapDict = dict(zip(mapList1, mapList2))
    print(mapDict)

#Exercice 4
def ex4():
    def sumTup(tup):
        listtup = []
        for i in range(0, len(tup[1])):
            sum= 0
            for j in range(0, len(tup)):
                sum += tup[j][i]
            listtup.append(sum)

        sumTuple = tuple(listtup)
        print(sumTuple)
        return sumTuple
    mtple = sumTup([(1, 2, 3, 4) ,(3, 5, 2, 1),(2, 2, 3, 1)])

#Exercice 5
def ex5():
    now = datetime.now()
    print("Current Time =", now)

    today = date.today()
    print("Current date =", today)
    yesterday = today - timedelta(days = 1)
    print("Yesterday date =", yesterday)
    tomorrow = today + timedelta(days = 1)
    print("Tomorrow date =", tomorrow)
    tday5 = today - timedelta(days = 5)
    print("5 days before Current date =", tday5)
    nbweek = today.isocalendar()[1]
    print("Current week number =", nbweek)


    def numOfDays(date1, date2):
        # check which date is greater to avoid days output in -ve number
        if date2 > date1:
            return (date2 - date1).days
        else:
            return (date1 - date2).days


    date1 = date(2023, 12, 13)
    date2 = date(2023, 2, 25)
    print(numOfDays(date1, date2), "days")

#Exercice 6
def ex6():
    f = open("test.txt", "r")
    nblines = len(f.readlines())
    print(nblines)

    if f.closed == False:
        print("File is not closed")
    else:
        print("File is closed")
    f.close()

    f = open("test.txt", "w")
    f.write("Hello World")
    f.close()

    text = open("test.txt", "r")
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])

ex3()