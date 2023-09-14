#Degree calculator: 
def f(x):
  f_g = int(x)
  return f_g

print("Give me the degrees in celcius and I will give you the degrees in Farenheit and Kelvin")
x = input()

g1 = int(x)*float(1.8)+32
g2 = int(x)+273.15
print("Your answer is",g1,"and",g2)
f(x)
