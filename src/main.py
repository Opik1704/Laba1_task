from typing import List
from Laba1_task.src.Task import Task
from Laba1_task.src.TaskSource import TaskSource
from Laba1_task.src.FileTaskSource import FileTaskSource
from Laba1_task.src.GeneratorTaskSource import GeneratorTaskSource
from Laba1_task.src.APITaskSource import APITaskSource
import json

def main():
    """Вход в приложение и получение tasks"""
    tasks = [
        {"id": "task_5", "payload": {"user_id": 1, "action": "fifth"}},
        {"id": "task_6", "payload": {"user_id": 2, "action": "sixth", }},
        {"id": "task_7", "payload": {"user_id": 3, "action": "seventh",}}
    ]
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f)

    task_source = [
        FileTaskSource("tasks.json"),
        GeneratorTaskSource(5),
        APITaskSource()
    ]

    all_tasks = []
    for task in task_source:
        if isinstance(task, TaskSource):
            tasks = task.get_tasks()
            all_tasks.extend(tasks)
    for task in all_tasks:
        print(task)

    classes = [
        FileTaskSource,
        GeneratorTaskSource,
        APITaskSource,
        str,
        int,
        list,
        dict
    ]
    for cls in classes:
        if issubclass(cls, TaskSource):
            print(cls.__name__,"Реализует контракт TaskSource")
        else:
            print(cls.__name__," НЕ реализует контракт TaskSource")

if __name__ == "__main__":
    main()
