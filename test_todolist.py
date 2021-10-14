from todolist import Todolist

todolist=Todolist()

todolist.save("공부하기")
todolist.save("운동하기")
todolist.selectAll()

print("====================")

todolist.changeStatus("공부하기",True)
todolist.selectAll()

print("====================")

todolist.changeImportant("운동하기",True)
todolist.selectAll()
