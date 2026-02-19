def bt16():
    fruit = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grapes", "dragon", "lemon"}
    print(fruit)
    check = str(input("Pick the fruit u wanna check bru: "))
    if check in fruit:
        print("Yes")
    else:
        print("No")
    return fruit
def bt17():
    fruit.update(["pineapple", "papaya", "lime", "lychee", "longan"])
    print(fruit)

def bt18():
    fruit1 = {"apple", "banana", "cherry", "orange", "kiwi"}
    fruit2 = {"melon", "mango", "grapes", "dragon", "lemon"}
    price = {"apple": 10, "banana":20, "cherry":30, "orange":40, "kiwi":50, "melon":60, "mango":70, "grapes":80, "dragon":90, "lemon":100 }
    name = str(input("Pick the fruit u wanna search bru: "))
    if name in fruit1:
        print(f"{name} in set1. Price: {price[name]}")
    elif name in fruit2:
        print(f"{name} in set2. Price: {price[name]}")
    fruit3 = fruit1.union(fruit2)
    print(fruit3)

def bt19():
    fruit1 = {"apple", "banana", "cherry", "orange", "kiwi", "rambutan"}
    fruit2 = {"melon", "mango", "grapes", "dragon", "lemon", "rambutan"}
    #+ Tìm phần giống nhau giữa hai set này và xuất ra màn hình
    fruit3 = fruit1.intersection(fruit2)
    print(fruit3)
    # + Tìm phần set 1 khác set 2 và xuất ra màn hình
    fruit4 = fruit1.difference(fruit2)
    print(fruit4)
    # + Tìm phần set 2 khác set 1 và xuất ra màn hình
    fruit5 = fruit2.difference(fruit1)
    print(fruit5)
    # + Xuất ra màn hình set tổ hợp cả hai bộ set trái cây
    fruit6 = fruit1.union(fruit2)
    print(fruit6)
    # +Xuất ra màn hình set 1 có thêm phần khác từ set 2
    test = list(fruit2)
    print(test[0])
    fruit7 = fruit1.update(test[0])
    print(fruit7)
    # +Xuất ra màn hình set 2 có thêm phần khác từ set 1
    test2 = list(fruit1)
    fruit8 = fruit2.update(test2[0])
    print(fruit8)
choice = int(input("BT so: "))
match choice:
    case 16:
        bt16()
    case 17:
        fruit = bt16()
        bt17()
    case 18:
        bt18()
    case 19:
        bt19()
    case _:
        print("dumb")