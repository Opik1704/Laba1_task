from typing import List
import random

from Laba1_task.src import Task
from Laba1_task.src.TaskSource import TaskSource


class GeneratorTaskSource(TaskSource):
    def __init__(self, count):
        self.count = count
    def get_tasks(self) -> List[Task]:
        """
        Генерирует указанное количество задач.
        """
        tasks = []
        actions = ["first", "second", "third", "fourth", "fifth", "update", "delete", "create"]
        for i in range(self.count):
            task= Task(
                id=f"task_{random.randint(1000, 9999)}",
                payload={
                    "user_id": random.randint(1, 100),
                    "action": random.choice(["first", "second", "third", "delete", "update"])
                }
            )
            tasks.append(task)
        return tasks
