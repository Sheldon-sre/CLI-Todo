# 为添加功能写的测试
from todo.core import add_task, get_tasks, complete_task, delete_task, edit_task
import pytest

def test_add_task():
    # 准备
    task_list = []
    title = "buy eggs"
    completed = False
    # 执行
    add_task(task_list, title)
    # 断言：任务确实被加进去了(加完一条任务后，你要断言哪几件事？)
    # 断言task_list不为空 + 任务的 title 是不是你传入的 "buy eggs" (+ 任务的 completed 初始值是不是 False)
    # 断言的语法: assert 条件, "失败时显示的错误信息" --> 条件是想要合法的条件
    # 测试命令: pytest tests/test_core.py -v

    assert len(task_list) == 1, "taks_list为空"

    # 先取出第一个任务
    task = task_list[0]

    # 再从任务 dict 里取字段
    assert task["title"] == "buy eggs", "title is not 'buy eggs'"

    '''
    错误的取值方法：
    assert task_list[title] == "buy eggs", "title is not 'buy eggs'"
    assert task_list[completed] == False, "completed is not False"

    task_list 是一个列表, task_list[title] 是用字符串当索引，列表只能用数字索引

    '''

# get_tasks 的职责是获取任务列表，所以测试的重点应该是——你拿到的数据对不对，而不只是"不为空"。 
# 拿到的任务数量是否正确？
# 拿到的第一个任务，内容对不对？
def test_get_tasks():
    task_list = []
    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    tasks = get_tasks(task_list)
    assert len(tasks) == 2, "the numbers of tasks is not 2"
    assert tasks[0]["title"] == "buy eggs", "the title of first task is not 'buy eggs'"
    assert tasks[1]["title"] == "buy fruits", "the title of second task is not 'buy fruits'"

# 另外还有一个边界情况值得测试——如果 task_list 是空的，get_tasks 应该返回什么？这种边界测试在工业界非常重要，单独写一个测试函数：
def test_get_tasks_empty():
    task_list = []
    tasks = get_tasks(task_list)
    assert tasks == [], "task list should be empty"

def test_complete_task():
    task_list = []
    index = 1

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    complete_task(task_list, index)

    assert task_list[0]["completed"] == False, "the status of first task should be uncompleted"
    assert task_list[1]["completed"] == True, "the status of second task should be completed"

# 边界情况: 如果传入的 index 超出列表范围怎么办？比如列表只有2个任务，但传入 index = 5？
def test_complete_task_invalid_index():
    task_list = []

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    # assert index < len(task_list), raise IndexError

    # 执行 complete_task(task_list, 5) 时，期望它抛出 IndexError，如果抛出了测试就通过，没抛出就失败。
    with pytest.raises(IndexError):
        complete_task(task_list, 5)

def test_delete_task():
    task_list = []
    index = 1

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    delete_task(task_list, index)

    assert len(task_list) == 1, "the numbers of tasks should be 1"
    assert task_list[0]["title"] == "buy eggs", "the title of first task should be 'buy eggs'"

def test_delete_task_invalid_index():
    task_list = []

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    with pytest.raises(IndexError):
        delete_task(task_list, 5)

def test_edit_task():
    task_list = []
    index = 1
    new_title = "buy tomatoes"

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    edit_task(task_list, index, new_title)

    assert len(task_list) == 2, "the number of tasks should be 2"
    assert task_list[1]["title"] == "buy tomatoes", "the title of second task should be 'buy tomatoes'"

def test_edit_task_invalid_index():
    task_list = []

    add_task(task_list, "buy eggs")
    add_task(task_list, "buy fruits")

    with pytest.raises(IndexError):
        edit_task(task_list, 5, "buy tomatoes")
# TDD cycle: Red → 先写测试，跑失败 ; Green → 写最简实现，跑通过; Refactor（重构）-> 写更清晰的测试