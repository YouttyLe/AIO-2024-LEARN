import math

def md_nre_single_sample(y, y_hat, n, p):
  return abs(math.pow(y, 1/n) - math.pow(y_hat, 1/n)) ** p

def get_input():
  while True:
    try:
      y = float(input("y: "))
      y_hat = float(input("y_hat: "))
      n = int(input("n (integer): "))
      p = int(input("loss (integer)): "))
      if n > 0 and p > 0:
        return y, y_hat, n, p
      else:
        print("loss must be integer.")
    except ValueError:
      print("Wrong value")
y, y_hat, n, p = get_input()

result = md_nre_single_sample(y, y_hat, n, p)
print(result)