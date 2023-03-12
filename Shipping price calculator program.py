print ('''==========================================
|          *** Order Total ***           |
------------------------------------------
''')

price = float(input("Enter Order summary : "))

print ('''
-------------------------------------------
|  Destination:                            |
|     (BK) The Bangkok Metropolitan Region |
|     (TH) For areas in other provinces    |
-------------------------------------------
''')

option = input("Enter destination : ")
weight = float(input("Enter total weight(KG) : "))

print ('''
------------------------------------------
|    Weight   |     BK     |      TH      |
------------------------------------------
|     1-5     |     80     |      140     |
|     6-10    |     150    |      200     |
|     10+     |     200    |      250     |
------------------------------------------
''')

if price>=3000 and price<=5000 :
  print ("Order Summary : %.2f" %price)
  price1 = price-60
  if option == "BK" :
    if weight>=1 and weight<=5 :
      print ("shipping      : 80.00")
      price2 = price1+80
    elif weight>=6 and weight<=10 :
      print ("shipping      : 150.00")
      price2 = price1+150
    elif weight>10 :
      print ("shipping      : 200.00")
      price2 = price1+200
  elif option == "TH" :
    if weight>=1 and weight<=5 :
      print ("shipping      : 140.00")
      price2 = price1+140
    elif weight>=6 and weight<=10 :
      print ("shipping      : 200.00")
      price2 = price1+200
    elif weight>10 :
      print ("shipping      : 250.00")
      price2 = price1+250
  print("discount      : -60.00")
  print('''========================
Order Total   : %.2f
========================''' %price2)
elif price>5000 :
  print ("Order Summary : %.2f" %price)
  price1 = price-120
  if option == "BK" :
    if weight>=1 and weight<=5 :
      print ("shipping      :  80.00")
      price2 = price1+80
    elif weight>=6 and weight<=10 :
      print ("shipping      :  150.00")
      price2 = price1+150
    elif weight>10 :
      print ("shipping      :  200.00")
      price2 = price1+200
  elif option == "TH" :
    if weight>=1 and weight<=5 :
      print ("shipping      :  140.00")
      price2 = price1+140
    elif weight>=6 and weight<=10 :
      print ("shipping      :  200.00")
      price2 = price1+200
    elif weight>10 :
      print ("shipping      :  250.00")
      price2 = price1+250
  print("discount      : -120.00")
  print('''========================
Order Total   : %.2f
========================''' %price2)