import json
from typing import List

from Laba1_task.src import Task
from Laba1_task.src.TaskSource import TaskSource


class FileTaskSource(TaskSource):
    """
    Читает задачи из Json файла
    """
    def __init__(self, filename):
        self.filePath = filename
    def get_tasks(self) -> List[Task]:
        try:
            with open(self.filePath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task(id=item["id"],payload = item['payload']) for item in data]
        except FileNotFoundError:
            print("Файл")
            return []
        except json.JSONDecodeError:
            print("Файл не формата JSON")
            return []
        except Exception as e:
            print("Ошибка",e)
            return []
