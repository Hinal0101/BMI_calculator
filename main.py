#calculation of BMI
def BMI(height,weight):
  bmi=float(weight/(height*height))
  if 0<bmi<1:
      print("\nBMI = {:.2f}\nSevere thinness!".format(bmi))
  elif 1<bmi<18.5:
      print("\nBMI = {:.2f}\nYou are Underweight!".format(bmi))
  elif 18.5<bmi<25:
      print("\nBMI = {:.2f}\nYou are Normal!".format(bmi))
  elif 25<bmi<30:
      print("\nBMI = {:.2f}\nYou are Overweight!".format(bmi))
  else:
      print("\nBMI = {:.2f}\nYou are Obese!".format(bmi))

#passing the weights to conversion and calculation of BMI
def units(unit_height,unit_weight,height,weight):
  height=convert_height(unit_height,height)
  weight=convert_weight(unit_weight,weight)
  print(height,weight)
  BMI(height,weight)

#conversion of height to standard units
def convert_height(unit_height,height):
  if unit_height==1:
    return height
  elif unit_height==2:
    return height/100
  elif unit_height==3:
    return height*0.3048
  elif unit_height==4:
    return height*0.0254

#conversion of weight to standard units
def convert_weight(unit_weight,weight):
  if unit_weight==1:
    return weight
  else:
    return weight/2.205

# Main program  
print("\n******** BMI Calculator **********\n")
unit_height=int(input("Select the unit of height\n(Enter the number corresponding to it)\n1.Metres (m)\n2.Centimetres (cm)\n3.Feet (ft)\n4.Inches (in)\n===> "))
if 0<unit_height<5:
  unit_weight=int(input("Select the unit of weight\n(Enter the number corresponding to it)\n1.Kilograms (kg)\n2.Pounds (p)\n===> "))
  if 0<unit_weight<3:
    height=float(input("Enter your height = "))
    weight=float(input("Enter your weight = "))
    if height>0 and weight>0:
      units(unit_height,unit_weight,height,weight)
    else:
      print("Please enter valid data!!")
  else:
    print("Please enter correct option")
else:
  print("Please enter the correct option")
  
