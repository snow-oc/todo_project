# --- 課題② ---
# todo_list の中身をすべて表示する関数 show_tasks() を作ろう
# タスクが何もなければ「タスクはありません」と表示するようにしてね
todo_list = []

def show_tasks():
    if len(todo_list) == 0:
        print("タスクはありません")
        return
    for task in todo_list:
        print(task)

show_tasks()
