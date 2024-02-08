print("Grades Calculator")

name = input("Enter your name: ")
school = input("Enter name of school: ")
age = input("Age: ")


maths = int(input("Maths: "))
eng = int(input("English: "))
phyc = int(input("Physics: "))
kisw = int(input("Kiswahili: "))
his = int(input("History: "))

# 0-39 E
# 40-50 D
# 51-60 C
# 61-70 B
# 79-100 A

average = ((maths + eng + phyc + kisw + his) / 5)
print(f"Mean = {average}")

if maths > 100 and eng > 100 and phyc > 100 and kisw > 100 and his > 100:
    print("Invalid")

elif maths < 0 and eng < 0 and phyc < 0 and kisw < 0 and his < 0:
    print("Invalid")

elif average > 78:
    print("Grade = A")

elif average > 60:
    print("Grade = B")

elif average > 50 :
    print("Grade = C")

elif average > 39:
    print("Grade = D")

else:
    print("Grade = E")


