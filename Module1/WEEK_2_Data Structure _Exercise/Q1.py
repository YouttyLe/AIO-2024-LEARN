def sliding_window_max(num_list, k):
  n = len(num_list)
  if k <= 1 or k > n:
    return []
  max_values = []
  for i in range(n - k + 1):
    window = num_list[i:i + k]
    max_value = max(window)
    max_values.append(max_value)
  return max_values
def main():
    num_list_str = input("Enter list integer: ")
    num_list = [int(x) for x in num_list_str.split()]
    k = int(input("Enter k: "))
    max_values = sliding_window_max(num_list, k)
    print(max_values)

  
if __name__ == '__main__':
    main()