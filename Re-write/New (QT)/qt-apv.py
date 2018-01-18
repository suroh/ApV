import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QTableWidget, QDockWidget, QTextEdit, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont

class ApvSetup(object):

    def __init__(self):
        self.__linux = '/home/' + str(os.getlogin()) + '/APV/'
        self.__winblows = 'C:\\APV\\'
        self.__mac = '/home/' + str(os.getlogin()) + '/.APV/'
        self.verify_setup()

    def verify_setup(self):
        try:
            if sys.platform == 'linux2':
                if os.path.isdir(self.__linux):
                    print('Directory: ' + self.__linux + 'exists aborting process')
                elif not os.path.isdir(self.__linux):
                    self.create_folder(self.__linux)
                    self.create_excel_document(self.__linux + 'Private.xlsx')
            elif sys.platform == 'win32':
                if os.path.isdir(self.__winblows):
                    print('Directory: ' + self.__winblows + 'exists aborting process')
                elif not os.path.isdir(self.__winblows):
                    self.create_folder(self.__winblows)
                    self.create_excel_document(self.__winblows + 'Private.xlsx')
            elif sys.platform == 'darwin':
                if os.path.isdir(self.__mac):
                    print('Directory: ' + self.__mac + 'exists aborting process')
                elif not os.path.isdir(self.__mac):
                    self.create_folder(self.__mac)
                    self.create_excel_document(self.__mac + 'Private.xlsx')
        except OSError as exception:
            raise OSError('%s: %s' % (exception.strerror))
        return None

    def create_folder(self, path):
        try:
            if os.path.isdir(path):
                pass
            else:
                os.makedirs(path)
                print(path + ': has been created')
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def create_excel_document(self, path):
        try:
            if sys.platform == 'linux2':
                if os.path.isdir(path):
                    if os.path.isfile(path + 'Private.xlsx'):  # .ods for linux so this should be changed
                        pass
                    elif not os.path.isfile(path):
                        df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                            'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                            'Password': ['ExamplePassword1234']})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35)  #
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                        'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                        'Password': ['ExamplePassword1234']})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    worksheet1.set_column(1, 5, 35)  #
                    writer.save()
            elif sys.platform == 'win32':
                if os.path.isdir(path):
                    if os.path.isfile(path + 'Private.xlsx'):
                        pass
                    elif not os.path.isfile(path):
                        df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                            'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                            'Password': ['ExamplePassword1234']})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35)
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                        'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                        'Password': ['ExamplePassword1234']})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    worksheet1.set_column(1, 5, 35)
                    writer.save()
            elif sys.platform == 'darwin':
                if os.path.isdir(path):
                    if os.path.isfile(path + 'Private.xlsx'):  # .ods for mac so this should be changed
                        pass
                    elif not os.path.isfile(path):
                        df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                            'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                            'Password': ['ExamplePassword1234']})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35)
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                        'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                        'Password': ['ExamplePassword1234']})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    worksheet1.set_column(1, 5, 35)
                    writer.save()
        except IOError as exception:
            raise IOError('%s: %s' % (exception.strerror))
        return None


class Apv(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Apv Alpha .5'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 650



        ApvSetup().verify_setup()
        self.__master_dict = {'Listing': None, 'Website': None, 'Email': None, 'Username': None, 'Password': None}
        self.__linux = '/home/' + str(os.getlogin()) + '/APV/'
        self.__winblows = 'C:\\APV\\'
        self.__mac = '/home/' + str(os.getlogin()) + '/.APV/'

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        '''
         QText Edits
        '''
        
        self.listing_gui = QLineEdit('', self)
        self.listing_gui.setFont(QFont('Arial', 12))
        self.listing_gui.setPlaceholderText('Listing: ')
        self.listing_gui.resize(200, 30)
        self.listing_gui.move(0, 30)
        self.listing_gui.returnPressed.connect(self.get_listing)
        
        #width = listing_gui.frameGeometry().width()
        #height = listing_gui.frameGeometry().height()
        #print(width)
        #print(height)
        
        
        self.website_gui = QLineEdit('', self)
        self.website_gui.setFont(QFont('Arial', 12))
        self.website_gui.setPlaceholderText('Website: ')
        self.website_gui.resize(200, 30)
        self.website_gui.move(0, 60)
        self.website_gui.returnPressed.connect(self.get_website)
        
        self.email_gui = QLineEdit('', self)
        self.email_gui.setFont(QFont('Arial', 12))
        self.email_gui.setPlaceholderText('Email Address: ')
        self.email_gui.resize(200, 30)
        self.email_gui.move(0, 90)
        self.email_gui.returnPressed.connect(self.get_email)
        
        self.username_gui = QLineEdit('', self)
        self.username_gui.setFont(QFont('Arial', 12))
        self.username_gui.setPlaceholderText('Username: ')
        self.username_gui.resize(200, 30)
        self.username_gui.move(0, 120)
        self.username_gui.returnPressed.connect(self.get_username)
        
        self.password_gui = QLineEdit('', self)
        self.password_gui.setFont(QFont('Arial', 12))
        self.password_gui.setPlaceholderText('Password: ')
        self.password_gui.resize(200, 30)
        self.password_gui.move(0, 150)
        self.password_gui.returnPressed.connect(self.get_password)
        
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

    def get_listing(self):
        __listing = self.listing_gui.text()
        self.__master_dict['Listing'] = __listing

    def get_website(self):
        __website = self.website_gui.text()
        self.__master_dict['Website'] = __website

    def get_email(self):
        __email = self.email_gui.text()
        self.__master_dict['Email'] = __email

    def get_username(self):
        __usr = self.username_gui.text()
        self.__master_dict['Username'] = __usr

    def get_password(self):
        if sys.platform == 'linux2':
            __password = self.password_gui.text()
            self.__master_dict['Password'] = __password
            self.append_and_write_dataframes(self.__linux)
        elif sys.platform == 'win32':
            __password = self.password_gui.text()
            self.__master_dict['Password'] = __password
            self.append_and_write_dataframes(self.__winblows)
        elif sys.platform == 'darwin':
            __password = self.password_gui.text()
            self.__master_dict['Password'] = __password
            self.append_and_write_dataframes(self.__mac)

    def append_and_write_dataframes(self, path):
        df = pd.read_excel(path, sheet_name='Accounts')
        df1 = pd.DataFrame({'Listing': [self.__master_dict['Listing']], 'Website': [self.__master_dict['Website']],
                            'Email': [self.__master_dict['Email']], 'Username': [self.__master_dict['Username']],
                            'Password': [self.__master_dict['Password']]})
        df3 = df.append(df1)
        df3 = df3[['Listing', 'Website', 'Email', 'Username', 'Password']]
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df3.to_excel(writer, sheet_name='Accounts')
        workbook = writer.book
        worksheet1 = writer.sheets['Accounts']
        worksheet1.set_column(1, 5, 35)
        writer.save()
        self.__master_dict.clear()



if __name__ == '__main__':
    apv = QApplication(sys.argv)
    ex = Apv()
    sys.exit(apv.exec_())
