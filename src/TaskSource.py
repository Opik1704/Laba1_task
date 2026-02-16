from .Task import *
from  typing import *

@runtime_checkable
class TaskSource(Protocol):
    def get_task(self) -> List[Task]:
        ...

