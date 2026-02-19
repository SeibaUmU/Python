import numpy as np
def BT1():
    arr_a = np.array([1,2,3,2,3,4,3,4,5,6])
    arr_b = np.array([7,2,10,2,7,4,9,4,9,8])
    #arr_c = np.extract(np.isin(arr_a, arr_b), arr_a)
    arr_c =np.array([], dtype=np.int32)
    for i in arr_a:
         if i in arr_b  and i in arr_a and i not in arr_c:
              arr_c = np.append(arr_c, i)

    print(arr_c)

    arr_d =np.array([], dtype=np.int32)
    for i in arr_a:
            if i not in arr_b and i not in arr_d:
                arr_d = np.append(arr_d, i)
    print(arr_d)

    arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])
    arr_f = np.extract((arr_e >= 5) & (arr_e<=10), arr_e)
    # for i in arr_e:
    #     if i >=5 and i<=10:
    #         arr_f = np.append(arr_f, i)
    print(arr_f)

def BT2():
    arr_zeros = np.zeros([10], dtype= int)
    arr_zeros[5] = 1
    print(arr_zeros)

    arr_h = np.arange(10, 25, 1)
    print(np.sort(arr_h)[::-1]) 

    arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
    arr_1 = np.extract(arr_k != 0, arr_k)
    print(arr_1)

    arr_2 = np.append(arr_1, [10, 20])
    print(arr_2)

    arr_3 = np.insert(arr_1, 5, [100])
    print(arr_3)

    arr_4 = np.delete(arr_3, slice(0, 3))
    print(arr_4)

def BT3():
    arr = np.ones([3,3], dtype= int)
    print(arr)

    arr_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    arr_2D = arr_1D.reshape(3, 3)
    print(arr_2D)
    arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]] #dong lay het, cot 0 2
    print("\nSau khi hoán đổi cột 1 và 3:")
    print(arr_2D)

    arr_2D[[0, 1], :] = arr_2D[[1, 0], :] #cot lay het, dong 0 1
    print("\nSau khi hoán đổi dòng 1 và 2:")
    print(arr_2D)

    arr_2D[:, :] = arr_2D[::-1, :] #dao nguoc ma tran
    print("\nSau khi đảo ngược dòng ma trận:")
    print(arr_2D)

    arr_2D[:, :] = arr_2D[:, ::-1] #dao nguoc tung cot
    print("\nSau khi đảo ngược cột ma trận:")
    print(arr_2D)   

    arr_2D_null = np.array([[1, 2, 3], [np.nan, 5, 6], [7, np.nan, 9], [4, 5, 6]], dtype=float)
    find = np.isnan(arr_2D_null)
    if np.any(find):
        print("\nMa trận arr_2D_null có phần tử NaN")
    else:
        print("\nMa trận arr_2D_null không có phần tử NaN")
    arr_2D_null = np.nan_to_num(arr_2D_null, nan=0)
    print("\nMa trận arr_2D_null sau khi thay thế NaN bằng 0:")
    print(arr_2D_null)


choice = int(input("BT so: "))
match choice:
    case 1:
        BT1()
    case 2:
        BT2()
    case 3:
        BT3()
    case _:
        print("fuck u")