class Todolist:

    # 변수 정의
    todoItem = {}
    iscompleted = False
    isimportant = False

    # 함수 정의
    def save(self, todo):
        self.todoItem[todo] = [False, False]

    def changeStatus(self, todo, iscompleted):
        self.todoItem[todo][0] = iscompleted

    def changeImportant(self, todo, isimportant):
        self.todoItem[todo][1] = isimportant

    def selectAll(self):
        for key in self.todoItem.keys():
            print(key, "/ 완료여부:",self.todoItem[key][0], "/ 중요여부:", self.todoItem[key][1])

    def delete(self, todo):
        del self.todoItem[todo]

    def changeTodoName(self, todo, changeTodo):
        self.todoItem[changeTodo] = self.todoItem.pop(todo)