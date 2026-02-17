# Лабораторная работа №2

## Подсистема приёма задач
Задачи могут поступать из различных источников, не связанных
наследованием, но реализуют единый поведенческий контракт.
## Структура проекта
Labal_1
 <pre>
 ├── src/ # 
 │ ├── init.py # Инициализация 
 │ ├── Task.py # Модель задачи в виде dataclass
 │ ├── TaskSource.py # Протокол источника задач
 │ ├── FileTaskSource.py # Источник задач из файла
 │ ├── GeneratorTaskSource.py # Генератор задач
 │ ├── APITaskSource.py # API-заглушка
 │ └── main.py # точка входа в программу
 │
 ├── tests/ # Тесты
 │ ├── init.py # Инициализация тестов
 │ ├── test.py # Тесты 
 ├── .gitignore 
 ├── .pre-commit-config.yaml
 ├── pyproject.toml
 ├── README.md
 ├── requirements.txt
 ├── tasks.json 
 └── uv.lock
  </pre>
Контракт описан с помощью typing.Protocol 
## Установка 
 ```bash
 $ python -m venv venv
 $ source venv/bin/activate
 
 $ pip install requirements.txt
 $ python -m src.main
```
