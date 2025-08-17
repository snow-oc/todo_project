# --- 課題③ ---
# タスクを削除する関数 remove_task(task) を作ろう
# 指定した task が todo_list にあれば削除して、「タスク '○○' を削除しました」と表示する
# 指定した task が見つからなければ「そのタスクは見つかりません」と表示する
# 動作確認として、存在するタスクと存在しないタスクの両方でテストしてみてね
todo_list = []

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"タスク '{task}'を削除しました")
    else:
        print("そのタスクは見つかりません")

todo_list.append("海に行く")
remove_task("海に行く")
print(todo_list)
