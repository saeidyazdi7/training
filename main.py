import mehr
import importlib
mehr.a = 5
print(mehr.a)
importlib.reload(mehr)
print(mehr.a)
