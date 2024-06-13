import random
import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calculate_loss(num_samples, loss_name):
  if not is_number(num_samples):
    print("number of samples must be an integer number")
    return

  num_samples = int(num_samples)

  for number in range(num_samples):
    predict = random.uniform(0, 10)
    target = random.uniform(0, 10)
    if loss_name == "MAE":
      loss = abs(target - predict)
      print(f"loss name: {loss_name}, sample: {number}, pred: {predict: }, target: {target: }, loss: {loss: }")
    elif loss_name == "MSE":
      loss = (target - predict) ** 2
      print(f"loss name: {loss_name}, sample: {number}, pred: {predict: }, target: {target: }, loss: {loss: }")
    elif loss_name == "RMSE":
      loss = math.sqrt((target - predict) ** 2)
      print(f"loss name: {loss_name}, sample: {number}, pred: {predict: }, target: {target: }, loss: {loss: }")

num_samples = input("Input number of samples ( integer number ) which are generated: ")
loss_name = input("Input loss name (MAE, MSE, RMSE): ")

calculate_loss(num_samples, loss_name)