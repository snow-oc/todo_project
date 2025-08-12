# --- 課題① ---
# 空のリスト todo_list を作って、そこにタスク（文字列）を追加する関数 add_task(task) を作ろう。
# 追加後に現在のタスク数をprintで表示しよう。
# 動作確認として、関数を使って3つくらいタスクを追加してみてね。

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"現在のタスク数は、{len(todo_list)}です")

add_task("海に行く")
add_task("勉強をする")
add_task("本を読む")

# --- 課題② ---
# todo_list の中身をすべて表示する関数 show_tasks() を作ろう
# タスクが何もなければ「タスクはありません」と表示するようにしてね
