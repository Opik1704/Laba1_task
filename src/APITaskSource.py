from typing import List

from Laba1_task.src.TaskSource import TaskSource
from Laba1_task.src.Task import Task

class APITaskSource(TaskSource):
    """
    API-заглушка, имитирующая внешний источник задач
    """
    def __init__(self, endpoint: str = "https://google.com/tasks")->None:
        """Создание фейковых тасков которые должны передатся с апи"""
        self.endpoint = endpoint
        self.mock_data = [
            {"id": "task_1", "payload": {"user_id": 51, "action": "first"}},
            {"id": "task_2", "payload": {"user_id": 52, "action": "second"}},
            {"id": "task_3", "payload": {"user_id": 53, "action": "third"}}
        ]
    def get_tasks(self):
        """
          Имитирует получение задач от внешнего API.
          Returns:
              List[Task]: Список задач из мок-данных API или пустой список в случае ошибки
          """
        try:
            tasks = []
            for task in self.mock_data:
                tasks.append(Task(
                    id=task["id"],
                    payload=task["payload"]
                ))
            return tasks
        except Exception as e:
            print("Ошибка",e)
            return []