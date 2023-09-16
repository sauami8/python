l =[1, 2, 3, 4, 'a', 'b', 'aa', [11, 12, 13], {'name': 'Jay', 'age': 10}]

for lv in l:
    if type(lv)==str:
        print(f"'{lv} ' --> value is string")
    elif type(lv) == int:
        print(f"'{lv} ' --> value is Integer")
    elif type(lv) == dict:
        print(f"'{lv} ' --> Its dictionary")
    elif type(lv) == list:
        print(f"{lv} ' --> value is list")
    else:
        print("something else")

lst = [1, 2, 3, ['hello', 'how'], {'a': 'AA', 'b': 'BB'}, 4]

for x in lst:
    if type(x) is dict:
        for k,v in x.items():
            print("key ", k, " value is ", v)
            if type(v) is list:
                for vv in v:
                    print("List values are ", vv)
    elif type(x) is list:
        for vl in x:
            print("list value is ", vl)
    else:
        print(x)