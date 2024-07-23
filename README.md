# Технічне завдання

## Завдання 1: Замикання та кешування чисел Фібоначчі

### Опис завдання

Реалізувати функцію `caching_fibonacci`, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

### Вимоги до завдання

- Функція `caching_fibonacci()` повинна повертати внутрішню функцію `fibonacci(n)`.
- Функція `fibonacci(n)` обчислює n-те число Фібоначчі, використовуючи рекурсію та кешування.
- Якщо число вже знаходиться у кеші, функція повинна повертати значення з кешу.
- Якщо число не знаходиться у кеші, функція повинна обчислити його, зберегти у кеш і повернути результат.

# Завдання 2: Аналіз тексту та обчислення доходів

## Опис завдання

Створити функцію `generator_numbers`, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Також потрібно реалізувати функцію `sum_profit`, яка буде використовувати `generator_numbers` для підсумовування цих чисел і обчислення загального прибутку.

## Вимоги до завдання

- Функція `generator_numbers(text: str)` повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті.
- Функція `sum_profit(text: str, func: Callable)` має використовувати генератор `generator_numbers` для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.
# Завдання 3: Аналіз файлів логів

## Опис завдання

Розробити Python-скрипт для аналізу файлів логів, який виводить статистику за рівнями логування та може фільтрувати записи за рівнем логування.

## Вимоги до завдання

1. Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
2. Скрипт повинен приймати не обов'язковий аргумент командного рядка для виведення всіх записів певного рівня логування.
3. Реалізувати функції:
   - `parse_log_line(line: str) -> dict` для парсингу рядків логу.
   - `load_logs(file_path: str) -> list` для завантаження логів з файлу.
   - `filter_logs_by_level(logs: list, level: str) -> list` для фільтрації логів за рівнем.
   - `count_logs_by_level(logs: list) -> dict` для підрахунку записів за рівнем логування.
   - `display_log_counts(counts: dict)` для форматування та виведення результатів.
# Завдання 4: Декоратори для обробки помилок у консольному боті

## Опис завдання

Додати обробку помилок за допомогою декораторів до консольного бота помічника.

## Вимоги до завдання

1. Створити декоратор `input_error`, який обробляє помилки введення користувача для всіх команд.
2. Обробляти помилки типу `KeyError`, `ValueError`, `IndexError` у функціях за допомогою декоратора `input_error`.
3. Кожна функція для обробки команд має власний декоратор `input_error`.
