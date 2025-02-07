def viewCourses(array):
    print("The following courses are available for registration:")
    i = 1
    for item in array:
        print(i, item)
        i += 1
def addCourses(array1, array2): #bug that doesn't properly add a course
    number = int(input("Enter the course number you'd like to register for:\n"))
    array1[number - 1] = array2[number - 1]
    return array1
def removeCourses(array1, number):
    array1.remove(number - 1)
    return array1
def registration():
    availableCourses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
    userCourses = []
    print("It's time to register for classes! To view available courses type 'view'. To register type 'add'. To remove type 'remove'.")
    while True:
        choice = input("What would you like to do?\n")
        if choice == "view":
            viewCourses(availableCourses)
        elif choice == "add":
            addCourses(userCourses, availableCourses)
        elif choice == "remove":
            print("These are your current courses:\n")
            i = 1
            for item in userCourses:
                print(i, item)
                i += 1
            number = int(input("Enter the course number you'd like to remove:\n"))
            removeCourses(userCourses, number)
        else:
            print("Invalid choice.")
# ==============================================================================
def main():
    registration()
# ==============================================================================
if __name__ == "__main__":
    main()
