########################################################################################################################
# Copyright 2017 - 2021                                                                                                #
# Aaron Johnson                                                                                                        #
# <Aaronjohnson@protonmail.ch>                                                                                         #
########################################################################################################################
__author__ = 'Aaron Johnson'
import sys
import os
import base64
import nacl
#from Crypto.Cipher import AES
#from Crypto import Random
import linecache
import hashlib
#from Crypto.PublicKey import RSA
#from Crypto.Signature import PKCS1_v1_5
import random
import array
import math
import datetime
import threading
import socket
import linecache
import fileinput
import xlwt
import pandas as pd
import kivy
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
import kivy.animation
from kivy.core.image import Image as CoreImage
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
import kivy.event
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner
from functools import partial
from kivy.properties import AliasProperty
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.filechooser import FileChooser, FileChooserListView
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.videoplayer import VideoPlayer


class Security(object):
    rsa_key = None

    def __init__(self):
        gen_len = random.randint(1, 100)
        k_len = list()
        complete = ''
        self._block = 16
        if gen_len < 50:
            for i in range(16):
                k_len.append(random.randint(32, 126))

            for i in k_len:
                if i != 32:
                    complete += chr(i)
                elif i == 32:
                    complete += chr(126)

            self._key = complete

        elif gen_len >= 50:
            for i in range(32):
                k_len.append(random.randint(32, 126))

            for i in k_len:
                if i != 32:
                    complete += chr(i)
                elif i == 32:
                    complete += chr(126)

            self._key = complete

    def UserKey(self, temp_key):
        key_length = len(temp_key)
        if key_length < 16:
            print('The key must be either 16 or 32 bytes in length')

        elif key_length == 16:
            self._key = temp_key

        elif key_length == 32:
            self._key = temp_key
        return self._key

    def Encrypt_Message(self, text):
        text = self.__Pad(text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return base64.urlsafe_b64encode(iv + cipher.encrypt(text))

    def Decrypt_Message(self, text):
        cleaned = base64.urlsafe_b64decode(text)
        iv = cleaned[:AES.block_size]
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return self.__Unpad(cipher.decrypt(cleaned[AES.block_size:])).decode('utf-8')

    def Encrypt_File(self, path):
        with open(path, 'r') as inFile:
            plainText = inFile.read()
        plainText = self.__Pad(plainText)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return base64.urlsafe_b64encode(iv + cipher.encrypt(plainText))

    def Write_Encrypted(self, path, hidden):
        with open(path, 'wb') as outFile:
            outFile.write(hidden)
        return None

    def Decrypt_File(self, path):
        with open(path, 'rb') as seeFile:
            encryptedData = seeFile.read()
        cleaned = base64.urlsafe_b64decode(encryptedData)
        iv = cleaned[:AES.block_size]
        cipher = AES.new(self._key, AES.MODE_CBC, iv)
        return self.__Unpad(cipher.decrypt(cleaned[AES.block_size:])).decode('utf-8')

    def Write_Decrypted(self, path, text):
        with open(path, 'w') as mkFile:
            mkFile.write(str(text))
        return None

    def __Pad(self, text):
        return text + (self._block - len(text) % self._block) * chr(self._block - len(text) % self._block)

    def __Unpad(self, text):
        return text[:-ord(text[len(text) - 1:])]

    def RSA_Key_Gen(self):
        Afflicted.Security.rsa_key = RSA.generate(1024, Random.new().read)
        return self._rsa_key

    def Encrypt_Key(self, aes_key):
        key = self.RSA_Key_Gen()
        PubKey = key.publickey()
        return PubKey.encrypt(bytes(aes_key.encode()), 32)

    def Decrypt_Key(self, aes_key):
        return self.rsa_key.decrypt(aes_key)

    def write_key(self, path, aes_key):
        with open(path, 'w') as f:
            f.write(str(aes_key))
        return None

    def read_key(self, path):
        with open(path, 'rb') as inFile:
            hidden = inFile.read()
        return self.Decrypt_Key(hidden)
    #re-write Security using pynacl; PyCrypto has been dead for years now.

class AfflictedIO(object):

    def write(path, text):
        try:
            if os.path.isfile(path):
                return None
            else:
                with open(path, 'w') as outFile:
                    outFile.write(text)
        except IOError as exception:
            raise IOError("%s: %s" % (path, exception.strerror))
        return None

    def append(path, text):
        try:
            if os.path.isfile(path):
                with open(path, 'a') as outFile:
                    outFile.write(text)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def read(path):
        try:
            if os.path.isfile(path):
                with open(path, 'r') as inFile:
                    temp = inFile.read()
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return temp

    def write_b(path, text):
        try:
            if os.path.isfile(path):
                with open(path, 'wb') as outFile:
                    outFile.write(text)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def append_b(path, text):
        try:
            if os.path.isfile(path):
                with open(path, 'ab') as outFile:
                    outFile.write(text)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def read_b(path):
        try:
            if os.path.isfile(path):
                with open(path, 'rb') as inFile:
                    temp = inFile.read()
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return temp

    def get_line( path, number):
        try:
            if os.path.isfile(path):
                temp = linecache.getline(path, number)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return temp

    def create_file(Directory, file_name):
        temp = Directory + file_name
        try:
            if os.path.isdir(Directory):
                with open(temp, 'w') as outFile:
                    pass
        except IOError as exception:
            raise IOError('%s: %s' % (Directory, exception.strerror))
        return temp

    def create_folder(path):
        try:
            if os.path.isdir(path):
                pass
            else:
                os.makedirs(path)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def delete_file(path):
        try:
            if os.path.isfile(path):
                os.remove(path)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def delete_folder(path):
        try:
            if os.path.isdir(path):
                os.rmdir(path)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

    def find_string(path, text):
        try:
            if os.path.isfile(path):
                with open(path, 'r') as inFile:
                    for i, line in enumerate(inFile):
                        if text in line:
                            return text
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def get_line_number(path, text):
        try:
            if os.path.isfile(path):
                with open(path, 'r') as inFile:
                    for i, line in enumerate(inFile):
                        if text in line:
                            return str(i)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def get_total_lines(path):
        counter = 0
        try:
            if os.path.isfile(path):
                with open(path, 'r') as inFile:
                    for i in enumerate(inFile):
                        counter = counter + 1
            return str(counter)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def get_lines_before(path, line_number):
        try:
            final = ''
            counter = 0
            if os.path.isfile(path):
                while counter < line_number:
                    final += linecache.getline(path, counter)
                    counter += 1
                return final
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def get_lines_from(path, text, amount):
        main = 0
        final = ''
        counter = 0
        try:
            if os.path.isfile(path):
                with open(path, 'r') as inFile:
                    for i, line in enumerate(inFile):
                        if text in line:
                            main = i
                            break
                final = linecache.getline(path, main)
                main += 1
                while counter < amount:
                    final += linecache.getline(path, main)
                    main += 1
                    counter += 1
                return final
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def get_lines_after(path, line_number, amount):
        final = ''
        counter = 0
        num = line_number + 1
        try:
            if os.path.isfile(path):
                while counter < amount:
                    final += linecache.getline(path, num)
                    num += 1
                    counter += 1
                return final
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))

    def erase_specific_text(path, text, skip_num):
        final = ''
        slice_one = ''
        slice_two = ''
        maximum_lines = self.get_total_lines(path)
        break_line = self.get_line_number(path, text)
        slice_one = self.get_lines_before(path, int(break_line))
        second_run = int(maximum_lines) - int(break_line)
        second_start = int(break_line) + skip_num
        slice_two = self.get_lines_after(path, int(second_start), int(second_run))
        final = slice_one
        final += slice_two
        return final

    def create_dataframe_file(path): # creates a file like excel, or LibreOffice Calc etc.. blank for now
        pass

    def write_dataframes(path):
        try:
            if sys.platform == 'linux2':
                if os.path.isfile(path):
                    pass # do othing because the file exists
                elif not os.path.isfile(path):
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None],'Email': [None], 'Username': [None],
                                        'Password': [None]})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    writer.save()
            elif sys.platform == 'win32':
                if os.path.isfile(path):
                    pass
                elif not os.path.isfile(path):
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
                    writer = pd.ExcelWriter(path,engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    writer.save()
            elif sys.platform == 'darwin':
                if os.path.isfile(path): # this is not a mac
                    pass # do nothing because file exists
                elif not os.path.isfile(path): # this is not a mac
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    writer.save()
        except IOError as exception:
            raise IOError('%s: %s' % (exception.strerror))
        return None

    def append_dataframes(path, listing_text, website_text, email_text, user_text, password_text, description_text):
        try:
            if sys.platform == 'linux2':
                if os.path.isfile(path):
                    pass  # do othing because the file exists
                elif not os.path.isfile(path):
                    '''
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    writer.save()
                    '''
                    #df = pd.DataFrame(, columns = ('BCDEF'))
                    pass
            elif sys.platform == 'win32':
                if os.path.isfile(path):
                    pass
                elif not os.path.isfile(path):
                    #write shit
                    pass
            elif sys.platform == 'darwin':
                if os.path.isfile(path):  # this is not a mac
                    pass  # do nothing because file exists
                elif not os.path.isfile(path):  # this is not a mac
                   #write shit
                   pass
        except IOError as exception:
            raise IOError('%s: %s' % (exception.strerror))
        return None

i = AfflictedIO

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ApvLoadingScreen(Screen):

    def __init__(self, **kwargs):
        super(ApvLoadingScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.switch_screen_callback, 20.0)

    def switch_screen_callback(self, dt):
        try:
            if sys.platform == 'linux2':
                if os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    self.parent.current = 'main_screen'
                elif not os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    i.create_folder('/home/' + str(os.getlogin()) + './APV/')
                    i.write_dataframes('/home/' + str(os.getlogin()) + './APV/Private.xlsx')
                    self.parent.current = 'main_screen'
            elif sys.platform == 'win32':
                if os.path.isdir('C:\\APV\\'):
                    self.parent.current = 'main_screen'
                elif not os.path.isdir('C:\\APV\\'):
                    i.create_folder('C:\\APV\\')
                    i.write_dataframes('C:\\APV\\Private.xlsx')
                    self.parent.current = 'main_screen'
            elif sys.platform == 'dawrin': # not mac
                if os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    self.parent.current = 'main_screen'
                elif not os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    i.create_folder('/home/' + str(os.getlogin()) + './APV/')
                    i.write_dataframes('/home/' + str(os.getlogin()) + './APV/Private.xlsx')
                    self.parent.current = 'main_screen'
        except OSError as exception:
            raise OSError('%s: %s' % (exception.strerror))
        return None
        #self.parent.current = 'main_screen'

class ApvMainScreen(Screen):

    def __init__(self, **kwargs):
        super(ApvMainScreen, self).__init__(**kwargs)
        self.__temporary_list = list()

    def open_load_file_dialog(self):
        content = LoadDialog(load = self.load, cancel = self.dismiss_popup)
        self._popup = Popup(title = "Load file", content = content, size_hint = (0.9, 0.9))
        self._popup.open()

    def open_save_file_dialog(self):
        content = SaveDialog(save = self.save, cancel = self.dismiss_popup)
        self._popup = Popup(title = "Save file", content = content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        try:
            if sys.platform == 'win32':
                with open(os.path.join(path, filename[0])) as stream:
                    self.ids.viewport_output.text = stream.read()
            elif sys.platform == 'linux2':
                with open(os.path.join(path, filename[0])) as stream:
                    self.ids.viewport_output.text = stream.read()
            elif sys.platform == 'darwin':
                with open(os.path.join(path, filename[0])) as stream:
                    self.ids.viewport_output.text = stream.read()
            self.dismiss_popup()
        except OSError as exception:
            raise OSError("%s: %s" % (exception.strerror))

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.ids.viewport_output.text)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()

    def clear_text(self):
        self.ids.viewport_output.text = ''

    def set_listing_text(self):
        __listing = self.ids.listing_input.text
        self.__gen_dataframe(__listing)
        self.ids.listing_input.text = 'Listing: '

    def set_website_text(self):
        __website = self.ids.website_input.text
        self.__gen_dataframe(__website)
        self.ids.website_input.text = 'Website: '

    def set_email_text(self):
        __email = self.ids.email_input.text
        self.__gen_dataframe(__email)
        self.ids.email_input.text = 'Email Address: '

    def set_user_text(self):
        __usr = self.ids.username_input.text
        self.__gen_dataframe(__usr)
        self.ids.username_input.text = 'Username: '

    def set_password_text(self):
        __password = self.ids.password_input.text
        self.__gen_dataframe(__password)
        self.ids.password_input.text = 'Password: '

    def __gen_dataframe(self, text):
        self.__temporary_list.append(text)
        # self.__test_dataframe()
        # self.__write_list()

    def __write_list(self):
        if len(self.__temporary_list) == 5:
            print('clearing now')
            self.__clear_list()
            for i in self.__temporary_list:
                print(i)

    def __test_dataframe(self):
        for i in self.__temporary_list:
            print(i)

    def __clear_list(self):
        self.__temporary_list.clear()

class ApvSettingsScreen(Screen):
    pass

class ApvScreenManager(ScreenManager):
    pass


########################################################################################################################

root_widget = Builder.load_string('''
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import Config kivy.config
#:import Window kivy.core.window
#:import Clock kivy.clock
#:import ActionBar kivy.uix.actionbar
#:import Animation kivy.animation.Animation

ApvScreenManager:
    transition: FallOutTransition()
    ApvLoadingScreen:
    ApvMainScreen:
    ApvSettingsScreen:

<ApvLoadingScreen>:
    name: 'loading_screen'
    Image:
        size_hint: .5, .5
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        source: 'Images/hat.png'

<ApvMainScreen>:
    name: 'main_screen'
    TextInput:
        id: listing_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .85 }
        text: 'Listing: '
        multiline: False
        on_text_validate: root.set_listing_text()
    TextInput:
        id: website_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .75 }
        text: 'Website: '
        multiline: False
        on_text_validate: root.set_website_text()
    TextInput:
        id: email_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .65 }
        text: 'Email Address: '
        multiline: False
        on_text_validate: root.set_email_text()
    TextInput:
        id: username_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .55 }
        text: 'Username: '
        multiline: False
        on_text_validate: root.set_user_text()
    TextInput:
        id: password_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .45 }
        text: 'Password: '
        multiline: False
        on_text_validate: root.set_password_text()
    TextInput:
        id: viewport_output
        size_hint: .9, .9
        pos_hint: {'x': .30, 'y': .0 }
        text: ''
        multiline: True
        ##disabled: True ## Prevents scrolling too.
        
    ActionBar:
        pos_hint: {'top':1}
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'Menu'
                with_previous: False
            ActionOverflow:
            ActionButton:
                text: 'Open file'
                on_press: root.open_load_file_dialog()
            ActionButton:
                text: 'Encrypt'
                ##on_press:
            ActionButton:
                text: 'Decrypt'
                ##on_press: 
            ActionButton:
                text: 'Clear'
                on_release: root.clear_text()
            ActionButton:
                text: 'Export File'
                on_press: root.open_save_file_dialog()
            ActionGroup:
                text: 'Settings'
                ActionButton:
                    text: 'Print'
                ActionButton:
                    text: 'Provide Key'
                ActionButton:
                    text: 'Save Key'
                ActionButton:
                    text: 'Edit Listing'
                ActionButton:
                    text: 'Search Listing'
                ActionButton:
                    text: 'Advanced'
                    
                    
<LoadDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()
            Button:
                text: "Load"
                on_release: root.load(filechooser.path, filechooser.selection)
                

<SaveDialog>:
    text_input: text_input
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserListView:
            id: filechooser
            on_selection: text_input.text = self.selection and self.selection[0] or ''
        TextInput:
            id: text_input
            size_hint_y: None
            height: 30
            multiline: False
        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()
            Button:
                text: "Save"
                on_release: root.save(filechooser.path, text_input.text)
                
                
''')


########################################################################################################################
class ApvApp(App):
    def build(self):
        self.title = 'apv'
        return root_widget


ApvApp().run()