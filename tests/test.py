import unittest
import json
import tempfile
from typing import List

from Laba1_task.src.Task import Task
from Laba1_task.src.TaskSource import TaskSource
from Laba1_task.src.FileTaskSource import FileTaskSource
from Laba1_task.src.GeneratorTaskSource import GeneratorTaskSource
from Laba1_task.src.APITaskSource import APITaskSource

class TestTask(unittest.TestCase):
    """Тесты TestTask"""
    def test_task_creation(self):
        """Тест создания задачи"""
        task = Task(id="test_task_1", payload={"user_id": 1, "action": "first"})
        self.assertEqual(task.id, "test_task_1")
        self.assertEqual(task.payload["user_id"], 1)
        self.assertEqual(task.payload["action"], "first")
    def test_task_types(self):
        """Тест типов полей Task"""
        task = Task(id="123", payload={"key": "value"})
        self.assertIsInstance(task.id, str)
        self.assertIsInstance(task.payload, dict)

class TestFileTaskSource(unittest.TestCase):
    """Тесты  FileTaskSource"""
    def setUp(self):
        """Создаём JSON файл для тестов"""
        self.test_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8')
        self.test_task = [
            {"id": "file_test_1", "payload": {"user_id": 1, "action": "first"}},
            {"id": "file_test_2", "payload": {"user_id": 2, "action": "second"}}
        ]
        json.dump(self.test_task, self.test_file)
        self.test_file.close()
        self.source = FileTaskSource(self.test_file.name)

    def test_file_read(self):
        """Тест FileTaskSource на правильное чтение файла"""
        tasks = self.source.get_tasks()
        self.assertEqual(len(tasks), 2)

        self.assertEqual(tasks[0].id, "file_test_1")
        self.assertEqual(tasks[0].payload["user_id"], 1)
        self.assertEqual(tasks[0].payload["action"], "first")

        self.assertEqual(tasks[1].id, "file_test_2")
        self.assertEqual(tasks[1].payload["user_id"], 2)
        self.assertEqual(tasks[1].payload["action"], "second")
    def test_file_list(self):
        """ Тест что FileTaskSource возвращает список"""
        tasks = self.source.get_tasks()
        self.assertIsInstance(tasks, List)

    def test_file_object_task(self):
        """Тест что FileTaskSource возвращает объекты Task"""
        tasks = self.source.get_tasks()
        for task in tasks:
            self.assertIsInstance(task, Task)
    def test_fake_file(self):
        """Проверка отсутствующего файла"""
        source = FileTaskSource("fake_file.json")
        tasks = source.get_tasks()
        self.assertEqual(tasks, [])
    def test_empty_file(self):
        """Проверка бработка пустого файла"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', encoding='utf-8') as f:
            f.write("[]")
            f.flush()
            nema_file = FileTaskSource(f.name)
            tasks = nema_file.get_tasks()
            self.assertEqual(tasks, [])


class TestGeneratorTaskSource(unittest.TestCase):
    def test_generetion_list(self):
        """GeneratorTaskSource возвращает список"""
        source = GeneratorTaskSource(3)
        tasks = source.get_tasks()
        self.assertIsInstance(tasks, List)

    def test_generation_object_task(self):
        """GeneratorTaskSource возвращает объекты Task"""
        source = GeneratorTaskSource(3)
        tasks = source.get_tasks()
        for task in tasks:
            self.assertIsInstance(task, Task)
    def test_fields(self):
        """Сгенереные задачи имеют все необходимые поля"""
        source = GeneratorTaskSource(3)
        tasks = source.get_tasks()
        for task in tasks:
            self.assertIsInstance(task.id, str)
            self.assertIn("user_id", task.payload)
            self.assertIn("action", task.payload)
            self.assertIsInstance(task.payload["user_id"], int)
            self.assertIsInstance(task.payload["action"], str)


class TestAPITaskSource(unittest.TestCase):
    """Тесты для APITaskSource"""
    def setUp(self):
        """ Создаёт экземпляр APITaskSource """
        self.source = APITaskSource()
    def test_correct_count(self):
        """ APITaskSource возвращает необходимое количество задач"""
        tasks = self.source.get_tasks()
        self.assertEqual(len(tasks), 3)

    def test_api_list(self):
        """APITaskSource возвращает список"""
        tasks = self.source.get_tasks()
        self.assertIsInstance(tasks, List)

    def test_api_task(self):
        """APITaskSource возвращает объекты Task"""
        tasks = self.source.get_tasks()
        for task in tasks:
            self.assertIsInstance(task, Task)


class TestTaskSourceProtocol(unittest.TestCase):
    """Тесты протокола TaskSource"""
    def test_protocol(self):
        """Проверка реализации протокола TaskSource"""
        sources = [
            FileTaskSource("test.json"),
            GeneratorTaskSource(3),
            APITaskSource()
        ]

        for source in sources:
            with self.subTest(source=source.__class__.__name__):
                self.assertIsInstance(source, TaskSource)
                self.assertTrue(hasattr(source, 'get_tasks'))
                self.assertTrue(callable(source.get_tasks))

    def test_subclasses(self):
        """Проверка что классы являются подклассами TaskSource"""
        classes = [FileTaskSource, GeneratorTaskSource, APITaskSource]
        for cls in classes:
            with self.subTest(cls=cls.__name__):
                self.assertTrue(issubclass(cls, TaskSource))

    def test_non_sources(self):
        """Проверка что другое не реализуют протокол TaskSource """
        non_sources = [
            "строка",
            123,
            [],
            {},
            None
        ]
        for item in non_sources:
            with self.subTest(item=item):
                self.assertNotIsInstance(item, TaskSource)

class TestIntegration(unittest.TestCase):
    """Интеграционные тесты"""
    def test_all_sources(self):
        """Проверка всех источников"""
        sources = [
            FileTaskSource("tasks.json"),
            GeneratorTaskSource(2),
            APITaskSource()
        ]
        all_tasks = []
        for source in sources:
            if isinstance(source, TaskSource):
                tasks = source.get_tasks()
                all_tasks.extend(tasks)
        self.assertGreaterEqual(len(all_tasks), 0)
        for task in all_tasks:
            self.assertIsInstance(task, Task)
    def test_runtime(self):
        """ runtime-проверка"""
        sources = [
            FileTaskSource("tasks.json"),
            GeneratorTaskSource(2),
            APITaskSource(),
            "не источник"
        ]
        valid_count = 0
        for source in sources:
            if isinstance(source, TaskSource):
                valid_count += 1
                tasks = source.get_tasks()
                self.assertIsInstance(tasks, List)
        self.assertEqual(valid_count, 3)
if __name__ == "__main__":
    unittest.main()