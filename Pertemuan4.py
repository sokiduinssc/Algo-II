#FUNGSI INPUT( )
#FUNGSI INPUT( ) DENGAN ARGUMEN
print("#Fungsi Input dengan argumen")
print( "Katakan apapun yang anda Inginkan ...")
apapun = input()
print("hmmmmm...", apapun, "benarkah")

#TYPE CONVERSIONS-1
print("#TYPE CONVERSIONS-1")
anything = float(input("Enter a number : "))
something = anything ** 2.0
print(anything, "to the power of is", something)

#TYPE CONVERSIONS-2
print("#TYPE CONVERSIONS-2")
leg_a = float (input("input first leg lenght:"))
leg_b = float (input("input second leg lenght:"))
hypo = (leg_a **2 +leg_b **2) ** 5
print ( "Hypotenuse length is", hypo)

#OPERATOR-OPERATOR STRING
#operator Konkatenasi
print("#Operator Konkatenasi")
fnam = input ("May I Have your first name, please?: ")
lnam = input ("May I Have your last name, please?: ")
print("thak you.")
print("\nYour name is " + fnam +" " + lnam + " ")

#operator replikasi
print("#operator replikasi")
print("+" +10* "-" + "+")
print(("|" + "" *10 + "|\n") * 5, end="")
print("+" +10* "-" + "+")

#TYPE CONVERSIONS-3
print("#TYPE CONVERSIONS-3")
x = input("Enter a number :")
print(type(x))
