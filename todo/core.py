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


# 2.获取所有任务
# 现在 task_list 是直接暴露给调用者的，工业界通常会提供一个函数来获取数据，而不是让外部直接操作内部数据结构。

# def get_tasks(task_list):
#     tasks = []
#     if len(task_list) == 0:
#         return []
#     for i in task_list:
#         tasks.append(i)
#     return tasks

# 可以简化，如果 task_list 本身就是一个列表，直接返回它的一个拷贝就行了
# def get_tasks(task_list):
#     if len(task_list) == 0:
#         return []
#     return list(task_list)

# .copy() 会返回列表的一个浅拷贝，空列表也会直接返回 []，所以那个 if 判断也不需要了。
def get_tasks(task_list):
    return task_list.copy()

#  Refactor 阶段的意义：改善代码质量，但不改变行为。


# 3. 完成任务
# 实现"把一个任务标记为完成"

# 怎么判断 index 是否越界？
# 越界时怎么抛出异常？
# 正常情况下怎么修改对应任务的 completed 字段

def complete_task(task_list, index):
    if index >= len(task_list):
        # raise IndexError
        # 工业界里异常信息越具体越好，出 bug 时能直接看出问题在哪
        raise IndexError(f"index {index} is out of range, task list has {len(task_list)} tasks")
    task_list[index]["completed"] = True


# 4. 删除任务
def delete_task(task_list, index):
    if index >= len(task_list):
        raise IndexError(f"index {index} is out of range, task list has {len(task_list)} tasks")
    task_list.pop(index)

# 5. 编辑任务标题
def edit_task(task_list, index, new_title):
    if index >= len(task_list):
        raise IndexError
    task_list[index]["title"] = new_title