import math

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def estimate_sin(x, n):
  estimate = 0
  for i in range(n):
    estimate += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
  return estimate

def estimate_cos(x, n):
  estimate = 0
  for i in range(n):
    estimate += ((-1)**i) * (x**(2*i)) / factorial(2*i)
  return estimate

def estimate_sinh(x, n):
  estimate = 0
  for i in range(n):
    estimate += (x**(2*i+1)) / factorial(2*i+1)
  return estimate

def estimate_cosh(x, n):
  estimate = 0
  for i in range(n):
    estimate += (x**(2*i)) / factorial(2*i)
  return estimate

def get_input():
  while True:
    try:
      x = float(input("Enter x (radian): "))
      n = int(input("Enter n (integer): "))
      if n > 0:
        return x, n
      else:
        print("n must be int")
    except ValueError:
      print("wrong value.")

x, n = get_input()

sin_result = estimate_sin(x, n)
cos_result = estimate_cos(x, n)
sinh_result = estimate_sinh(x, n)
cosh_result = estimate_cosh(x, n)
print(f"sin({x:}) ≈ {sin_result: .4f}")
print(f"cos({x:}) ≈ {cos_result: .4f}")
print(f"sinh({x:}) ≈ {sinh_result: .2f}")
print(f"cosh({x:}) ≈ {cosh_result: .2f}")