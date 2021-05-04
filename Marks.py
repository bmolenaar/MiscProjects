def getMarks(one, two, three, four, five):
    marks = []
    #Get 5 inputs
    one = int(input("Please enter a mark for subject one as a whole number:"))
    two = int(input("Please enter a mark for subject two as a whole number:"))
    three = int(input("Please enter a mark for subject three as a whole number:"))
    four = int(input("Please enter a mark for subject four as a whole number:"))
    five = int(input("Please enter a mark for subject five as a whole number:"))
    #one = 1
    #two = 2
    #three = 3
    #four = 4
    #five = 5

    #Add inputs to list
    marks.extend([one, two, three, four, five])

    #Print inputs
    print("The marks you entered - " + str(marks))

    #Sum inputs together and display
    totalMarks = sum(marks)
    print("The sum of your marks is: " + str(totalMarks))

    #Average out the marks and display
    print("The average of your marks is: " + str(totalMarks / len(marks)))

    return marks


getMarks(1, 2, 3, 4, 5)
input("Press enter to close")