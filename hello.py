from lib import A
from anotherlib import B


name = input()
a = A(name)
b = B(name)
print(f"hello {a.data}")

print(f"hello {b}")