from .abstract_memory import ABCMemory
from .sql_abstraction import SQL
from .json_abstraction import JSON


def get_memory_handle(val) -> ABCMemory:
    if val == "sql":
        return SQL()
    elif val == "json":
        return JSON()
    else:
        raise Exception("Invalid memory handle type.")
