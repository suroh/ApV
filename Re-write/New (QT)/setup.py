import sys
import os
import pandas as pd

'''
 
class ApvCore(object):
    
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
                    if os.path.isfile(path + 'Private.xlsx'): # .ods for linux so this should be changed
                        pass
                    elif not os.path.isfile(path):
                        df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                            'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                            'Password': ['ExamplePassword1234']})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35) #
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': ['Example Listing'], 'Website': ['www.examplewesbite.com'],
                                        'Email': ['ExampleEmail@email.com'], 'Username': ['ExampleUserName'],
                                        'Password': ['ExamplePassword1234']})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    worksheet1.set_column(1, 5, 35) #
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
                    if os.path.isfile(path + 'Private.xlsx'): # .ods for mac so this should be changed
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
    
    
c = ApvCore()
c.verify_setup()
'''

linux = '/home/' + os.getlogin() + '/.APV'
winblows = 'C:\\APV\\'
mac = '/home/' + str(os.getlogin()) + '/.APV/'


def verify_setup():
    try:
        if sys.platform == 'linux2':
            if os.path.isdir(linux):
                print('Directory: ' + linux + 'exists aborting process')
            elif not os.path.isdir(linux):
                create_folder(linux)
                create_excel_document(linux + 'Private.xlsx')
        elif sys.platform == 'win32':
            if os.path.isdir(winblows):
                print('Directory: ' + winblows + 'exists aborting process')
            elif not os.path.isdir(winblows):
                create_folder(winblows)
                create_excel_document(winblows + 'Private.xlsx')
        elif sys.platform == 'darwin':
            if os.path.isdir(mac):
                print('Directory: ' + mac + 'exists aborting process')
            elif not os.path.isdir(mac):
                create_folder(mac)
                create_excel_document(mac + 'Private.xlsx')
    except OSError as exception:
        raise OSError('%s: %s' % (exception.strerror))
    return None

def create_folder(path):
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

verify_setup()