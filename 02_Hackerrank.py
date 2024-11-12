soal =str(input("Soal yang mana : "))

match soal:
    case "1":
        #Witch riddle
        
        #input
        number = input("insert the list: ").split()
        cat = int(input("number of the cat that will jump: "))
        jump = int(input("how many times cat will jump: "))
        where = input("selecet the index: ").split()    
        
        x = int(where[0])
        y = int(where[1])
        z = int(where[2])
        
        #process
        i = 0
        for i in range(0,jump):
            number = number[-cat:] + number[:-cat] 
        
        print(number[x],number[y],number[z])
        
    case "2": 
        #Prime Beginning
        g = int(input("input the number: "))
        
        if g == 2:
            is_prime = True
        elif g > 2: 
            is_prime = True                         #For numbers greater than 2, check for factors from 2 up to the square root of the number (int(number**0.5) + 1). 
            for i in range(2, int(g**0.5) + 1):     #If any of these numbers divides the given number evenly (i.e., number % i == 0), then the number is not prime.
                if g % i == 0:
                    is_prime = False
                    break
                 
        if is_prime:  
            print("IT IS A PRIME")
        else:
            print("IT IS NOT A PRIME")
    
    case "3":
        #Sever the number
        number = input("Enter the number: ")
        if '4' in number: 
            print("SEVER")
        else: 
            print("UNITE")
            
    case "4": 
        #mulyosari Avenue 
        line = input().split()
        m = int(line[0]) #cars in front 
        n = int(line[1]) #cars behind 
        t = int(line[2]) #time
        you = False #your car
        
        #1 car pass in 5s / t - red(20) -yellow(5) -green(60) / green = 12 car
        while t > 0:        #one cycle              
            if t <=0 or (m == 0 and n == 0 and you == True):
                break
            t = t - 25      #red and yellow
            print(t,m,n,"cycle")
            while t > 0:    #green
                if m > 0:   #check car in front of us 
                    m = m-1 #1 car pass
                    t = t-5
                    print(t,m,n,"front car")
                else:           #if no one in front of us  
                    if you == False: 
                        t = t-5 #our time to pass
                    you = True  #we already pass
                    print(t,m,n,you,"our car")
                    if t > 0:   #we count the cars behind 
                        while n > 0:
                            n = n-1
                            t = t-5
                            print(t,m,n,"back car")
                        if n == 0:
                            break  
                          
        if you == True: 
            print("YES!",m+n,t)
        else:
            print("NO!",m+n+1,t)        
             
    case "5": 
        #Lala Lili
        ll = input().split()  
        n = int(ll[0])
        c = int(ll[1]) #1 lala #2 lili 
        
        if n % 2 == 0:  #ganjil  
            if c == 2: 
                print("Lili")   
            elif c ==1: 
                print("Lala")
        else:           #genap
            if c == 2:
                print("Lili")
            elif c == 1: 
                print("Lala")  
                 
    case "6":
        #Genesis and Pillar
        pillar = input().split()
        maxDistance = int(pillar[0])
        aB = int(pillar[1])
        bC = int(pillar[2])
        cD = int(pillar[3])
        dE = int(pillar[4])
        
        if aB <= maxDistance and bC <= maxDistance and cD <= maxDistance and dE <= maxDistance: 
            print("YES HE CAN")
        else: 
            print("NO HE CANT")   
            
    case "7": 
        #Different time zone
        event = input("event in GMT+2     :").split(":")
        time =  input("right now in GMT+7 :").split(":")
        hh,mm,ss = map(int,event)
        ch,cm,cs = map(int,time)
        
        #convert hour to GMT+2
        ch = ch -5
        
        #check 
        def Waiting_Time(hh,mm,ss,ch,cm,cs):
            if ch > hh: 
                return False
            elif ch == hh:
                if mm - cm > 0:
                    if ss - cs > 0:
                        return True
            return False    
        
        #output
        if Waiting_Time(hh,mm,ss,ch,cm,cs):
            print(hh-ch,":",mm-cm,":",ss-cs)
        else: 
            print("See you on the next Pear Event!")