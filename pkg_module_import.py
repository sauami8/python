
# two way to import package file folder.module
from pkg import modulefile as mf
# import pkg.modulefile as mf

mf.SayHello()

# combine package tree with dot and than import module
from pkg.p2 import p2hello as p

print(p.p2list)