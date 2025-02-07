def ToDoList():
    command1 = "add"
    command2 = "remove"
    command3 = "list"
    print(
        "This is a simple to do list. To add a new item, enter 'add'. To remove an item, enter 'remove'. To see all items, enter 'list'.")
    taskList = []
    while True:
        command = str(input("What would you like to do?\n"))
        while True:
            if command == command1:
                add = input("What would you like to add?\n")
                taskList.append(add)
                break
            elif command == command2:
                i = 1
                for item in taskList:
                    print(i, item)
                    i += 1
                remove = int(input("Which numbered task would you like to remove?\n"))
                taskList.remove(taskList[remove - 1])
                break
            elif command == command3:
                i = 1
                for item in taskList:
                    print(i, item)
                    i += 1
                break
            elif command != command1 or command != command2 or command != command3:
                print("Invalid input. Please enter 'add', 'remove' or 'list'.")
                break
# ==============================================================================
def main():
    ToDoList()
# ==============================================================================
if __name__ == "__main__":
    main()



