import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("./logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def operations(filename: Path) -> list[Path]:
    """Принимает путь до JSON-файла и возвращает список словарей"""
    logger.debug("Функция operations запущена.")
    try:
        with open(filename, encoding="utf-8") as f:
            content = json.load(f)

        if isinstance(content, list):
            logger.info(f"Данные из файла {filename} прочитаны")
            return content
        else:
            logger.warning("JSON не является списком")
            return []

    except FileNotFoundError as e:
        logger.error(f"Ошибка {e} - Файл не найден")
        return []
    except json.decoder.JSONDecodeError as e:
        logger.error(f"Ошибка {e} - Некорректный формат JSON")
        return []


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    OPERATIONS_FILE = BASE_DIR / "data" / "operations.json"
    print(operations(OPERATIONS_FILE))
