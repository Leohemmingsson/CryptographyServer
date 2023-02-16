from abe_abstraction import *
from database_abstraction import DB

x = ABE(CPAc17)

x.set_policy("aaaaa")
print(x.get_policy())
