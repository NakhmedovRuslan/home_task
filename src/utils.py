import json
from pathlib import Path


def operations(filename: Path) -> list[Path]:
    """Принимает путь до JSON-файла и возвращает список словарей"""
    try:
        with open(filename, encoding="utf-8") as f:
            content = json.load(f)

        if isinstance(content, list):
            return content
        else:
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# if __name__ == "__main__":
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     OPERATIONS_FILE = BASE_DIR / "data" / "operations.json"
#     print(operations(OPERATIONS_FILE))

# print(operations(r"C:\Users\rusla\PycharmProjects\hometask9\data\operations.json"))
