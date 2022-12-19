from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLineEdit, QCheckBox, QPushButton 
import json

class ToDoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.path = f'/home/heero/Documentos/Grandes Projetos/newtodo/task_lists/task1.json'
        self.setWindowTitle('archiveName')
        self.setGeometry(200, 200, 300, 200)
        self.dict = {}
        self.taskDict()
        self.ToDoLayout()
        print(len(self.dict))

    def taskDict(self):
        with open(self.path, 'r') as jFile:
            self.dict = json.load(jFile)
            for key in self.dict:
                print(self.dict)
                print(key)
                self.dict[key].append(QCheckBox)
                self.dict[key].append(QLineEdit)
                print(self.dict[key][0])
                print(self.dict[key][1])
                print(self.dict[key][2])
                print(self.dict[key][3])
    
    def newTask(self):
        print(len(self.dict))
        self.dict[f'task{len(self.dict)+1}'] = ['', False, QCheckBox, QLineEdit]
        self.todoLayout.addWidget(self.dict[f'task{len(self.dict)-1}'][2](), len(self.dict), 0)
        self.todoLayout.addWidget(self.dict[f'task{len(self.dict)-1}'][3](), len(self.dict), 1, 1, 3)
        
    def ToDoLayout(self):
        self.todoLayout = QGridLayout()
        for key in self.dict:
            #Adding checkbox
            self.todoLayout.addWidget(self.dict[key][2](), int(key[4]), 0)
            self.dict[key][2]().setChecked(self.dict[key][1])
            
            #Adding lineedit
            self.todoLayout.addWidget(self.dict[key][3](), int(key[4]), 1, 1, 3)
            self.dict[key][3]().setText(self.dict[key][0])
        
        self.add_todo = QPushButton('New')
        self.add_todo.clicked.connect(self.newTask)
        
        self.save_todo = QPushButton('Save')
        self.save_todo.clicked.connect(self.newTask)
        
        self.cancel_todo = QPushButton('Cancel')
        self.cancel_todo.clicked.connect(self.newTask)

        self.delete_todo = QPushButton('Delete')
        self.delete_todo.clicked.connect(self.newTask)

        self.todoLayout.addWidget(self.add_todo, 0, 0)
        self.todoLayout.addWidget(self.save_todo, 0, 1)
        self.todoLayout.addWidget(self.cancel_todo, 0, 2)
        self.todoLayout.addWidget(self.delete_todo, 0, 3)        
                       
        self.setLayout(self.todoLayout)

class taskObject():
    def __init__(self, task = '', checked = False):
        self.task = task
        self.checked = checked
    
    def printTask(self):
        print(self.task)
        print(self.checked)
        
    def updateTask(self):
        #self.task = new_task
        #self.checked = update_check
        pass       
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    todo = ToDoDialog()
    todo.show()
    sys.exit(app.exec_())    