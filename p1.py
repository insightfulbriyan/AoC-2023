with open("input.txt", 'r') as f:
  f = f.read().split('\n')
  numbers = []
  for line_in in range(len(f)):
    line = f[line_in]
    for char_in in range(len(line)-3):
      serial = line[char_in:char_in+3]
      if serial[-1] not in '0123456789':
        continue
      if serial[1] not in '0123456789':
        continue
      #print(serial, serial[1])
      
      if serial[0] not in '0123456789':
        serial = serial[1:3]
        try:
          if f[line_in][char_in + 3] in '0123456789':
            continue
        except IndexError:
          neki = 10
        for dl, dc in [(-1, 0), (-1, 1), (-1, 2),(-1, 3),(0, 0),(0, 3), (1, 0),(1, 1), (1, 2), (1, 3)]:
          try:
            x = char_in + dc
            y = line_in + dl 
            #print(x,y,len(line),len(f))
            if f[y][x] not in '1234567890.':
                try:
                  numbers.append(int(serial))
                except ValueError:
                  print(serial)
          except IndexError:
            continue
        continue
      for dl, dc in [(-1, -1), (-1, 0), (-1, 1), (-1, 2), (-1, 3), (0, -1), (0, 3), (1, -1), (1, 0), (1, 1), (1, 2), (1, 3)]:
        try:
          x = char_in + dc
          y = line_in + dl
          if f[y][x] not in '1234567890.':
            try:
              numbers.append(int(serial))
            except ValueError:
              print(serial)
        except IndexError:
          continue
  sum = 0
  for i in numbers:
    sum += i
  print(sum)