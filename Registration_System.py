def viewCourses(array):
    i = 1
    for item in array:
        print(i, item)
        i += 1
def addCourses(array1, array2):
    number = int(input("Enter the course number you'd like to register for:\n"))
    array1.append(array2[number - 1])
    return array1
def removeCourses(array1):
    print("These are your current courses:")
    i = 1
    for item in array1:
        print(i, item)
        i += 1
    number = int(input("Enter the course number you'd like to remove:\n"))
    array1.remove(array1[number - 1])
    return array1


# ==============================================================================
def main():
    availableCourses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
    userCourses = []
    print(
        "It's time to register for classes! To view available courses type 'courses'. To register type 'add'. To remove type 'remove'. To see your current courses type 'view'. To quit type 'quit'.")
    while True:
        choice = input("What would you like to do?\n")
        if choice == "courses":
            print("The following courses are available for registration:")
            viewCourses(availableCourses)


        elif choice == "add":
            if len(userCourses) < 3:
                print("Here are the available courses:")
                viewCourses(availableCourses)
                addCourses(userCourses, availableCourses)
            else:
                print("You can only have 3 courses")

        elif choice == "remove":
            removeCourses(userCourses)

        elif choice == "view":
            if len(userCourses) == 0:
                print("You have no courses!")
            else:
                viewCourses(userCourses)
        elif choice == "quit":
            break
        else:
            print("Invalid choice.")
# ==============================================================================
if __name__ == "__main__":
    main()
