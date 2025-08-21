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

def check_deadlines():
    today = datetime.date.today()
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

def check_upcoming(days):
    today = datetime.date.today()
    upcoming = [(task, detail)
                for task, detail in todo_list.items()
                if 0 <= (datetime.datetime.fromisoformat(detail["deadline"]).date() - today).days <= days
    ]
    if upcoming:
        for task, detail in upcoming:
            remaining_days = (datetime.datetime.fromisoformat(detail["deadline"]).date() - today).days
            print(f"タスク'{task}'の期限が近づいています。(あと{remaining_days}日) 期限: {detail['deadline']}")
    else:
        print("期限が近いタスクはありません")

def edit_task(old_task, new_task=None, new_deadline=None):
    if old_task not in todo_list:
        print("そのタスクは見つかりません")
        return
    if new_task:
        todo_list[new_task] = todo_list.pop(old_task)
        print(f"タスク '{old_task}' を '{new_task}' へ更新しました")
    if new_deadline:
        target = new_task or old_task
        todo_list[target]["deadline"] = new_deadline
        print(f"タスク '{target}' の期限を {new_deadline} へ更新しました'")

def show_done_tasks():
    done_task_list = [(task, detail) for task, detail in todo_list.items() if detail["done"]]
    if done_task_list:
        for task, detail in done_task_list:
            print(f"[✓] タスク: {task}, 期限: {detail['deadline']}")
    else:
        print("完了のタスクはありません")

def show_pending_tasks():
    pending_task_list = [(task, detail) for task, detail in todo_list.items() if not detail["done"]]
    if pending_task_list:
        for task, detail in pending_task_list:
            print(f"[ ] タスク: {task}, 期限: {detail['deadline']}")
    else:
        print("未完了のタスクはありません")

def search_tasks(keyword):
    found = False
    for task, task_detail in todo_list.items():
        if keyword in task:
            print(f"[{'✓' if task_detail['done'] else ' '}] タスク: {task}, 期限: {task_detail['deadline']}")
            found = True
    if not found:
        print("該当するタスクはありません")


# 動作確認
add_task("買い物に行く", "2025-08-17")
add_task("読書をする", "2025-08-16")
add_task("デート", "2025-08-20")
add_task("ゲーム", "2025-08-21")
show_tasks()
check_deadlines()
mark_done("読書をする")
show_tasks()
remove_task("買い物に行く")
remove_task("サッカー観戦")
check_upcoming(3)
edit_task("仕事", new_task="Python勉強")
edit_task("デート", new_task="Python勉強")
edit_task("Python勉強", new_deadline="2025-09-01")
edit_task(old_task="ゲーム", new_task="アクションゲーム", new_deadline="2025-09-20")
show_tasks()
show_done_tasks()
show_pending_tasks()
search_tasks("Python")
