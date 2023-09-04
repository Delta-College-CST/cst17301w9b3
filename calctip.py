# This program adds the tip to calculate the total
# cost of a meal.

# Input
name = input("Enter your name: ")
cost = float(input("Enter base cost for meal: "))

# Calculate gratuity
tip       = cost * 0.18
totalCost = cost + tip

# Output
print (name,"your meal will cost $",totalCost)
