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

    def add_tag(self, tag: str):
        self.tags.insert(tag)

prueba = Todo(1, 'hola', 'jaja')
print(prueba.completed)
prueba.mark_completed()
print(prueba.completed)
print(prueba.tags)
prueba.add_tag('David')

