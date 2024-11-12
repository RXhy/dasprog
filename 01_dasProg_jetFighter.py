# Jet Fighter

#input distance and takeoff speed
distance = float(input("Input the take off distance (meter): "))
velocity = float(input("Input the take off speed (km/hr)   : "))

#calculate time and acceleration 
velocity = velocity *5/18 # km/hr to m/s 
time = (2*distance) / velocity # t=2s/v from v=at, with a =2s/t^2 
accel = 2*distance / (time**2) # a=2s/t^2 from s=1/2at^2

#output
print("time needed to accelerate :", format(time,".2f"), "second")
print("the acceleration of a jet fighter :", format(accel,".2f"), 'm/s^2')