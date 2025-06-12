import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitNodes')
from Revit.Elements import *

import numpy as np

# string_0 = "Hello "
# string_1 = "Bo"

# li = [0, 1, 3, 7, 999]
# ok = list((9,9,9))
# numbers = []
# for i in range(10):
#     numbers.append(i)
# print("hello, world!")
# OUT = string_0 + string_1
# OUT = li
# OUT = ok
# OUT = numbers

col_list = []


for x in np.arange(0, 10.4, 5.3):
    famtype = IN[0]
    level = IN[1]
    pbc = Point.ByCoordinates(x,0,0)
    col = FamilyInstance.ByPointAndLevel(famtype, pbc, level)
    col_list.append(col)
    print("Hello, world!")


    print("I want to have Hrithek printed")
OUT = col_list