try:
    num_str = float(input("Введіть число: "))
    num_int = int(num_str)
    print(f"Введене число у вигляді цілого: {num_int}")
except:
    print(f"Помилка: введені дані не можливо перетворити на ціле число")