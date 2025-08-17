# --- 課題④ ---
# タスクを「名前」と「期限」のセットで管理できるようにしよう。
# 1. todo_list はリストではなく、辞書（dict）を使って { "タスク名": "期限" } の形で保存する。
# 2. add_task(task, deadline) でタスク名と期限を追加する。
#    例: add_task("買い物に行く", "2025-08-20")
# 3. show_tasks() は、登録されているタスクと期限をすべて表示するようにする。
# 4. remove_task(task) は、タスク名を指定して削除できるようにする。
#
# 動作確認として、3つのタスクを登録 → 表示 → 1つ削除 → 再表示 の流れを試してね。

todo_list = {}

def add_task(task, deadline):
    todo_list[task] = deadline

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

# 動作確認
add_task("買い物に行く", "2025-08-20")
add_task("海に行く", "2025-08-21")
add_task("本を読む", "2025-08-22")
show_tasks()
remove_task("買い物に行く")
remove_task("旅行の準備をする")
show_tasks()
