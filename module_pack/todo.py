from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QLineEdit, QCheckBox, QPushButton 
import json

class ToDoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.path = f'/home/heero/Documentos/projetos/python/newtodo/task_lists/task1.json'
        self.setWindowTitle('archiveName')
        self.dict = {}
        self.taskDict()
        self.windowLayout()        

    def taskDict(self):
        with open(self.path, 'r') as jFile:
            self.dict = json.load(jFile)
            for key in self.dict:
                self.dict[key].append(QCheckBox())
                self.dict[key].append(QLineEdit())
    
    def newTask(self):
        if len(self.dict) < 10: 
            self.dict[f'task{len(self.dict)+1}'] = ['', False, QCheckBox(), QLineEdit()]
            self.todoLayout.addWidget(self.dict[f'task{len(self.dict)}'][2], len(self.dict), 0)
            self.todoLayout.addWidget(self.dict[f'task{len(self.dict)}'][3], len(self.dict), 1, 1, 3)
        else:
            pass
            
    def saveToDo(self):
        #Runs trough the dict, changes the values and excludes the functions
        for key in self.dict:
            if self.dict[key][3].text() == "":
                del self.dict[key]
            else:
                self.dict[key][0] = self.dict[key][3].text()
                self.dict[key][1] = self.dict[key][2].isChecked()
                del self.dict[key][2]
                del self.dict[key][2]
        with open(self.path, 'w') as jFile:
            jFile.write(json.dumps(self.dict))
        
    def taskLayout(self, position = 0):
        for key in self.dict:
            #Adding lineedit
            self.dict[key][3].setText(self.dict[key][0])
            self.todoLayout.addWidget(self.dict[key][3], int(key[4]) - position, 1, 1, 3)
            
            #Adding checkbox
            self.dict[key][2].setChecked(self.dict[key][1])
            self.todoLayout.addWidget(self.dict[key][2], int(key[4]) - position, 0)

    def ButtonLayout(self):
        self.add_todo = QPushButton('New')
        self.add_todo.clicked.connect(self.newTask)
        
        self.save_todo = QPushButton('Save')
        self.save_todo.clicked.connect(self.saveToDo)
        
        self.cancel_todo = QPushButton('Cancel')
        self.cancel_todo.clicked.connect(self.newTask)

        self.delete_todo = QPushButton('Delete')
        self.delete_todo.clicked.connect(self.newTask)

        self.todoLayout.addWidget(self.add_todo, 0, 0)
        self.todoLayout.addWidget(self.save_todo, 0, 1)
        self.todoLayout.addWidget(self.cancel_todo, 0, 2)
        self.todoLayout.addWidget(self.delete_todo, 0, 3)        
    
    def windowLayout(self):
        self.todoLayout = QGridLayout()
        if __name__ == '__main__':   
            self.setGeometry(200, 200, 300, 200)
            self.ButtonLayout()
            self.taskLayout()
        else:
            self.setGeometry(200, 200, 100, 100)
            self.taskLayout(1)
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