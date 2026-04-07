# Comparison Operators
print("Comparison Operators")

x = 0
y = 1
z = 0

print("x == y :", x == y)   # False
print("x == z :", x == z)   # True
print("x != y :", x != y)   # True
print("x > y  :", x > y)    # False
print("x < y  :", x < y)    # True
print("x >= z :", x >= z)   # True
print("x <= y :", x <= y)   # True


# A If tunggal
print("A. If tunggal")

nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")


# If - Else
print("B. If - Else")

nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")

# If - Elif - Else
print("B. If - Else")

nilai = int(input("Masukkan nilai: "))

if nilai >= 85:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
elif nilai >= 65:
    print("Grade C")
else:
    print("Grade D")

    