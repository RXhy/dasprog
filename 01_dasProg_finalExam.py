# Final exam score

#input
desiredGrade = str(input("Enter desired grade> "))
minAverage = float(input("Enter minimum average required> "))
currentAverage = float(input("Enter current average in course> "))

#check 
if currentAverage >= minAverage:
    print("your score already pass the desired grade")
else:         
    finalPercentage = float(input("Enter how much the final counts as a percentage of the course grade> "))
    
#Calculate Score
    firstPercentage = (100 - finalPercentage) /100 # (0.xx) / amount of the rest percentage  
    score = currentAverage * firstPercentage #total score that already obtained
    score = (minAverage - score) / (finalPercentage/100) #score that needed

#output
    print("You need a score of", format(score,".2f"),"on the final to get",desiredGrade)