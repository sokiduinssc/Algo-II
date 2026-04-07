#literal
#integer
print("Tipe Data String")
print("2") #ini string
print("Tipe Data Integer")
print(2) #ini integer

#konvension tambahan pada python: octal dan hexadesimal
print("oktal")
print(0x123)
print("heksadesimal")
print(0o123)

#floats

#String
print("ini String")
print("I \'am Monty Python")
print('I \'am "Monty Python"')
print("I \'am \"Monty Python\"")

#Boolean
print("Boolean")
print(True>False)
print(True<False)

#Operator

#EXPONENTIATION
print(2**3)
print(2**3.)
print(2.**3)
print(2.**3.)

#MULTIPLICATION
print(2*3)
print(2*3.)
print(2.*3)
print(2.*3.)

#DIVISION
print(6/3)
print(6/3.)
print(6./3)
print(6./3.)

#INTEGER DIVISION (FLOOR DIVISION)
print(6//3)
print(6//3.)
print(6.//3)
print(6.//3.)

print(6//4)
print(6.//4)
print(-6//4)
print(6.//-4)

#MODULO
print( 14 % 4 )
print(12 % 4.5)

#UNARY AND BINARY OPERATORS
print(-4 + 4)
print(-4.+ 8)
print(-4 - 4)
print(4. - 8)

#OPERATORS AND THEIR BINDINGS
print(9 % 6 % 2)
print(2 ** 2 ** 3)

#OPERATORS AND PARENTHESES
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Dalam Python, urutan prioritas operator (yang relevan di sini):
# 1.Tanda kurung ( )
# 2.Modulo %
# 3.Perkalian * dan pembagian /
# 4.Floor division //


print("contoh Casting")
#casting tipe data
#merubah tipe data satu ke tipe data lainnya
# Tipe Data = integer, float, string, boolean

data_int = 9
print("data = ", data_int, ",type=", type(data_int)
      )
data_float = float(data_int)
print("data = ", data_float, "type=", type (data_float))
