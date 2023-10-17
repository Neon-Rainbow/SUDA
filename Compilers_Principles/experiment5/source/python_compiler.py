# file: python_compiler.py
# !/usr/bin/python


"""
Simple python compiler

This file create a simple python compiler

Date:2023.10.12
"""
import os
import re
import subprocess
import sys
from pathlib import Path

from PyQt6.QtGui import QIcon, QAction, QFont
from PyQt6.QtWidgets import (
    QMainWindow, QTextEdit,
    QFileDialog, QApplication, QToolTip, QListWidget,
    QListWidgetItem
)

from string2html import string2html


class FunctionAndClassWindow(QMainWindow):
    """
    Displays a list of functions and classes from the provided code.

    This window provides a list of functions and classes extracted from the
    Python code. Clicking on a function or class name in the list will navigate
    to its location in the main code editor.

    Attributes:
        text_edit (QTextEdit): Reference to the main code editor.
    """

    def __init__(self, functions_and_classes, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.initUI(functions_and_classes)

    def initUI(self, functions_and_classes):
        self.setGeometry(800, 800, 300, 400)
        self.setWindowTitle("Functions and Classes")
        list_widget = QListWidget()

        for name in functions_and_classes:
            item = QListWidgetItem(name)
            list_widget.addItem(item)

        list_widget.itemClicked.connect(self.onItemClicked)
        self.setCentralWidget(list_widget)

    def onItemClicked(self, item):
        """
        Handles the event when an item in the list is clicked.

        Navigates to the location of the clicked function or class in the main
        code editor.

        Args:
            item (QListWidgetItem): The clicked item in the list.
        """
        text = item.text()
        index = self.text_edit.toPlainText().find(text)
        if index != -1:
            cursor = self.text_edit.textCursor()
            cursor.setPosition(index)
            self.text_edit.setTextCursor(cursor)
            self.text_edit.setFocus()


class AnswerWindow(QMainWindow):
    """
    This class is used to display the results of running Python code
    """

    def __init__(self, output, error):
        super().__init__()
        self.text_edit = None  # self.text_edit displays the output result of the code execution
        self.output = output
        self.error = error
        self.initUI()

    def initUI(self):
        """
        display the results of running Python code

        Args:
            self: The Example object that calls this function.

        Returns:
            None.But it will display the result of the code
        """
        self.setGeometry(800, 300, 400, 400)
        self.setWindowTitle('Python Run Results Window')
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        python_execution_result = f"""
        </p><p style="color: red;">{self.error}
        </p><p style="color: black;">{self.output}
        """
        # print(f"{self.error}\n{self.output}")
        self.text_edit.setHtml(python_execution_result)


class MainWindow(QMainWindow):
    """
    This class is used to display the  main interface of the GUI
    """

    def __init__(self):
        super().__init__()
        # self.function_window = None
        # TODO(Haonan_Fang@Outlook.com):something wrong with self.function_window
        self.output_window = None  # self.output_window displays the output result of the code execution
        self.text_edit = None  # self.text_edit is used for inputting Python code
        self.initUI()

    def initUI(self):
        # 添加代码区域
        self.text_edit = QTextEdit()
        # TODO(Haonan_Fang@Outlook.com):添加行号区域

        self.setCentralWidget(self.text_edit)
        self.setWindowIcon(QIcon("icons/python.svg"))

        QToolTip.setFont(QFont('SansSerif', 10))

        # Set up a text box for inputting Python code
        # self.text_edit = QTextEdit()
        # self.setCentralWidget(self.text_edit)
        self.statusBar()

        # Set up the title of the program
        self.setWindowTitle('Simple python compiler')

        # Set up the status bar of the program
        self.statusBar().showMessage('Simple python compiler authored by FHN', 5000)

        # Set up the menu bar of the program
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        edit_menu = menubar.addMenu("&Edit")
        run_menu = menubar.addMenu("&Run")

        # Set up a way to exit the program
        exit_act = QAction(QIcon('icons/exit.svg'), '&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.instance().quit)

        # Save the file
        save_act = QAction(QIcon('icons/save_file.svg'), '&Save', self)
        save_act.setShortcut('Ctrl+S')
        save_act.setStatusTip("Save file")
        save_act.triggered.connect(self.saveDialog)

        # Open the file
        open_act = QAction(QIcon('icons/open_file.svg'), '&Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.setStatusTip("Open file")
        open_act.triggered.connect(self.showDialog)

        # New file
        new_file_act = QAction(QIcon("icons/new_file.svg"), "&New File", self)
        new_file_act.setShortcut("Ctrl+N")
        new_file_act.setStatusTip("New file")
        new_file_act.triggered.connect(self.newFile)

        file_menu.addAction(new_file_act)
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addAction(exit_act)

        # Undo
        undo_act = QAction(QIcon("icons/undo.svg"), "&Undo", self)
        undo_act.setShortcut("Ctrl+Z")
        undo_act.setStatusTip("Undo")
        undo_act.triggered.connect(self.text_edit.undo)

        # Redo
        redo_act = QAction(QIcon("icons/redo.svg"), "&Redo", self)
        redo_act.setShortcut("shift+Ctrl+Z")
        redo_act.setStatusTip("Redo")
        redo_act.triggered.connect(self.text_edit.redo)

        # Cut
        cut_act = QAction(QIcon("icons/cut.svg"), "&Cut", self)  # 创建一个操作对象
        cut_act.setShortcut("Ctrl+X")  # 设置快捷键
        cut_act.setStatusTip("Cut")  # 设置状态提示
        cut_act.triggered.connect(self.text_edit.cut)

        # Paste
        paste_act = QAction(QIcon("icons/paste.svg"), "&Paste", self)
        paste_act.setShortcut("Ctrl+V")
        paste_act.setStatusTip("Paste")
        paste_act.triggered.connect(self.text_edit.paste)

        # Copy
        copy_act = QAction(QIcon("icons/copy.svg"), "&Copy", self)
        copy_act.setShortcut("Ctrl+C")
        copy_act.setStatusTip("Copy")
        copy_act.triggered.connect(self.text_edit.copy)

        # find function and class
        find_function_and_class_act = QAction(QIcon("icons/search.svg"), "&Find", self)
        find_function_and_class_act.setShortcut("Ctrl+F")
        find_function_and_class_act.setStatusTip("Find all functions and classes")
        find_function_and_class_act.triggered.connect(self.findFunctionsAndClasses)

        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act)
        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addAction(find_function_and_class_act)

        # Run the program
        run_act = QAction(QIcon("icons/run_code.svg"), "&Run", self)
        run_act.setShortcut("Shift+F10")
        run_act.setStatusTip("Run the python code")
        run_act.triggered.connect(self.runCode)

        run_menu.addAction(run_act)

        # Set Window Size and Position
        self.setGeometry(350, 300, 350, 250)
        self.show()

    def newFile(self):
        """
        Clears the content of the text editor to create a new file.

        This function sets the content of the text editor to an empty string,
        allowing the user to start writing a new Python code from scratch.

        Args:
            self: The Example object that calls this function.

        Returns:
            None. But the text editor will be cleared.
        """
        self.text_edit.clear()

    def showDialog(self):
        """
        Opens a file dialog and reads the content of a file.

        This function opens a file dialog and allows the user to select a file from the home directory.
        Then it reads the content of the file and displays it in a QTextEdit widget.

        Args:
            self: The Example object that calls this function.

        Returns:
            None,but the function will show the code on the window

        Raises:
            FileNotFoundError: If the file does not exist or cannot be opened.
            IOError: If there is an error reading the file.
        """
        home_dir = str(Path.home())
        file_name = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        with open(file_name[0], 'r', encoding="utf-8") as f:
            text = f.read()
            css = string2html(text)
            self.text_edit.setHtml(css)

    def saveDialog(self):
        """
        Opens a file dialog and saves the content of the text edit.

        This function opens a file dialog and allows the user to select a file name and location from the home directory.
        Then it writes the content of the text edit widget to the file.

        Args:
            self: The Example object that calls this function.

        Returns:
            None,But the function will save the python file

        Raises:
            FileNotFoundError: If the file cannot be created or opened.
            IOError: If there is an error writing to the file.
        """
        home_dir = str(Path.home())
        file_name = QFileDialog.getSaveFileName(self, "Save file", home_dir)
        with open(file_name[0], "w", encoding="utf-8") as f:
            text = self.text_edit.toPlainText()
            f.write(text)

    def runCode(self):
        """
        Executes Python code from a text editor.

        This function retrieves code from a text editor, writes it to a file named 'code.py', and then uses the subprocess module to run this file.
        The output of the code is captured and stored in the `result` variable. The output is then decoded from bytes to a string. Finally, the 'code.py' file is removed and the output is printed.

        Note: This function can dynamically run Python code, but it can execute any Python code, which can be dangerous if the code comes from an untrusted source.
        Always make sure to validate and sanitize any input you receive if you're planning to execute it.

        Args:
            self: An instance of an object that contains the text editor and the code to be executed.

        Returns:
            None. But this function will print the output and the errors after executing the Python code.

        Raises:
            May raise any exceptions that are raised by the Python code being executed or file operations.
        """
        code = self.text_edit.toPlainText()
        self.text_edit.setHtml(string2html(code))
        with open('code.py', 'w', encoding="UTF-8") as f:
            f.write(code)
        # In some computer, args needs to be "python3" instead of "python"
        result = subprocess.run(['python3', 'code.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode("UTF-8")
        errors = result.stderr.decode("UTF-8")
        os.remove("code.py")
        errors = result.stderr.decode("UTF-8")
        self.output_window = AnswerWindow(output, errors)
        self.output_window.show()

    def findFunctionsAndClasses(self):
        """
        Displays a window listing all functions and classes in the code editor.

        This method extracts all the functions and classes from the current code
        in the text editor, and displays them in a new FunctionAndClassWindow.
        Clicking on a function or class name in this window will navigate to its
        location in the main code editor.

        Returns:
            None. A new FunctionAndClassWindow is displayed with the list of functions and classes.
        """
        code = self.text_edit.toPlainText()
        functions_and_classes = re.findall(r'(def|class)\s+(\w+)\s*\(', code)
        names = [f"{item[0]} {item[1]}" for item in functions_and_classes]
        self.function_and_class_window = FunctionAndClassWindow(names, self.text_edit)
        self.function_and_class_window.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
