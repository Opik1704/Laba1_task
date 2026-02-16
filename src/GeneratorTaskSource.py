from typing import List
import random

from Laba1_task.src.Task import Task
from Laba1_task.src.TaskSource import TaskSource


class GeneratorTaskSource(TaskSource):
    def __init__(self, count):
        self.count = count
    def get_tasks(self) -> List[Task]:
        """
           Генерирует указанное количество задач
           Returns:
               List[Task]: Список сгенерированных задач
           """
        tasks = []
        for i in range(self.count):
            task= Task(
                id=f"task_{random.randint(1000, 9999)}",
                payload={
                    "user_id": random.randint(1, 100),
                    "action": random.choice(["first", "second", "third", "fourth", "fifth", "sixth", "seventh"])
                }
            )
            tasks.append(task)
        return tasks
