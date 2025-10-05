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
            for i, item in enumerate(todos):
                print(i+1, "- " + item)
            index = int(input("Enter an option number You want to edit: "))
            index = index - 1
            new_todo = input("Enter new to do: ")
            todos[index] = new_todo
            for i, item in enumerate(todos):
                print(i+1, "- " + item)
        case "show":
            for i, item in enumerate(todos):
                print(i+1, "- " + item)
        case "exit":
            print("Thank you! Bye!")
            break

