print("Please Introduce the pH of the substance to determine it's acid level ")

ph = int(input() )

if ph>10:
  print('acid')
elif ph>7:
  print('Basic')
else:
  print('Neutral')
