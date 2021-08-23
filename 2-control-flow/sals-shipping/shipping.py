weight = 41.5
# user types the weight of the cargo
cost = 0
# initial cost is zero 

typeOfShipment = 'Premium'
# The user needs to choose the type of the shipment - 'Ground', 'Premium' or 'Drone' 

#Now we will decide the price(cost) based on the type of shipment and the weight of the package. 
if typeOfShipment == 'Ground':
  cost = 20
  if weight <= 2:
    cost += weight * 1.5
  elif weight <= 6:
    cost += weight * 3
  elif weight <= 10:
    cost += weight * 4
  else:
    cost += weight * 4.75
elif typeOfShipment == 'Premium':
    cost = 125
else:
  if weight <= 2:
    cost = weight * 4.5
  elif weight <= 6:
    cost = weight * 9
  elif weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25 

#now we will print the cost to the user 
print('The cost of your shipment is ' + str(cost))
