pages = int(input('Kiek knygoje puslapiu?..'))

def digits(puslapiai):
  if puslapiai < 10:
    return 1
  elif puslapiai < 100:
    return 2
  elif puslapiai < 1000:
    return 3
  elif puslapiai < 10000:
    return 4
  elif puslapiai < 100000:
    return 5
  elif puslapiai < 1000000:
    return 6
  else:
    return 7

def total(pages):
  totaliai = 0
  for puslapiai in range(1, pages + 1):
    totaliai += digits(puslapiai)
  return totaliai

totaliai = total(pages)
print(f"Knygoje su {pages} puslapiu prireiks {totaliai} skaitmenu.")


