from vector import Vector

column_v0 = Vector([[0.0], [1.0], [2.0], [3.0]])
row_v0 = Vector([0.0, 1.0, 2.0, 3.0])
column_v2 = Vector([[2.0], [4.0], [6.0], [8.0]])
row_v2 = Vector([2.0, 4.0, 6.0, 8.0])
m = (5, 10)
n = (5, 15)

print("============================= TEST INIT =============================")
try:
    print(">>> TEST1 Vector([1., 2e-3, 3.14, 5.]) <<<")
    print(Vector([1., 2e-3, 3.14, 5.]))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST2 Vector([1., 2e-3, None, 5.]) <<<")
    print(Vector([1., 2e-3, None, 5.]))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST3 Vector(5) <<<")
    print(Vector(5))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST4 Vector(-42) <<<")
    print(Vector(-42))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST5 Vector(0) <<<")
    print(Vector(0))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST6 Vector(42.42) <<<")
    print(Vector(42.42))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST7 Vector((21, 27)) <<<")
    print(Vector((21, 27)))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST8 Vector((10, 5)) <<<")
    print(Vector((10, 5)))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST9 Vector((5, 5)) <<<")
    print(Vector((5, 5)))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST10 Vector((4, 2.)) <<<")
    print(Vector((4, 2.)))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST11 Vector((4, 2.1)) <<<")
    print(Vector((4, 2.1)))
except ValueError:
    print("ValueError")
print("========================= TEST MUL AND RMUL =========================")
print("column_v0", repr(column_v0))
print("column_v2", repr(column_v2))
print("row_v0", repr(row_v0))
print("row_v2", repr(row_v2))
try:
    print(">>> TEST12 column_v0 * column_v2 <<<")
    print(column_v0 * column_v2)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST13 row_v0 * row_v2 <<<")
    print(row_v0 * row_v2)
except ValueError:
    print("ValueError")

try:
    print(">>> TEST14 Vector(1) * Vector(1) <<<")
    print(Vector(1) * Vector(1))
except ValueError:
    print("ValueError")
print("Vector(m)", repr(Vector(m)))
print("Vector(n)", repr(Vector(n)))
try:
    print(">>> TEST15 Vector(m) * Vector(m) <<<")
    print(Vector(m) * Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST16 Vector(m) * 2 <<<")
    print(Vector(m) * 2)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST17 2 * Vector(m) <<<")
    print(2 * Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST18 Vector(m) * None <<<")
    print(Vector(m) * None)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST19 Vector(m) * 'hello' <<<")
    print(Vector(m) * 'hello')
except ValueError:
    print("ValueError")
try:
    print(">>> TEST20 None * Vector(n) <<<")
    print(None * Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST21 'world' * Vector(m) <<<")
    print('world' * Vector(m))
except ValueError:
    print("ValueError")

print("========================= TEST ADD AND RADD =========================")
try:
    print(">>> TEST22 Vector(m) + Vector(m) <<<")
    print(Vector(m) + Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST23 Vector(1) + Vector(1) <<<")
    print(Vector(1) + Vector(1))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST24 Vector(m) + Vector(n) <<<")
    print(Vector(m) + Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST25 Vector(m) + 2 <<<")
    print(Vector(m) + 2)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST26 2 + Vector(m) <<<")
    print(2 + Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST27 Vector(m) + None <<<")
    print(Vector(m) + None)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST28 Vector(m) + 'hello' <<<")
    print(Vector(m) + "hello")
except ValueError:
    print("ValueError")
try:
    print(">>> TEST29 None + Vector(n) <<<")
    print(None + Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST30 'world' + Vector(m) <<<")
    print("world" + Vector(m))
except ValueError:
    print("ValueError")
print("========================= TEST SUB AND RSUB =========================")
try:
    print(">>> TEST31 Vector(m) - Vector(m) <<<")
    print(Vector(m) - Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST32 Vector(1) - Vector(1) <<<")
    print(Vector(1) - Vector(1))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST33 Vector(m) - Vector(n) <<<")
    print(Vector(m) - Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST34 Vector(m) - 2 <<<")
    print(Vector(m) - 2)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST35 2 - Vector(m) <<<")
    print(2 - Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST36 Vector(m) - None <<<")
    print(Vector(m) - None)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST37 Vector(m) - 'hello' <<<")
    print(Vector(m) - "hello")
except ValueError:
    print("ValueError")
try:
    print(">>> TEST38 None - Vector(n) <<<")
    print(None - Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST39 'world' - Vector(m) <<<")
    print("world" - Vector(m))
except ValueError:
    print("ValueError")
print("===================== TEST TRUEDIV AND RTRUEDIV =====================")
try:
    print(">>> TEST40 Vector(m) / 2 <<<")
    print(Vector(m) / 2)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST41 Vector(m) / 3.14 <<<")
    print(Vector(m) / 3.14)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST42 Vector(m) / 0 <<<")
    print(Vector(m) / 0)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST43 Vector(m) / Vector(m) <<<")
    print(Vector(m) / Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST44 Vector(m) / Vector(n) <<<")
    print(Vector(m) / Vector(n))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST45 Vector(m) / None <<<")
    print(Vector(m) / None)
except ValueError:
    print("ValueError")
try:
    print(">>> TEST46 None / Vector(m) <<<")
    print(None / Vector(m))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST47 2 / Vector((n, m)) <<<")
    print(2 / Vector((n, m)))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST48 2 / Vector((0, n)) <<<")
    print(2 / Vector((0, n)))
except ValueError:
    print("ValueError")
print("===================== TEST .DOT() AND .T() =====================")
try:
    print(">>> TEST49 Vector([[1.0], [2.0], [3.0]]).dot(Vector([[3.0], ",
          "[2.0], [1.0]])) <<<")
    print(Vector([[1.0], [2.0], [3.0]]).dot(Vector([[3.0], [2.0], [1.0]])))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST50 Vector([1.0, 2.0, 3.0]).dot(Vector([3.0, 2.0, 1.0]))")
    print(Vector([1.0, 2.0, 3.0]).dot(Vector([3.0, 2.0, 1.0])))
except ValueError:
    print("ValueError")
try:
    print(">>> TEST51 Vector([[2.0], [4.0], [6.0], [8.0]]).T() <<<")
    print(Vector([[2.0], [4.0], [6.0], [8.0]]).T())
except ValueError:
    print("ValueError")
try:
    print(">>> TEST52 Vector([2.0, 4.0, 6.0, 8.0]).T() <<<")
    print(Vector([2.0, 4.0, 6.0, 8.0]).T())
except ValueError:
    print("ValueError")
