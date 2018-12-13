keepGoing = True        #Keeps the loop going

print("\n<------------------------------------------------------------------------->")
print("                     WELCOME TO ELLIS'S GPA CALCULATOR                      ")
print("<------------------------------------------------------------------------->\n")



print("Input Done if you're done inputting your class\n") #Instructions
grade = 0.0     #The grade for each class ex: A, B, C, etc.
numCredits = 0.0        #Records how many total credits to divide by
gradePoint = 0.0        #total Gradepoints, gets divided later
i = 1           #For the index of which class you are on

while keepGoing:
    classGrade = input("Enter your grade for class "+ str(i)+ ": ")
    #Checks to see what grade and does calculations based on that
    if (classGrade == "done" or classGrade == "Done"):
        keepGoing = False
    elif (classGrade == 'A' or classGrade == 'a'):
        creditHour = int(input("How many credit hours was this class? "))
        grade = 4.0
        gradePoint += (grade * creditHour)
        numCredits += creditHour
    elif (classGrade == 'b' or classGrade == 'B'):
        creditHour = int(input("How many credit hours was this class? "))
        grade = 3.0
        gradePoint += (grade * creditHour)
        numCredits += creditHour
    elif (classGrade == 'C' or classGrade =='c'):
        creditHour = int(input("How many credit hours was this class? "))
        grade = 2.0
        gradePoint += (grade * creditHour)
        numCredits += creditHour
    elif (classGrade == 'D'or classGrade == 'd'):
        creditHour = int(input("How many credit hours was this class? "))
        grade = 1.0
        gradePoint += (grade * creditHour)
        numCredits += creditHour
    elif (classGrade == 'F' or classGrade == 'f'):
        creditHour = int(input("How many credit hours was this class? "))
        grade = 0.0
        gradePoint += (grade * creditHour)
        numCredits += creditHour
    else:
        i-=1
        print("Please enter a valid grade")
    i+=1
#formula for GPA
gpa = gradePoint/numCredits
print("Your GPA is: " , round(gpa, 2))

print("\n<------------------------------------------------------------------------->")
print("                     ELLIS'S GPA CALCULATOR SAYS GOODBYE                      ")
print("<------------------------------------------------------------------------->\n")

