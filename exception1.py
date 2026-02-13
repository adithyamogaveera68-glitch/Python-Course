def validateAge(age):
    if(age<=18):
        raise Exception("invalid age")
    else:
        print("eligible")

try:
   validateAge(20)
except Exception as e:
   print(e)