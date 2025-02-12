#uses to view courses
def viewCourses(array):
    #iterates through each item in the list, printing them out
    for i in range(len(array)):
        print(i+1, array[i])


def addCourses(array1, array2):
    #ask the user for which course to add
    try:
        number = int(input("Enter the course number you'd like to register for:\n"))
        array1.append(array2[number - 1])
        return array1
    #if the user doesn't put a number, then the error pops up
    #uses except and then asks the user again
    except ValueError:
        print("Please enter a number.")
        addCourses(array1, array2)
    #if the course is out of range, it asks the user again
    except IndexError:
        print("The course number you entered is out of range")
        addCourses(array1, array2)


def removeCourses(array1):
    #shows the courses that could be remove
    print("These are your current courses:")
    #shows the course to remove
    viewCourses(array1)
    #asks for the course to remove
    try:
        number = int(input("Enter the course number you'd like to remove:\n"))
        array1.remove(array1[number - 1])
        return array1
    #if the user enters a number outside the range ask the user again
    except IndexError:
        print("You aren't enrolled for that course.")
        removeCourses(array1)
    #if the user enters somthing other than a number, ask again
    except ValueError:
        print("Please enter a number.")
        removeCourses(array1)


# ==============================================================================
def main():
    #creates list to store data
    availableCourses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
    userCourses = []
    print("It's time to register for classes!")
    #loop through the functions that the user can do
    while True:
        print(
            "To view available courses type 'courses'. To register type 'add'. To remove type 'remove'. To see your current courses type 'view'. To quit type 'quit'.")
        #ask user what to do
        choice = input("What would you like to do?\n")
        #these if statements check what the user asked to do and then runs the corresponding function
        #to see all courses
        if choice == "courses":
            print("The following courses are available for registration:")
            viewCourses(availableCourses)


        elif choice == "add":
            #checks if the user hsa reach the max amount of courses
            if len(userCourses) < 3:
                print("Here are the available courses:")
                #shows the courses to add
                viewCourses(availableCourses)
                #call the add course function
                addCourses(userCourses, availableCourses)
                print("Course added!")

            else:
                print("You can only have 3 courses")

        elif choice == "remove":
            #checks if user can even remove a course, if they can it calls the remove function
            if len(userCourses) == 0:
                print("You have no courses!")
            else:
                removeCourses(userCourses)
                print("Course removed!")
        #call the view function to see what course user already has added
        elif choice == "view":
            if len(userCourses) == 0:
                print("You have no courses!")
            else:
                viewCourses(userCourses)
        #if the user wants to quit
        elif choice == "quit":
            break
        #if the user inputs a invalid choice
        else:
            print("Invalid choice.")


# ==============================================================================
if __name__ == "__main__":
    main()
