with open('input.txt', 'r') as i:

  conteudo = i.read()

  calories = 0
  elves = []

  for line in conteudo:

    while(True):
      try:
        i_calories = input()

        if (i_calories):
          calories += int(i_calories)
          print(f'calories:  {calories}')

        if (i_calories == ''):
          elves.append(calories)
          calories = 0
      
      except EOFError:
        break


    print (f'max calories: {max(elves)}')
