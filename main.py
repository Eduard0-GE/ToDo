from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QGridLayout, QPushButton
from module_pack.todo_copy import ToDoDialog

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
        todoLayout.addWidget(self.todoN1, 0, 0, 1, 2)
        todoLayout.addWidget(self.todoN2, 0, 2 ,1, 2)
        todoLayout.addWidget(self.todoN3, 1, 0, 1, 2)
        todoLayout.addWidget(self.todoN4, 1, 2, 1, 2)
        
        #showing the main window buttons
        todoLayout.addWidget(self.button_new, 2, 0)
        todoLayout.addWidget(self.button_something, 2, 1)
        todoLayout.addWidget(self.button_previous, 2, 2)
        todoLayout.addWidget(self.button_next, 2, 3)
        
        
        self.setLayout(todoLayout)

#Executs the program
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    program = ToDoMainWindow()
    program.show()
    sys.exit(app.exec_())