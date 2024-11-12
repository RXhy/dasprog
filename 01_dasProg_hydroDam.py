#hydroelectric dam

#input height of the dam
height = float(input("please input the height of the dam in meter: "))
 
#input the nunmber of cubic meters of water
water = float(input("please input the volume of the flowing water each second: "))

#convert water to electrical energy
gravity = 9.80
mass = water * 1000
efficiency =  0.9

#formula 
energy = mass * gravity * height * efficiency

#output
print("The amount of energy that been produced is", energy/(10**6), "MW") #convert from watt to megawatt 