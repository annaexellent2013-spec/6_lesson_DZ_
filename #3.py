file_path = input("Введіть шлях до файлу: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("Вміст файлу: ")
        print(content)
except FileNotFoundError:
    print(f"Файл за шляхом '{file_path}' не існує.")