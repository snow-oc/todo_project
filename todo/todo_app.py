todo_list = {}

def add_task(task, deadline):
    todo_list[task] = deadline
    print(f"現在のタスク数は、{len(todo_list)}です")

def show_tasks():
    if len(todo_list) == 0:
        print("タスクはありません")
        return
    for task, deadline in todo_list.items():
        print(f"タスク: {task}, 期限: {deadline}")

def remove_task(task):
    if task in todo_list:
        todo_list.pop(task)
        print(f"タスク '{task}'を削除しました")
    else:
        print("そのタスクは見つかりません")

import datetime

today = datetime.date.today()

def check_deadlines():
    for task, deadline in todo_list.items():
        deadline_datetime = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        deadline_date = datetime.date(deadline_datetime.year, deadline_datetime.month, deadline_datetime.day)
        if deadline_date <= today:
            print(f"タスク '{task}' の期限が過ぎています")



# 動作確認
check_deadlines();
