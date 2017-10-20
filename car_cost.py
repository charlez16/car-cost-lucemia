#car_cost
#The problem is to find out how much the car is going to be monthly
#Charles & Enes
#10/20/17
#There are no bugs

carValue = float(input("What is the value of your new car: "))
salesTax = 0.06 * carValue
registrationFee = 192
dealerFee = 200
deliveryFee = 120
extras = registrationFee + dealerFee + deliveryFee
total = salesTax + extras + carValue
r = 0.09 / 12
payment = ((r*(1 + r)**36) \
           /(((1 + r)**36)-1))*carValue
print ("total cost "+ str(total))
print ("payment " + str(int(payment)))


