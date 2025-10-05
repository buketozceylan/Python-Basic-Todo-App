from unittest import case

todos =[]

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)

        case "edit":
            for item in todos:
                print(item)
            index = int(input("Enter an option number You want to edit: "))
            index = index - 1
            new_todo = input("Enter new to do: ")
            todos[index] = new_todo
            for item in todos:
                print(item)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            print("Thank you! Bye!")
            break

