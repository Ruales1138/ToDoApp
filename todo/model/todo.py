# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed = False
        self.tags = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print('Elemento repetido')

    def __str__(self):
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
        todos = {}
