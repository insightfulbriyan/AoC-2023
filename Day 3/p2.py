with open('test.txt', 'r') as f:
  f = f.read().split('\n')
  stars = []
  for line_in in range(len(f)):
    line = f[line_in]
    for char_in in range(len(line)):
      if line[char_in] == '*':
        stars.append((line_in, char_in))
        
  numbers = []
  line_in = 0
  while line_in < len(f):
    char_in = 0
    line = f[line_in]
    while char_in < len(line)-1:
      char = line[char_in]
      if char.isnumeric():
        try:
          if not line[char_in+2].isnumeric():
            raise IndexError('no repeating code')
          else:
            numbers.append((line_in, char_in, 3))
            char_in += 2
        except IndexError:
          numbers.append((line_in, char_in, 2))
          char_in += 1
          pass
      char_in += 1
    line_in += 1
    
    
  #print(stars)
  #print(numbers)
  numarray = []
  for star_in in range(len(stars)):
    temp=[]
    line_in, char_in = stars[star_in]
    for off_c, off_l in [(-3, -1), (-3, 0), (-3, 1), (-2, -1), (-2, 1), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
      if (line_in + off_l, char_in + off_c, 3) in numbers:
        temp.append(
          f[line_in+off_l][char_in+off_c:char_in+off_c+3])
    numarray.append(temp)
  
    for off_c, off_l in [(-2, -1), (-2, 0), (-2, 1), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
      if (line_in + off_l, char_in + off_c, 2) in numbers:
        temp.append(f[line_in+off_l][char_in+off_c:char_in+off_c+2])
    
  print(numarray)
   
   
  sum = 0
  for nimamvecimen in numarray:
    if len(nimamvecimen) != 2:
      continue
    try:
      sum += int(nimamvecimen[0])*int(nimamvecimen[1])
    except ValueError:
      continue
  print(sum)