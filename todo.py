# To-Do List Manager
def display_menu():
    print("\n=== To-Do List Manager ===")
    print("1. Показать список задач")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Очистить список")
    print("5. Выход")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Введите новую задачу: ").strip()
    if task:
        tasks.append(task)
        print(f"Задача '{task}' добавлена.")
    else:
        print("Ошибка: задача не может быть пустой.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Задача '{removed_task}' удалена.")
        else:
            print("Ошибка: неверный номер задачи.")
    except ValueError:
        print("Ошибка: введите число.")

def clear_tasks(tasks):
    if tasks:
        tasks.clear()
        print("Список задач очищен.")
    else:
        print("Список уже пуст.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            clear_tasks(tasks)
        elif choice == "5":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Ошибка: неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
