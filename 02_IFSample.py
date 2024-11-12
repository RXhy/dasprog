problem =str(input("Problem yang mana : "))

match problem:
    case "1": 
        #discount student 
        
        purchaseTotal =float(input("total your purcahse's ($)"))        #total purchase 
        isStudent = input("are you a student (Y/N)")                    #check is the user student or not
        discount = purchaseTotal*0.8                                    #student discount
        
        if  isStudent == "Y":              #if Student 
            print("Total Purchase          : $",format(purchaseTotal,".2f"))
            print("Student's discount (20%):  ",format(purchaseTotal-discount,".2f"))
            print("Discounted total        :  ",format(discount,".2f"))
            print("Sales tax (5%)          :  ",format(discount*0.05,".2f"))
            print("Total                   : $",format(discount+(discount*0.05),".2f"))
        elif isStudent == "N":             #not student
            print("Total Purchase          : $",format(purchaseTotal,".2f"))
            print("Sales tax (5%)          :  ",format(purchaseTotal*0.05,".2f"))
            print("Total                   : $",format(purchaseTotal+(purchaseTotal*0.05),".2f"))
        else:
            print("mbalen")                # try again if user put the wrong answer 
    
    case "2":
        #BMI 
    
        bodyMass = float(input("please insert your body weight in pounds> "))   #input mass in american 
        bodyHeight = float(input("please insert your height in inches> "))      #input height
        bmi = round((703*bodyMass)/bodyHeight**2)                               #formula
        
        if bmi < 18.5:
            print("you are underweight",bmi)
        elif bmi >= 18.5 and bmi < 25: 
            print("you are normal",bmi)
        elif bmi >= 25 and bmi < 30: 
            print("you are overweight",bmi)
        elif bmi >= 30: 
            print("YOU ARE OBESE",bmi) 
        
    case "3":
        print("C")
        
    case "4": 
        #its cylinder
         
        letter = str(input("input your cylinder color: "))
         
        if letter == "Y" or letter == "y":
             print("Hydrogen")
        elif letter == "O" or letter == "o":
             print("Ammonia")
        elif letter == "B" or letter == "b":
             print("Carbon monoxide")
        elif letter == "G" or letter == "g":
             print("Oxygen")
        else: 
            print("idk")
    
    case "5": 
        #Data usage
        
        jenisData = input("Inster data in GB OR MB: ")
        dataUsage = 0
        if jenisData == "GB" or jenisData == "gb":
            dataUsage = float(input("Data usage for 1 month in GB: "))
        elif  jenisData == "MB" or jenisData == "mb":
            dataUsage = float(input("Data usage for 1 month in MB: "))
            dataUsage = dataUsage / 1000
        
        if dataUsage <= 1:
            charge = 250
        elif dataUsage <= 2:
            charge = 500
        elif dataUsage <=5: 
            charge = 1000
        elif dataUsage <=10: 
            charge = 1500
        else: 
            charge = 2000
        
        print("you need to pay",charge,"this month by using",dataUsage,"GB")   
    
    case "6": 
        #quadrant
        
        coordinate = input("Coordinate (x,y): ").split(",")
        x = float(coordinate[0])
        y = float(coordinate[1])
        
        if x == 0: 
            print("(",x,",",y,") is on the y-axis")
        elif y == 0: 
            print("(",x,",",y,") is on the x-axis")
        elif x > 0 and y > 0: 
            print("(",x,",",y,") is in quadrant I")
        elif x < 0 and y > 0: 
            print("(",x,",",y,") is in quadrant II")
        elif x < 0 and y < 0: 
            print("(",x,",",y,") is in quadrant III")
        elif x > 0 and y < 0: 
            print("(",x,",",y,") is in quadrant IV")
            
    case "8":
        #free services
        print("(1) First Free Service")
        print("(2) Second Free Service")
        
        selection = input("Enter the Free Service number>> ")
        miles = input("Enter number of Miles>>")
        
        if selection == "1":
            if miles <= 3000 and miles > 1500: 
                print("Vehicle must be serviced.")
            else:
                print("Vehicle doesnt need services") 
        elif selection == "2":
            if miles > 3001 and miles <= 4500: 
                print("Vehicle must be serviced.") 
            else: 
                print("Vehicle doesnt services.")    
    
    case "9":
        #Chatflow Wireless
        
        timeChat = (input("Weekday minutes,night minutes and weekend minutes used: ")).split(",")
        weekday, night, weekend = map(float,timeChat)
        cost = weekday*39.99
        
        if weekday > 600:
            cost = cost + (weekday - 600)*0.40
            
        taxes = cost*0.0525 
        
        print("Weekdays minutes used:",weekday)
        print("Night minutes used   :",night)
        print("Weekend minutes used :",weekend)
        print("monthly bill         :",cost)
        print("average minute cost  :",cost/weekday+weekend+night)
        print("taxes                :",taxes)
        print("total bill           :",cost+taxes)
                         
    case "10":
        #Bread Machine 
        breadVariant = input(" White or Sweet bread (White/Sweet): ")
        loafSize = input("is nromal or double loaf (N/D) : ")
        baking = input("manual or auto baking (M/A)      : ")
        
        def display_instructions(breadVariant, loafSize, baking):
            time_chart = {
                'White': {
                    'Primary kneading': 15,
                    'Primary rising': 60,
                    'Secondary kneading': 18,
                    'Secondary rising': 20,
                    'Loaf shaping': round(2 / 60),  # 2 seconds in minutes
                    'Final rising': 75,
                    'Baking': 45,
                    'Cooling': 30
                },
                'Sweet': {
                    'Primary kneading': 20,
                    'Primary rising': 60,
                    'Secondary kneading': 33,
                    'Secondary rising': 30,
                    'Loaf shaping': round(2 / 60),  # 2 seconds in minutes
                    'Final rising': 75,
                    'Baking': 35,
                    'Cooling': 30
                }
            }
            # Get the times for the selected bread type
            times = time_chart[breadVariant]
            # Adjust baking times if the loaf size is double
            if loafSize == 'D':
                for step in ['Primary kneading', 'Primary rising', 'Secondary kneading',
                            'Secondary rising', 'Final rising', 'Baking']:
                    times[step] *= 1.5  # Increase by 50%
            
            # Display instructions
            print(f"\nInstructions for {breadVariant} Bread:")
            print(f"1. Primary kneading: {times['Primary kneading']} mins")
            print(f"2. Primary rising: {times['Primary rising']} mins")
            print(f"3. Secondary kneading: {times['Secondary kneading']} mins")
            print(f"4. Secondary rising: {times['Secondary rising']} mins")
            print(f"5. Loaf shaping: {times['Loaf shaping']} mins")
            print(f"6. Final rising: {times['Final rising']} mins")
            if baking == 'M' or 'manual':
                print("7. Remove dough after loaf shaping and bake manually.")
            else:
                print(f"7. Baking: {times['Baking']} mins")
            print(f"8. Cooling: {times['Cooling']} mins")
            
        display_instructions(breadVariant,loafSize,baking)
