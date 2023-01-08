from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton,QMenuBar, QMenu)
import json
from module_pack.todo import ToDoDialog

#Main Window Class
class ToDoMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 450)
        self.setWindowTitle('To Do')
        self.mainWindowLayout()
    
    #Sets the layout of the Main Window
    def mainWindowLayout(self):
        todoLayout = QGridLayout()
        
        #I'm gonna implement the todo miniatures here
        self.todoN1 = QPushButton('To do 1')
        self.todoN2 = QPushButton('To do 2')
        self.todoN3 = QPushButton('To do 3')
        self.todoN4 = QPushButton('To do 4')
        
        #Main Window Buttons
        self.button_new = QPushButton('New')
        self.button_something = QPushButton('Something')
        self.button_previous = QPushButton('Previous')
        self.button_next = QPushButton('Next')
        
        #I'm going to show the miniatures here
        
        task1 = ToDoDialog()
        task2 = ToDoDialog()
        task3 = ToDoDialog()
        task4 = ToDoDialog()
        todoLayout.addWidget(task1, 1, 0, 1, 2)
        todoLayout.addWidget(task2, 1, 2, 1, 2)
        todoLayout.addWidget(task3, 2, 0, 1, 2)
        todoLayout.addWidget(task4, 2, 2, 1, 2)
        
        #showing the main window buttons
        todoLayout.addWidget(self.button_new, 3, 0)
        todoLayout.addWidget(self.button_something, 3, 1)
        todoLayout.addWidget(self.button_previous, 3, 2)
        todoLayout.addWidget(self.button_next, 3, 3)
        
        self.setLayout(todoLayout)
    
#Executs the program
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    program = ToDoMainWindow()
    program.show()
    sys.exit(app.exec_())