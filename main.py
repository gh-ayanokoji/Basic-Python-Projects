class Student:

    def __init__(self, name, rollno, year):
        self.name = name
        self.rollno = rollno
        self.year = year

    def accept(self, n, r, y):
        obj = Student(n, r ,y)
        ls.append(obj)

    def display(self, obj):
        print(f"\nName : {obj.name}\nRoll No.:{obj.rollno}\nYear : {obj.year}\n")

    def search(self, rn):
        for i in range(ls.__len__()):
            if ls[i].rollno == rn:
                print("\nStudent is Found!!")
                print(f"\nName : {ls[i].name}\nRoll No.:{ls[i].rollno}\nYear : {ls[i].year}\n")
            else:
                print("\nStudent not Found")
                

    def delete(self, rn):
        for i in range(ls.__len__()):
            if ls[i].rollno == rn:
                del ls[i]

ls = []

admin = Student('',0,0)
run = 1

print("Welcome to Student Management System")
while run != 0:
    print("")
    print("What Would you like to do?")
    print("1. Add a Student to the local Database")
    print("2. Display the data of all Students")
    print("3. Search for a Student")
    print("4. Delete the Information of a Student")
    print("0. Quit")
    std = int(input("Your Answer: "))

    if std == 1:
        n = input("Enter the name of Student: ")
        r = int(input("Enter the Roll No. of Student: "))
        y = int(input("Enter the Year of Student: "))
        admin.accept(n,r,y)
        print("Student Successfully Added!!")

    elif std == 2:
        for i in range(ls.__len__()):
            admin.display(ls[i])

    elif std == 3:
        rn = int(input("Enter the Roll No. of Student to be Searched: "))
        admin.search(rn)

    elif std == 4:
        rn = int(input("Enter the Roll No. of Student to be deleted: "))
        admin.delete(rn)
        print("\nStudent was Deleted Successfully!!")

    elif std == 0:
        run = 0

    else:
        print("Please Enter a Valid Input!")
        
