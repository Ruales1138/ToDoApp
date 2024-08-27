# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print('Elemento repetido')

    def __str__(self) -> str:
        return f'{self.code_id} - {self.title}'

prueba = Todo(1, 'hola', 'jaja')
print(prueba.tags)
prueba.add_tag('David')
print(prueba.tags)
prueba.add_tag('David')
print(prueba.tags)
print(prueba.__str__())

class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        todo_id: int = len(self.todos) + 1
        todo: Todo = Todo(todo_id, title, description)
        return todo_id
