def total(a=5,*numbers,**phonebook):
    print('a',a)

    #通过元组遍历全部的参数
    for item in numbers:
        print('num_item',item)

    #通过字典遍历全部的参数   
    for first,second in  phonebook.items():
        print(first,second)

total(10,1,2,3,Name='zhuly',age=26)
