def ToDoList():
#Neil has edit this file
#Louis also yeah
    print(
        "This is a simple to do list. To add a new item, enter 'add'. To remove an item, enter 'remove'. To see all items, enter 'list'.")
    taskList = []
    while True:
        command = input("What would you like to do?\n")
        while True:
            if command == "add":
                add = input("What would you like to add?\n")
                taskList.append(add)
                break
            elif command == "remove":
                i = 1
                for item in taskList:
                    print(i, item)
                    i += 1
                remove = int(input("Which numbered task would you like to remove?\n"))
                taskList.remove(taskList[remove - 1])
                break
            elif command == "list":
                i = 1
                for item in taskList:
                    print(i, item)
                    i += 1
                break
            elif command != "add" or command != "remove" or command != "list":
                print("Invalid input. Please enter 'add', 'remove' or 'list'.")
                break
# ==============================================================================
def main():
    ToDoList()
# ==============================================================================
if __name__ == "__main__":
    main()




