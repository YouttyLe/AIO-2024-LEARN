def sliding_window_maximum(num_list, k):
    if k < 1:
        return []
    max_values = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        max_values.append(max(window))

    return max_values

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
result = sliding_window_maximum(num_list, k)
print(result)