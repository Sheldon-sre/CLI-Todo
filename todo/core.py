# 核心业务逻辑

# 1. 添加任务
# 第一个也是最核心的功能：在内存中添加一条任务
# questions before coding
# 1. 一个任务至少需要哪些字段
# 2. 函数签名应该是什么？ 入参是什么？ 返回是什么？

'''
工业界视角：
你现在用 dict 或 dataclass 表示一条任务都很正常。
但在真实项目里，任务往往是一个数据库 Model（比如 SQLAlchemy 的 ORM 对象）。我
们之后会走到那一步，现在先保持简单

当前阶段：
当前将任务状态通过completed参数传入, bool类型的参数值, Flase代表任务未完成, True代表任务完成

但我告诉你工业界的考量：
布尔值只能表示两种状态，如果将来任务要加 "in_progress"（进行中）怎么办？
所以很多项目会用字符串枚举，或者 Python 的 Enum 类型

from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

def add_task(task_list, title, status):
    pass
'''

'''
    Args:
    {
        title: "xxxx",
        completed: False/True
    }

    调用者不能决定completed的值, 一个新加入的任务总为未完成

    Args:
    {
        title: "xxxx",
    }
'''
def add_task(task_list, title):
    task = {"title": title, "completed": False}
    task_list.append(task)