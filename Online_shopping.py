global status
selectedCountry = ''
selectedGender = ''
selectedSection = ''

status = "new"

print("Welcome TO Zara")

cartProductName = []
cartPrice = []
cartSize = []
cartColor = []
totalPrice = 0.0



sizeIndex = [1,2,3,4]
sizeName = ["Small","Medium","Large","XLarge"]

colorIndex = [1,2,3,4,5,6,7,8]
colorName = ["white","black","red","brouwn","green","yellow","blue","Pink"]

def womanfunc():
  WomanIndex = [1,2,3,4]
  WomanProducts = ['OVERSIZE COAT', 'BUTTONED CAPE - LIMITED EDITION', 'LONG COTTON TRENCHCOAT', 'TEXTURED WOOL BLEND COAT']
  WomanPrices = [65.900, 79.900, 49.900, 79.900]

  for i in range(len(WomanProducts)):
    print(f'{WomanIndex[i]}: {WomanProducts[i]}, Price: OMR: {WomanPrices[i]}')
  
  try:
    value = int(input("Select item number that you want: "))
    value -=1
  except ValueError:
    print("You should print number")
    return womanfunc()

  for i in range(len(sizeName)):
    print(f'{sizeIndex[i]}: {sizeName[i]}')
  try:
   sizeValue = int(input("Select color that you want: "))
   sizeValue -=1
  except ValueError:
    print("You should print number")
    return womanfunc()

  for i in range(len(colorName)):
    print(f'{colorIndex[i]}: {colorName[i]}')
  try:
    colorValue = int(input("Select color that you want: "))
    colorValue -=1
  except ValueError:
    print("You should print number")
    return womanfunc()

  
  if (colorValue >= 0 and colorValue <= 7) and (sizeValue >= 0 and sizeValue <= 3) and (value >= 0 and value <=3):
    cartProductName.append(WomanProducts[value])
    cartPrice.append(WomanPrices[value])
    cartSize.append(sizeName[sizeValue])
    cartColor.append(colorName[colorValue])
    return
  else:
    return womanfunc() 


def manfunc():
  ManIndex = [1,2,3,4]
  ManProducts = ['HOODED PUFFER PARKA', 'TECHNICAL WINDBREAKER PARKA', 'DOUBLE-BREASTED COAT', 'NEON TRENCH COAT - LIMITED EDITION']
  ManPrices = [39.900, 25.900, 59.900, 59.900]

  for i in range(len(ManProducts)):
    print(f'{ManIndex[i]}: {ManProducts[i]}, Price: OMR: {ManPrices[i]}')
  
    
  try:
    value = int(input("Select item number that you want: "))
    value -=1
  except ValueError:
    print("You should print number")
    return manfunc()

  for i in range(len(sizeName)):
    print(f'{sizeIndex[i]}: {sizeName[i]}')
  try:
   sizeValue = int(input("Select color that you want: "))
   sizeValue -=1
  except ValueError:
    print("You should print number")
    return manfunc()

  for i in range(len(colorName)):
    print(f'{colorIndex[i]}: {colorName[i]}')
  try:
    colorValue = int(input("Select color that you want: "))
    colorValue -=1
  except ValueError:
    print("You should print number")
    return manfunc()

  if (colorValue >= 0 and colorValue <= 7) and (sizeValue >= 0 and sizeValue <= 3) and (value >= 0 and value <=3):
    cartProductName.append(ManProducts[value])
    cartPrice.append(ManPrices[value])
    cartSize.append(sizeName[sizeValue])
    cartColor.append(colorName[colorValue])
    return
  else:
    return manfunc() 


def kidsfunc():
  KidsIndex = [1,2,3,4]
  KidsProducts = ['FLAME PRINT SWEATSHIRT', 'SPORTY CONTRAST HOODIE', 'WEEKEND FEELING SWEATSHIRT', 'KIDS/ ALPHABET BUCKET HAT']
  KidsPrices = [9.900, 9.900, 6.900, 2.500]

  for i in range(len(KidsProducts)):
    print(f'{KidsIndex[i]}: {KidsProducts[i]}, Price: OMR: {KidsPrices[i]}')
  
    
  try:
    value = int(input("Select item number that you want: "))
    value -=1
  except ValueError:
    print("You should print number")
    return kidsfunc()

  for i in range(len(sizeName)):
    print(f'{sizeIndex[i]}: {sizeName[i]}')
  try:
   sizeValue = int(input("Select color that you want: "))
   sizeValue -=1
  except ValueError:
    print("You should print number")
    return kidsfunc()

  for i in range(len(colorName)):
    print(f'{colorIndex[i]}: {colorName[i]}')
  try:
    colorValue = int(input("Select color that you want: "))
    colorValue -=1
  except ValueError:
    print("You should print number")
    return kidsfunc()

  if (colorValue >= 0 and colorValue <= 7) and (sizeValue >= 0 and sizeValue <= 3) and (value >= 0 and value <=3):
    cartProductName.append(KidsProducts[value])
    cartPrice.append(KidsPrices[value])
    cartSize.append(sizeName[sizeValue])
    cartColor.append(colorName[colorValue])
    return
  else:
    return kidsfunc() 


def beautyfunc():
  BeautyIndex = [1,2,3,4]
  BeautyProducts =  ['BLUSH - REFILLABLE', 'LIMITLESS SOFT-MATTE FOUNDATION', 'CULT SATIN', 'MULTIFUNCTIONAL PALETTE']
  BeautyPrices = [5.900, 10.900, 5.900, 22.900]

  for i in range(len(BeautyProducts)):
    print(f'{BeautyIndex[i]}: {BeautyProducts[i]}, Price: OMR: {BeautyPrices[i]}')
  
    
  try:
    value = int(input("Select item number that you want: "))
    value -=1
  except ValueError:
    print("You should print number")
    return beautyfunc()

  for i in range(len(sizeName)):
    print(f'{sizeIndex[i]}: {sizeName[i]}')
  try:
   sizeValue = int(input("Select color that you want: "))
   sizeValue -=1
  except ValueError:
    print("You should print number")
    return beautyfunc()

  for i in range(len(colorName)):
    print(f'{colorIndex[i]}: {colorName[i]}')
  try:
    colorValue = int(input("Select color that you want: "))
    colorValue -=1
  except ValueError:
    print("You should print number")
    return beautyfunc()

  if (colorValue >= 0 and colorValue <= 7) and (sizeValue >= 0 and sizeValue <= 3) and (value >= 0 and value <=3):
    cartProductName.append(BeautyProducts[value])
    cartPrice.append(BeautyPrices[value])
    cartSize.append(sizeName[sizeValue])
    cartColor.append(colorName[colorValue])
    return
  else:
     return beautyfunc()


def country():
  global countryName
  global countryValue
  
  countryName = ["Oman", "India", "UAE", "UK"]
  try:
    tempValue = int(input("Select your country\n1 = Oman\n2 = India\n3 = UAE\n4 = UK\nWrite number here:"))
    countryValue = tempValue - 1
  except ValueError:
    print("You should print number")
    return country


  if countryValue >= 0 and countryValue <= 3:
    return
  else:
    return country()
  

def gender():
  global genderName
  global genderValue
  genderName = ["Male","Female"]
  try:
    genderValue = int(input("Select Gender\n1 = Male\n2 = Female\nWrite number here:"))
    genderValue -= 1
  except ValueError:
    print("You should print number")
    return gender()

  if genderValue >= 0 and genderValue <= 1:
    return
  else:
    return gender()

global sectionName
def section():
  global sectionValue
  sectionName = ["Woman","Man","Kids","Beauty"]
  try:
    sectionValue = int(input("Select Section\n1 = Woman\n2 = Man\n3 = Kids\n4 = Beauty\nWrite number here:"))
    sectionValue -= 1
  except ValueError:
    print("You should print number")
    return section()
  if sectionValue >= 0 and sectionValue <= 3:
    return
  else:
    return section()

def joinsuctionfunc():
  if sectionValue == 0:
    womanfunc()
  elif sectionValue == 1:
    manfunc()
  elif sectionValue == 2:
    kidsfunc()
  else:
    beautyfunc()
  return
def askcontinue():
  value = input("Do you want to continue? type y for Yes, type n for No: ")
  if value == "y":
    status = "y"
    loopSysFunc(status)
  elif value == "n":
    SystemExit
  else:
    askcontinue()


def loopSysFunc(value):
  if value == "new":
    country()
  if value == "new":
    gender()
  if value == "new" or value == "y":
    section()
  if value == "new" or value == "y":
    joinsuctionfunc()
  if value == "new" or value == "y":
    askcontinue()

loopSysFunc(status)

print(f'\n\nCustomer Country: {countryName[countryValue]}\nCustomer Gender: {genderName[genderValue]}\n\n')
print("Products purchased")
for i in range(len(cartProductName)):
    print(f'{i + 1}: {cartProductName[i]}\t Price: OMR: {cartPrice[i]}\t Size: {cartSize[i]}\t Color: {cartColor[i]}')
    totalPrice += cartPrice[i]
totalPrice = format(totalPrice, '.3f')
print(f'\nTotal Price: OMR: { totalPrice }\n\n')
print("Thank you for shopping\n\n\n")