print("Identification number must be 10 characters long")
id = int(input("Enter your identification number: "))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

if len(str(id)) == (10-1):
  if id % 11 == 0:
    mm = str(id)[1:3]
    mm = int(mm)

    if str(id)[2] == 5 or str(id)[2] == 6:
      print(months[mm-51])
      print("Woman")
    else:
      print(months[mm-1])
      print("man")

  else:
    print("Invalid identification number")

else:
  print("Incorrect length, try again")
