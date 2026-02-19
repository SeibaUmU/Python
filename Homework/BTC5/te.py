# import numpy as np
# import pandas as pd

# arr1 = np.array([1, 2, 3])
# ser1 = pd.Series(arr1)
# ser1[3] = 4
# print(ser1)
# ser2 = pd.Series(ser1, copy=True)
# ser2[0] = 100
# print(ser1)
# print(ser2)

# try:    
#     age = int(input("Enter the age:"))    
#     if(age < 18):    
#         raise ValueError   
#     else:    
#         print("the age is valid") 
#     print("hellp")   
# except ValueError:    
#     print("The age is not valid")
# #neu co error phatsinh du error dc xuli r di nx thi nhung cmd tiep theo sau ngoai lenh nay se ko chay dc

# try:
#     age = int(input("Enter the age:"))   # nhập và ép kiểu số nguyên
#     if age < 18:                         # nếu nhỏ hơn 18
#         print("The age is not valid")    # in lỗi trực tiếp
#     else:
#         print("The age is valid")        # hợp lệ
#     print("hello")                       # in hello
# except ValueError:                       # nếu nhập không phải số
#     print("The age is not valid 2")

# # ser1 và ser2
# ser1 = pd.Series([2, 4, 6, 8, 10])
# ser2 = pd.Series([1, 3, 5, 7, 11, 6, 12])

# # Cách 1: dùng set ^ (symmetric difference) toan tu hieu doi xung
# ser5 = pd.Series(list(set(ser1) ^ set(ser2)))
# #dung set de loai bo phan tu trung lap
# #^ de lam hieu doi xung cua set: lay nhung cai ko co trong ca 2 set, chi lay nhung cai chi co trong 1 set 1 or 2, tuc ko lay phan giao, tra ve 1 set chua gt ko trung lap
# #ep kieu lai thanh list de truyen vao Series, vi series ko chap nhan set
# #pd.Series() cần một sequence có thứ tự (list, tuple, numpy array, …) để gán index 0,1,2…
# print("ser1:\n", ser1)
# print("ser2:\n", ser2)
# print("\nser5 (các phần tử chỉ có trong ser1 hoặc ser2):\n", ser5)

# try:    
#     fileptr = open("file2.txt","r")      
#     try:    
#         fileptr.write("Hi I am good")    
#     finally:    
#         fileptr.close()    
#         print("file closed")    
# except:    
#     print("Error")

# try:
# #this will throw an exception if the file doesn't exist.
#     fileptr = open("file2.txt","r")
#     a=2/1
#     b=3/0
# except IOError:
#     print("File not found")
# except ArithmeticError:
#     print("chia cho 0")
# else:
#     print("The file opened successfully")
# print("hello") #neu ko co except nao dc xli thi khoi nay se ko chay dc, vd neu them c = int("a") thi se ko chay dc
# #th1: ko file, th2: chia 0, th3: ko co except io or arith dc xli    

try:
    num = int(input("Enter a positive integer: ")) #no kphai ep kieu ma la quy dinh kieu
    if num <= 0:
        raise Exception("Non-positive integer")

except ValueError:
    # Lỗi ép kiểu int
    print("Error: Input must be an integer")

except Exception as e:
    # Lỗi do mình raise
    print("Error:", e)
# cach fix bai tren
try:
    raw = input("Enter a positive integer: ")

    # Thử parse float trước
    num_float = float(raw)

    # Nếu là số thực nhưng không phải số nguyên
    if not num_float.is_integer():
        raise ValueError("FLOAT")   # gắn nhãn lỗi riêng

    num = int(num_float)

    # Kiểm tra số nguyên có dương không
    if num <= 0:
        raise Exception("Non-positive integer")

    print("OK:", num)

except ValueError as e:
    if str(e) == "FLOAT":
        print("Error: Input must be an integer, not a float")
    else:
        print("Error: Input must be an integer (not letters or symbols)")
except Exception as e:
    print("Error:", e)
