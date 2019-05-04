from statistics import mean as m

admins={'python':'#pass12', 'python12':'@psw12'}
studentDic={'Shwetha':[85,64,89],'Lava':[75,62,89],'Sam':[68,78,95]}

def gradesEnter():
    studentName=input("Student name: ")
    if studentName in studentDic:
        grade=(input('Grade: '))
        studentDic[studentName].append(float(grade))
        print(studentDic)
    else:
        print('Student {} does not exist'.format(studentName))

def removeStudent():
    nameToRemove=input('Student name to remove: ')
    if nameToRemove in studentDic:
        del studentDic[nameToRemove]
        print(studentDic)
    else:
        print('Student {} does not exist'.format(nameToRemove))

def calculateAvgs():
    for eachStudent in studentDic:
        gradeList=studentDic[eachStudent]
        avgGrade=m(gradeList)
        print(eachStudent,'Average Grade = ',avgGrade)

def addStudent():
    addName=input('Enter the Student name: ')
    if addName in studentDic:
        print('Student {} is already exist'.format(addName))
    else:
        grades = int(input('Enter the grade: '))
        studentDic.update({addName:grades})
    print(studentDic)

def main():
    print("""
    [1] - Enter the grades of the student
    [2] - Removing a student from the system
    [3] - Calculating the average grades of students
    [4] - Adding a new Student
    [5] - Exit
    """)
    action = int(input("What option do you want to perform? "))
    if action == 1:
        gradesEnter()
    elif action == 2:
        removeStudent()
    elif action == 3:
        calculateAvgs()
    elif action == 4:
        addStudent()
    else:
        print('Invalid option selected. Please try again')
        exit()


login = input('Username: ')
password=input('Password: ')

if login in admins:
    if admins[login]==password:
        print('Welcome, ',login)
        while True:
            main()
    else:
        print('Invalid Password')
else:
    print('Invalid Username')
