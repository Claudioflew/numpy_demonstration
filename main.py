import numpy as np

def main():
  func_table = [
    maxMinArr,
    maxMinRow,
    maxMinCol,
    meanArr,
    meanRow,
    meanCol,
    medArr,
    medRow,
    medCol,
    displayNice
  ]

  arr = np.random.randint(0, 100, (7, 7))
  displayNice(arr)

  choice = chooseMenu()
  while choice:
    func_table[int(choice)-1](arr)
    choice = input("\nPlease enter your choice if you want to cotinue, press 'D' to display the menu again, or hit Return to quit: ")
    if choice.lower() == "d":
      choice = chooseMenu()
    
def chooseMenu():
  choice = input("""
***2D Array Manupilation Menu***

\t1) Find max and min of the array
\t2) Find max and min of each row
\t3) Find max and min of each column
\t4) Calculate mean of all values in the array
\t5) Calculate mean of each row
\t6) Calculate mean of each column
\t7) Find median of the array
\t8) Find median of each row
\t9) Find median of each column
\t10) Display the array again

Please enter your choice here: """)

  choices = [str(i) for i in range(1, 11)]
  while choice not in choices:
    choice = input("\nInvalid entry... Please enter an integer from 1 to 10: ")

  return choice

def maxMinArr(arr):
  lArr = arr.flatten()
  max = lArr.max()
  min = lArr.min()
  print(f"\nThe Array's Max: {max}, Min: {min}")

def maxMinRow(arr):
  print("\n       Max  Min")
  # for i in range(len(arr)):
  #   max = arr[i, :].max()
  #   min = arr[i, :].min()
  #   print("Row {0}: {1:3}  {2:3}".format(i+1, max, min))

  maxList = arr.max(axis=1)
  minList = arr.min(axis=1)
  ind = 1
  for max, min in zip(maxList, minList):
    print("Row {0}: {1:3}  {2:3}".format(ind, max, min))
    ind += 1

def maxMinCol(arr):
  print("\n       Max  Min")
  # for i in range(len(arr[0])):
  #   max = arr[:, i].max()
  #   min = arr[:, i].min()
  #   print("Col {0}: {1:3}  {2:3}".format(i+1, max, min))

  maxList = arr.max(axis=0)
  minList = arr.min(axis=0)
  ind = 1
  for max, min in zip(maxList, minList):
    print("Col {0}: {1:3}  {2:3}".format(ind, max, min))
    ind += 1

def meanArr(arr):
  sum = arr.sum()
  mean = sum / arr.size
  print(f"\nThe Array's Mean: {round(mean, 2)}")

def meanRow(arr):
  print("\n         Mean")
  for i in range(len(arr)):
    sum = arr[i, :].sum()
    mean = sum / len(arr[0])
    print("Row {0}:  {1:5}".format(i+1, round(mean, 2)))

def meanCol(arr):
  print("\n         Mean")
  for i in range(len(arr[0])):
    sum = arr[:, i].sum()
    mean = sum / len(arr)
    print("Col {0}:  {1:5}".format(i+1, round(mean, 2)))

def medArr(arr):
  lArr = np.sort(arr, axis=None)
  num = arr.size
  if num % 2 == 0:
    med = (lArr[int(num/2)-1] + lArr[int(num/2)]) / 2
    print(f"\nThe Array's Median: {round(med, 2)}")
  else:
    med = lArr[num//2]
    print(f"\nThe Array's Median: {med}")

def medRow(arr):
  print("\n       Median")
  lArr = np.sort(arr)
  num = len(arr[0])
  if num % 2 == 0:
    for i in range(len(arr)):
      med = (lArr[i, int(num/2)-1] + lArr[i, int(num/2)]) / 2
      print("Row {0}: {1:6}".format(i+1, round(med, 2)))
  else:
    for i in range(len(arr)):
      med = lArr[i, num//2]
      print("Row {0}: {1:6}".format(i+1, med))
      
def medCol(arr):
  print("\n       Median")
  lArr = np.sort(arr, axis=0)
  num = len(arr)
  if num % 2 == 0:
    for i in range(len(arr[0])):
      med = (lArr[int(num/2)-1, i] + lArr[int(num/2), i]) / 2
      print("Col {0}: {1:6}".format(i+1, round(med, 2)))
  else:
    for i in range(len(arr[0])):
      med = lArr[num//2, i]
      print("Col {0}: {1:6}".format(i+1, med))

def displayNice(arr):
  s = str(arr)
  s = s.replace("[", "")
  s = s.replace("]", "")
  s = "\nYour current array:\n\n " + s
  print(s)

if __name__ == "__main__":
  main()
