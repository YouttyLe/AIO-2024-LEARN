import numpy as np
# Câu hỏi 1: Câu nào sau đây là đúng để tạo mảng 1 chiều từ 0 đến 9
arr = np . arange (1 , 10 , 1)
# print(arr)
# Câu hỏi 2: Cách tạo một mảng boolean 3x3 với tất cả giá trị là True
arr1 = np . full ((3 ,3) , fill_value = True , dtype = bool )
# print(arr1)
# Câu hỏi 3: Kết quả của đoạn code sau đây:
arr2 = np.arange(0,10)
# print(arr2[arr2%2 == 1])
# Câu hỏi 4: Kết quả của đoạn code sau đây:
arr3 = np.arange(0,10)
arr3[arr3%2 == 1] = -1
# print(arr3)
# Câu hỏi 5: Kết quả của đoạn code sau đây:
arr = np . arange (10)
arr_2d = arr . reshape (2 , -1)
print ( arr_2d )
#Câu hỏi 6: Kết quả của đoạn code sau đây:
arr_1 =  np.arange(10).reshape(2,-1)
arr_2 = np.repeat(1,10).reshape(2,-1)
c = np.concatenate()
