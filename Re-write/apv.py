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
from pandas import ExcelWriter
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
import xlrd
from openpyxl import load_workbook


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
                    self.create_folder('/home/' + str(os.getlogin()) + './APV/')
                    self.create_excel_document('/home/' + str(os.getlogin()) + './APV/Private.xlsx')
                    self.parent.current = 'main_screen'
            elif sys.platform == 'win32':
                if os.path.isdir('C:\\APV\\'):
                    self.parent.current = 'main_screen'
                elif not os.path.isdir('C:\\APV\\'):
                    self.create_folder('C:\\APV\\')
                    self.create_excel_document('C:\\APV\\Private.xlsx')
                    self.parent.current = 'main_screen'
            elif sys.platform == 'dawrin': # not mac
                if os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    self.parent.current = 'main_screen'
                elif not os.path.isdir('/home/' + str(os.getlogin()) + './APV/'):
                    self.create_folder('/home/' + str(os.getlogin()) + './APV/')
                    self.create_excel_document('/home/' + str(os.getlogin()) + './APV/Private.xlsx')
                    self.parent.current = 'main_screen'
        except OSError as exception:
            raise OSError('%s: %s' % (exception.strerror))
        return None
        #self.parent.current = 'main_screen'

    def create_excel_document(self, path):
        try:
            if sys.platform == 'linux2':
                if os.path.isdir(path):
                    if os.path.isfile(path + 'Private.xlsx'): # .ods for linux so this should be changed
                        pass
                    elif not os.path.isfile(path):
                        df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                            'Password': [None]})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35) #
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
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
                        df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                            'Password': [None]})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35)
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
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
                        df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                            'Password': [None]})
                        writer = pd.ExcelWriter(path, engine='xlsxwriter')
                        df1.to_excel(writer, sheet_name='Accounts')
                        workbook = writer.book
                        worksheet1 = writer.sheets['Accounts']
                        worksheet1.set_column(1, 5, 35)
                        writer.save()
                elif not os.path.isdir(path):
                    df1 = pd.DataFrame({'Listing': [None], 'Website': [None], 'Email': [None], 'Username': [None],
                                        'Password': [None]})
                    writer = pd.ExcelWriter(path, engine='xlsxwriter')
                    df1.to_excel(writer, sheet_name='Accounts')
                    workbook = writer.book
                    worksheet1 = writer.sheets['Accounts']
                    worksheet1.set_column(1, 5, 35)
                    writer.save()
        except IOError as exception:
            raise IOError('%s: %s' % (exception.strerror))
        return None

    def create_ods_document(self, path):
        pass # finish this

    def create_folder(self, path):
        try:
            if os.path.isdir(path):
                pass
            else:
                os.makedirs(path)
        except IOError as exception:
            raise IOError('%s: %s' % (path, exception.strerror))
        return None

class ApvMainScreen(Screen):

    def __init__(self, **kwargs):
        super(ApvMainScreen, self).__init__(**kwargs)

        self.__listing_list = list()
        self.__Website_list = list()
        self.__Email_list = list()
        self.__User_list = list()
        self.__password_list = list()

        self.__win = 'C:\\APV\\Private.xlsx'
        self.__linux = '/home/' + str(os.getlogin()) + './APV/Private.xlsx'
        self.__mac = '/home/' + str(os.getlogin()) + './APV/Private.xlsx' # wrong

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
        if sys.platform == 'linux2':
            __listing = self.ids.listing_input.text
            self.__listing_list.append(__listing)
            self.ids.listing_input.hint_text = 'Listing: '
        elif sys.platform == 'win32':
            __listing = self.ids.listing_input.text
            self.__listing_list.append(__listing)
            self.ids.listing_input.hint_text = 'Listing: '
        elif sys.platform == 'darwin':
            __listing = self.ids.listing_input.text
            self.__listing_list.append(__listing)
            self.ids.listing_input.hint_text = 'Listing: '

    def set_website_text(self):
        if sys.platform == 'linux2':
            __website = self.ids.website_input.text
            self.__Website_list.append(__website)
            self.ids.website_input.hint_text = 'Website: '
        elif sys.platform == 'win32':
            __website = self.ids.website_input.text
            self.__Website_list.append(__website)
            self.ids.website_input.hint_text = 'Website: '
        elif sys.platform == 'darwin':
            __website = self.ids.website_input.text
            self.__Website_list.append(__website)
            self.ids.website_input.hint_text = 'Website: '

    def set_email_text(self):
        if sys.platform == 'linux2':
            __email = self.ids.email_input.text
            self.__Email_list.append(__email)
            self.ids.email_input.hint_text = 'Email Address: '
        elif sys.platform == 'win32':
            __email = self.ids.email_input.text
            self.__Email_list.append(__email)
            self.ids.email_input.hint_text = 'Email Address: '
        elif sys.platform == 'darwin':
            __email = self.ids.email_input.text
            self.__Email_list.append(__email)
            self.ids.email_input.hint_text = 'Email Address: '

    def set_user_text(self):
        if sys.platform == 'linux2':
            __usr = self.ids.username_input.text
            self.__User_list.append(__usr)
            self.ids.username_input.hint_text = 'Username: '
        elif sys.platform == 'win32':
            __usr = self.ids.username_input.text
            self.__User_list.append(__usr)
            self.ids.username_input.hint_text = 'Username: '
        elif sys.platform == 'darwin':
            __usr = self.ids.username_input.text
            self.__User_list.append(__usr)
            self.ids.username_input.hint_text = 'Username: '

    def set_password_text(self):
        if sys.platform == 'linux2':
            __password = self.ids.password_input.text
            self.__password_list.append(__password)
            self.append_and_write_dataframes(self.__linux)
            self.ids.password_input.hint_text = 'Password: '
        elif sys.platform == 'win32':
            __password = self.ids.password_input.text
            self.__password_list.append(__password)
            self.append_and_write_dataframes(self.__win)
            self.ids.password_input.hint_text = 'Password: '
        elif sys.platform == 'darwin':
            __password = self.ids.password_input.text
            self.__password_list.append(__password)
            self.append_and_write_dataframes(self.__mac)
            self.ids.password_input.hint_text = 'Password: '

    def test_read(self):
        df = pd.read_excel(self.__win, sheet_name='Accounts')
        temp = pd.DataFrame.to_string(df)
        s = temp.replace('NaN', '')
        s = s.replace('[', '')
        s = s.replace(']', '')
        self.ids.viewport_output.text = str(s)

    def append_and_write_dataframes(self, path):
        df = pd.read_excel(path, sheet_name='Accounts')
        df1 = pd.DataFrame({'Listing': [self.__listing_list], 'Website': [self.__Website_list],
                            'Email': [self.__Email_list], 'Username': [self.__User_list], 'Password': [self.__password_list]})
        df3 = df.append(df1)
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df3.to_excel(writer, sheet_name='Accounts')
        workbook = writer.book
        worksheet1 = writer.sheets['Accounts']
        worksheet1.set_column(1, 5, 35)
        writer.save()
        self.__listing_list.clear()  #
        self.__Website_list.clear()
        self.__Email_list.clear()
        self.__User_list.clear()
        self.__password_list.clear()

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
        hint_text: 'Listing: '
        multiline: False
        on_focus: listing_input.text = ''
        on_text_validate: root.set_listing_text()
        text_validate_unfocus: True
    TextInput:
        id: website_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .75 }
        hint_text: 'Website: '
        multiline: False
        on_focus: website_input.text = ''
        on_text_validate: root.set_website_text()
        text_validate_unfocus: True
    TextInput:
        id: email_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .65 }
        hint_text: 'Email Address: '
        multiline: False
        on_focus: email_input.text = ''
        on_text_validate: root.set_email_text()
        text_validate_unfocus: True
    TextInput:
        id: username_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .55 }
        hint_text: 'Username: '
        multiline: False
        on_focus: username_input.text = ''
        on_text_validate: root.set_user_text()
        text_validate_unfocus: True
    TextInput:
        id: password_input
        size_hint: .3, .05
        pos_hint: {'x': 0, 'y': .45 }
        hint_text: 'Password: '
        multiline: False
        password: True
        on_focus: password_input.text = ''
        on_text_validate: root.set_password_text()
        text_validate_unfocus: True
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
            ActionButton: ## remove
                text: 'Test read' ## remove
                on_press: root.test_read() ## remove
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