# --- 課題⑤ ---
# 今日の日付を基準にして、期限が過ぎているタスクをチェックする関数 check_deadlines() を作ろう
# 過ぎている場合は「タスク '○○' の期限が過ぎています」と表示する
# 過ぎていない場合は何も表示しなくてOK
# datetimeモジュールを使って、期限（文字列）を日付型に変換して比較してみてね

todo_list = {}

def add_task(task, deadline):
    todo_list[task] = deadline

add_task("服を買う", "2025-08-16")
add_task("買い物に行く", "2025-08-17")
add_task("海に行く", "2025-08-21")
add_task("本を読む", "2025-08-22")

# ここから
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
