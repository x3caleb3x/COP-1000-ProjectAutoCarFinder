#Vehicle Finder


#Function to List Cars
def vehicles():
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
  file = open("authorizedvehiclelist.txt", "r")
  response = file.read()
  print(response)

#Menu
while input != 5:
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please enter the following number below from the following menu:")
  print("1. PRINT all Authorized Vehicles")
  print("2. Exit")

  menu = int(input(""))
  #Menu Selection
  if menu == 1:
    vehicles()

  if menu == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()
