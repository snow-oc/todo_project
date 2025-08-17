# todoリスト { "買い物に行く": {"deadline": "2025-08-20", "done": False} }
todo_list = {}

def add_task(task, deadline):
    todo_list[task] = {"deadline": deadline, "done": False}
    print(f"タスクを追加しました。現在のタスク数は、{len(todo_list)}です")

def show_tasks():
    if len(todo_list) == 0:
        print("タスクはありません")
        return
    for task, task_detail in todo_list.items():
        print(f"[{'✓' if task_detail['done'] else ' '}] タスク: {task}, 期限: {task_detail['deadline']}")

def remove_task(task):
    if task in todo_list:
        todo_list.pop(task)
        print(f"タスク '{task}'を削除しました")
    else:
        print("そのタスクは見つかりません")

import datetime

today = datetime.date.today()

def check_deadlines():
    for task, task_detail in todo_list.items():
        deadline_date = datetime.datetime.fromisoformat(task_detail["deadline"]).date()
        if deadline_date < today:
            print(f"タスク '{task}' の期限が過ぎています")

def mark_done(task):
    if task in todo_list:
        todo_list[task]["done"] = True
        print(f"タスク '{task}' を完了にしました")
    else:
        print("そのタスクは見つかりません")

# 動作確認
add_task("買い物に行く", "2025-08-17")
add_task("読書をする", "2025-08-16")
show_tasks()
check_deadlines()
mark_done("読書をする")
show_tasks()
remove_task("買い物に行く")
remove_task("サッカー観戦")
