from typing import List

from Laba1_task.src.TaskSource import TaskSource
from Laba1_task.src import Task

class APITaskSource(TaskSource):
    """
    API-заглушка, имитирующая внешний источник задач
    """
    def __init__(self, endpoint: str = "https://fake-api.com/tasks"):
        self.endpoint = endpoint
        self.mock_data = [
            {"id": "api_1", "payload": {"user_id": 41, "action": "first"}},
            {"id": "api_2", "payload": {"user_id": 42, "action": "second"}},
            {"id": "api_3", "payload": {"user_id": 43, "action": "third"}}
        ]
    def get_tasks(self):
        try:
            tasks = []
            for item in self.mock_data:
                tasks.append(Task(
                    id=item["id"],
                    payload=item["payload"]
                ))
            print(f"Успешно получено {len(tasks)} задач")
            return tasks
        except Exception as e:
            print("Ошибка",e)
            return []