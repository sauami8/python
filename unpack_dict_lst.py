d = {"a":"Apple", "b":"Boy"}

#d["a"]="value of aA"
#print(d["a"])
#print(d)
for k,v in d.items():
    print("dict key ",k, " value is ", v)
    if d[k] =="boy":
        print("chk conditiono Boy")
    else:
        print("No matching values")

d=[1,2,3]
if type(d) is dict:
    print("Object is dictionary")
elif type(d) is list:
    print("object is list")

print("---")
obj = {"ename":["a","b","c"], "id":[10,20,30], "city":{"Address":["coppell","TX"], "Country":"US"}}
print(obj," is type of ",type(obj),"\n")
for k, v in obj.items():
    if type(v) is list:
        print(k, "is key type of list ", v)
        for vname in v:
            print("\tValue of Key ", k, " are ", vname)
    elif type(v) is dict:
        print(k, "<- type of dict-> ", v)
        for k1,v1 in v.items():
            print("\t", k1, "Nested value Key")
            if type(v1) is list:
                for v1v in v1:
                    print("\t\tVales are ", v1v)
            if type(v1) is str:
                print("\t\tvalue is str", v1)
    elif type(v) is str:
        print("\tKey is string ", k, " and value is ", v)
    elif type(v) is int:
        print("\tKey is int ", k, " and value is ", v)
    else:
        print("value is different ", v)
