import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QTableWidget, QDockWidget, QTextEdit, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont


class Apv(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Apv Alpha .5'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 650
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        '''
         QText Edits
        '''
        
        listing_gui = QTextEdit('', self)
        listing_gui.setFont(QFont('Arial', 12))
        listing_gui.setPlaceholderText('Listing: ')
        listing_gui.resize(200, 30)
        listing_gui.move(0, 30)
        
        #width = listing_gui.frameGeometry().width()
        #height = listing_gui.frameGeometry().height()
        #print(width)
        #print(height)
        
        
        website_gui = QTextEdit('', self)
        website_gui.setFont(QFont('Arial', 12))
        website_gui.setPlaceholderText('Website: ')
        website_gui.resize(200, 30)
        website_gui.move(0, 60)
        
        email_gui = QTextEdit('', self)
        email_gui.setFont(QFont('Arial', 12))
        email_gui.setPlaceholderText('Email Address: ')
        email_gui.resize(200, 30)
        email_gui.move(0, 90)
        
        username_gui = QTextEdit('', self)
        username_gui.setFont(QFont('Arial', 12))
        username_gui.setPlaceholderText('Username: ')
        username_gui.resize(200, 30)
        username_gui.move(0, 120)
        
        password_gui = QTextEdit('', self)
        password_gui.setFont(QFont('Arial', 12))
        password_gui.setPlaceholderText('Password: ')
        password_gui.resize(200, 30)
        password_gui.move(0, 150)
        
        '''
         End QText Edits
        '''
        
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(1)
        table.setHorizontalHeaderLabels('Listing;Website;Email Address;Username;Password'.split(";"))
        table.setItem(0, 0, QTableWidgetItem('Example Listing'))
        table.setItem(0, 1, QTableWidgetItem('https://example_website.com'))
        table.setItem(0, 2, QTableWidgetItem('ExampleEmail@email.com'))
        table.setItem(0, 3, QTableWidgetItem('ExampleUser66'))
        table.setItem(0, 4, QTableWidgetItem('ExAmPlEpassW0rd872@##@1'))
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        
        
        dock = QDockWidget('Table', self)
        dock.setWidget(table)
        #dock.setLayout(QVBoxLayout())
        dock.resize(800, 650 - 200)
        dock.move(0, 180)
        
        
        
        '''
          Menu
        '''
        mainMenu = self.menuBar() 
        
        fileMenu = mainMenu.addMenu('File')
        
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
     
        printButton = QAction('Print File', self)
        printButton.setShortcut('Ctrl+P')
        printButton.setStatusTip('Print File')
        #printButton.triggered.connect()
        
        fileMenu.addAction(printButton)
        fileMenu.addAction(exitButton)
        
        
        
        editMenu = mainMenu.addMenu('Edit')
        
        
        
        viewMenu = mainMenu.addMenu('View')
        
        displayButton = QAction('Display All', self)
        displayButton.setShortcut('Ctrl+V')
        displayButton.setStatusTip('Display Entire File')
        #displayButton.triggered.connect()
        
        viewMenu.addAction(displayButton)
        
        
        
        
        searchMenu = mainMenu.addMenu('Search')
        searchStringButton = QAction('Search String', self)
        searchStringButton.setShortcut('Ctrl+S')
        searchStringButton.setStatusTip('Enter listing name in text box to search for that listing')
        #searchStringButton.triggered.connect()
        
        searchRowButton = QAction('Search Row', self)
        searchRowButton.setShortcut('Ctrl+R')
        searchRowButton.setStatusTip('Search a specific row')
        #searchRowButton.triggered.connect()
        
        searchColumnButton = QAction('Search Column', self)
        searchColumnButton.setShortcut('Ctrl+Y')
        searchColumnButton.setStatusTip('Enter the specific column you wish to search')
        #searchColumnButton.triggered.connect()
        
        searchMenu.addAction(searchStringButton)
        searchMenu.addAction(searchRowButton)
        searchMenu.addAction(searchColumnButton)
        
        toolsMenu = mainMenu.addMenu('Tools')
        
        
        
        helpMenu = mainMenu.addMenu('Help')
        
        '''
         End Menu
        '''
        self.show()
 
if __name__ == '__main__':
    apv = QApplication(sys.argv)
    ex = Apv()
    sys.exit(apv.exec_())
