def addingNums():
    add_num = []
    for i in range(5):
        num_q = float(input("Enter a number: "))
        add_num.append(num_q)
    adding_all_nums = sum(add_num)
    print("The total is ", adding_all_nums, ".", sep='')

addingNums()