# 为添加功能写的测试
from todo.core import add_task

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

    task_list 是一个列表，task_list[title] 是用字符串当索引，列表只能用数字索引

    '''

    # TDD cycle: Red → 先写测试，跑失败 ; Green → 写最简实现，跑通过; Refactor（重构）-> 写更清晰的测试