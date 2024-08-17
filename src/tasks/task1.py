userName = input("What you name?")
birthdayYear = input("Enter your birthday year: ")
currentYear = 2000
age = int(currentYear) - int(birthdayYear)
ageIn2035 = 2035 - int(birthdayYear)
print(age)
print("In 2035 ", userName,"'s age will:", ageIn2035)
ageBetween = 2000 - int(birthdayYear)
print(userName,"older for ", ageBetween, "years than birth in 2000")

birthdayYearTaras = 1861
ageTaras = int(currentYear) - int(birthdayYearTaras)
birthdayYearMaxim = int(currentYear) - int(ageTaras)*5
petroAge = (2061 - int(birthdayYearTaras))/4
print("Taras age:", ageTaras)
print("Maxim age: " , int(currentYear) - int(birthdayYearMaxim))
print("Petro age:", petroAge)

