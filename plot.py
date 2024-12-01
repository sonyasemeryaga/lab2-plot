import matplotlib.pyplot as plt
import os

# Функція для прочитання датасету з текстового файлу
def read_file(file_path):
    # Перевяємо, чи існує файл
    if not os.path.exists(file_path):
        print(f"Файл '{file_path}' не знайдено в директорії проєкту.")
        return []
    # Збергіаємо точки як список кортежів після перевірки на їх коректність
    points = []
    with open(file_path, 'r') as file:
        # Рахуємо номер рядку, щоб при можливих некоректних значеннях координат вказати користувачу, де саме помилка
        line_number = 1
        for line in file:
            try:
                y, x = map(int, line.split())
                points.append((x, y))
            except ValueError:
                # Повідомляємо користувача, якщо є некоректні значення в файлі
                print(f"Некоректні значення координат у рядку {line_number}: {line.strip()}")
                return []
            line_number += 1
    return points

# Функція для побудови графіка за точками
def plot(points):
    # Встановлюємо розміри полотна за умовами завдання
    plt.figure(figsize=(9.6, 5.4)) 
    # Розділюємо координати точок на х та у
    x, y = zip(*points)
    # Налаштування графіку та координатної площини
    plt.scatter(x, y, color = "green")
    plt.title("Лабораторна робота №2\nСемеряга Софія, КМ-31, датасет DS8", fontsize=12)
    plt.savefig("plot.png", format="png")
    plt.show()
    plt.close()

# Головна функція, де вказуємо назву файла з датасетом та викликаємо відповідні функції
def main():
    # Назва файлу з датасетом
    file_path = "DS8.txt"
    points = read_file(file_path)
    plot(points)

if __name__ == "__main__":
    main()
