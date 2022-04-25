def factendzero(num):
  x = num  // 5
  y = x 
  while x > 0:
    x /= 5
    y += int(x)
  return y


fac_input = input("INPUT - FACT : ")
num = int(fac_input)
print(factendzero(num))

