#tip calculator: 
def f(g1,g2):
  f_g = int(g1)
  return f_g

print("Give me the bill amount")
g1 = input()

print("Give me the % of the tip you want to give in decimal form please")
g2 = input()

C = int(g1)*float(g2)

P = int(g1)+int(C)

print("The total amount including the tip is",P)
