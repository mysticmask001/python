# object oriented programming
# class = blueprint
# object = contents of class

# class People:
#     def __init__(self):
#         self.name = "Phil"
#         self.age = 18
#         self.gender = "Male"
#         self.nationality = "Kenyan"
#
#
# person1 = People("John", 19)
# person2 = People("Felicity", 18)
# portfolio = People()
#
# # reassigned
# portfolio.name = "Tyla"
# portfolio.age = 19
# portfolio.gender = "Female"
# portfolio.nationality = "South African"
#
# print(portfolio.name)
# print(portfolio.age)
# print(portfolio.gender)
# print(portfolio.nationality)



class People:
    def __init__(self, name, age, gender, nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality


person1 = People("John", 19, "Male", "Swiss")
person2 = People("Felicity", 18, "Female", "Russian")

print(person2.name, person2.age, person2.gender, person2.nationality)
print(person1.name, person1.age, person1.gender, person1.nationality)



