""" Modulo per gestire una lista di cosa da fare """

todo_list=[]

while True:
    todo = input('Cosa devi fare? (premi q per uscire) ')
    if todo.lower() == 'q':
        break
    todo_list.append(todo)

for t in todo_list:
    print(t)