n = int(input("Enter some number: "))

if str(n)[-1] == 8:
  if n % 3 == 0:
    print("number ends with 8 and IS divisible by 0")
  elif n % 3 != 0:
    print("number ends with 8 and IS NOT divisible by 0")
elif str(n)[-1] != 8:
  if n % 3 == 0:
    print("number DOES NOT end with 8 and number IS divisible by 0")
  elif n % 3 != 0:
    print("number DOES NOT end with 8 and number IS NOT divisible by 0")
