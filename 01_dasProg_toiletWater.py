# Toilet water
import math 

#input community population
population = int(input("Community's population :"))

#every data about toilet
oldToilet = 15 #liters/flush
newToilet = 2 #liters/flush 
#toilet flushed 14 times a day
amountToilet = math.ceil(population / 3) #soale klo misal 10 / 3 = 3... ga mungkin toilet koma dan sisa 1nya harus dibuat toilet baru
costToilet = 150 * amountToilet #dollar for total population  

#calculate 
magnitudeOld = amountToilet * oldToilet * 14 #liters/day using old toilet
magnitudeNew = amountToilet * newToilet * 14 #liters/day using new toilet

#output 
print("Water that used for toilets per day by", population, "people is", magnitudeNew, "liters/day with low flush models.")
print("water used for toilets reduced from", magnitudeOld, "liters/day to", magnitudeNew, "liters/day,") 
print("Saving", magnitudeOld-magnitudeNew, "liters with the cost of", costToilet, "dollars to install new toilet.")