import sys
import logs_functions as lf


def main():
    if len(sys.argv) < 2:
        return
    args = sys.argv[1:]
    logs = lf.load_logs(args[0])
    if len(args) > 1:
        lf.display_log_counts(lf.count_logs_by_level(logs))
        print()
        print(f"Деталі логів для рівня {args[1]}:")
        for log in lf.filter_logs_by_level(logs, args[1].lower()):
            print(f'{log["date"]} {log["time"]} - {log["message"]}')
    else:
        lf.display_log_counts(lf.count_logs_by_level(logs))


if __name__ == "__main__":
    main()
