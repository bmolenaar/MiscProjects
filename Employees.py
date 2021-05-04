from datetime import datetime

curDate = datetime.today()

# Read employees text file
employeesFile = open("employees.txt", "r")
employees = employeesFile.readlines()
employeesFile.close()

# print date
print("#" * 45)
print("Report run on: " + str(curDate))
print("#" * 45)

#Loop through the lines of the text file and read them into an array
for i in employees:

	#Make each individual line it's own array
    s = i.split(",")
	
	#Test how many items are in each line and set variables 
    if len(s) == 2:
        lastName = s[0]
        firstName = s[1].strip("\n")
        dayOne = ""
        dayTwo = ""

    elif len(s) == 3:
        lastName = s[0]
        firstName = s[1]
        if s[2] != "":
            dayOne = s[2]
        else:
            dayOne = ""
        dayTwo = ""
    else:
        lastName = s[0]
        firstName = s[1]
        if s[2] != "":
            dayOne = s[2]
        else:
            dayOne = ""
        dayTwo = s[3]

	#Check for each line for blanks and display
    if dayOne != "" and dayTwo != "":
        print(firstName + " " + lastName + " will receive both days pack \n")
    elif dayOne != "" or dayTwo != "":
        print(firstName + " " + lastName + " will receive a single day pack \n")
    else:
        print(firstName + " " + lastName + " will not receive a conference pack \n")


str(input("Press enter to close"))
