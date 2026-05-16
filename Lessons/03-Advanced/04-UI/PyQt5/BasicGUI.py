
# Reference: https://realpython.com/python-pyqt-gui-calculator/ 

import sys

from PyQt5.QtWidgets import *

class GUIWidgets():
    
    def __init__(self):
        # Create an instance of QApplication
        app = QApplication(sys.argv)

        # Create an instance of your application's GUI
        self.window = QWidget()
        self.window.setWindowTitle('Python GUI Example')
        
        # Set layout
        self.layout = QGridLayout()

        # Create Widgets
        self.CreateLabel()
        self.CreateButton()
        self.CreateLineEdit()
        self.CreateComboBox()
        self.CreateRadioButton()

        self.window.setLayout(self.layout)

        # Show your application's GUI
        self.window.show()

        # Run your application's event loop (or main loop)
        sys.exit(app.exec_())

    def CreateLabel(self):
        label = QLabel('Enter Something:', parent=self.window)
        self.layout.addWidget(label, 0, 0)

    def CreateButton(self):
        empty = QLabel('', parent=self.window)
        button = QPushButton('Continue', parent=self.window)
        self.layout.addWidget(empty, 9, 0)
        self.layout.addWidget(button, 10, 0, 1, 2)

        button.clicked.connect(self.ButtonClickEvent)

    def CreateLineEdit(self):
        self.line_edit = QLineEdit('Text', parent=self.window)
        self.layout.addWidget(self.line_edit, 0, 1)

    def CreateComboBox(self):
        empty = QLabel('', parent=self.window)
        self.combo_box = QComboBox(parent=self.window)
        self.combo_box.setCurrentText('-- Select an Option --') 
        self.combo_box.addItem('Option 1')
        self.combo_box.addItem('Option 2')
        self.combo_box.addItem('Option 3')
        self.combo_box.addItem('Option 4')
        self.combo_box.addItem('Option 5')
        self.layout.addWidget(empty, 2, 0)
        self.layout.addWidget(self.combo_box, 3, 0, 1, 2)

    def CreateRadioButton(self):
        empty = QLabel('', parent=self.window)
        label = QLabel('Select an Option:', parent=self.window)
        self.radio1 = QRadioButton('Radio Option 1', parent=self.window)
        self.radio2 = QRadioButton('Radio Option 2', parent=self.window)
        self.radio3 = QRadioButton('Radio Option 3', parent=self.window)
        self.radio4 = QRadioButton('Radio Option 4', parent=self.window)
        self.layout.addWidget(empty, 4, 0)
        self.layout.addWidget(label, 5, 0)
        self.layout.addWidget(self.radio1, 5, 1)
        self.layout.addWidget(self.radio2, 6, 1)
        self.layout.addWidget(self.radio3, 7, 1)
        self.layout.addWidget(self.radio4, 8, 1)

    def ButtonClickEvent(self):
        print('Text Box: ' + self.line_edit.text())

        print('Combo Box: ' + self.combo_box.currentText())

        print('Radio Button: ', end='')
        if self.radio1.isChecked(): print('Radio 1')
        elif self.radio2.isChecked(): print('Radio 2')
        elif self.radio3.isChecked(): print('Radio 3')
        elif self.radio4.isChecked(): print('Radio 4')
        else: print('None')

        print()

def main():
    GUIWidgets()
    

if __name__ == '__main__':
    main()