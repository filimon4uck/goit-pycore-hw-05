from collections import defaultdict


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    count_logs = defaultdict(int)
    for log in logs:
        count_logs[log["level"]] += 1
    return dict(count_logs)


def display_log_counts(counts: dict):
    headers = ["Рівень логування", "Кількість"]

    key_length = len(headers[0])
    value_length = len(headers[1])
    header_row = f"{headers[0]:<{key_length}} | {
        headers[1]:<{value_length}}"
    separator_row = f"{'-' * key_length}-|-{'-' * value_length}"
    print(header_row)
    print(separator_row)

    for key, value in counts.items():
        data_row = f"{key:<{key_length}} | {value:<{value_length}}"
        print(data_row)


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(maxsplit=3)
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            return [parse_log_line(line) for line in file.readlines()]
    except FileNotFoundError:
        return "File not found"
    except FileExistsError:
        return "File not exists"
