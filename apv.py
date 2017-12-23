import sys
import math
import os
import datetime
import threading
import socket
import base64
from Crypto.Cipher import AES
from Crypto import Random
import linecache
import hashlib
import Afflicted
import fileinput
import kivy
from kivy.uix.textinput import TextInput
from  kivy.uix.label import Label
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




'''
This section contains the main class, apv '''

class apv(object):


    
    _win_dir_one = 'C:\\APV\\'
    _win_path_one = 'C:\\APV\\Private.txt'

    _win_dir_two = 'C:\\Afflicted Password Storage\\'
    _win_path_two = 'C:\\Afflicted Password Storage\\Private.txt'

    _linux_dir_one = '/home/' '''+ os.getlogin()''' + '/.APV/'
    _linux_path_one = '/home/' '''+ os.getlogin()''' + '/.APV/Private.txt'

    _linux_dir_two = '/home/' '''+ os.getlogin()''' + '/.Afflicted Password Storage/'
    _linux_path_two = '/home/' '''+ os.getlogin()''' + '/.Afflicted Password Storage/Private.txt'

    _encryption_time = 0
    _decryption_time = 0

    _deletion_time = 0
    _save_edit_time = 0

    _default = ''
    _usr_supplied = ''

    def default_key(self):
        temp_usr = len(A._usr_supplied)
        temp_default = len(A._default)
        if temp_usr is None and temp_default is None:
            A._default = Crypto.gen_aes_key

        elif temp_default is None and temp_usr is not None:
            pass
        
            
            
    
    @staticmethod
    def get_text(text):
        return_text = text
        return return_text


    @staticmethod
    def set_listing_text(listing):
        listingInput.text = listing
        listingInput.cursor =(0,0)
        return None


    @staticmethod
    def set_website_text(web):
        websiteInput.text = web
        websiteInput.cursor = (0,0)
        return None


    @staticmethod
    def set_email_text(mail):
        emailInput.text = mail
        emailInput.cursor = (0,0)
        return None


    @staticmethod
    def set_user_text(usr):
        userInput.text = usr
        userInput.cursor = (0,0)
        return None
    

    @staticmethod
    def set_password_text(pwd):
        passwordInput.text = pwd
        passwordInput.cursor = (0,0)
        return None


    @staticmethod
    def set_description_text(des):
        descriptionInput.text = des
        descriptionInput.cursor = (0,0)
        return None


    @staticmethod
    def current_time(self, increment):
        percent = increment
        if percent < 100:
            return current_time(increment + 1)
        elif percent == 100:
            return percent
 

    def clear_display(self):
        displayWindow.text = ''
        return None


    
    def write_listing(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Listing name: ' + apv.get_text(listingInput.text) + '\n')
                    apv.set_listing_text('')    

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'a') as file:
                        file.write('Listing name: ' + apv.get_text(listingInput.text) + '\n')
                    apv.set_listing_text('')


            elif sys.platform  == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'a') as file:
                        file.write('Listing name: ' + apv.get_text(listingInput.text) + '\n')
                    apv.set_listing_text('')
                    
                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'a') as file:
                        file.write('Listing name: ' + apv.get_text(listingInput.text) + '\n')
                    apv.set_listing_text('')

        except OSError:
            pass

        return None




    def write_website(self, event):
        try:
            if sys.platform  == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Website name: ' + apv.get_text(websiteInput.text) + '\n')
                    apv.set_website_text('')     

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'a') as file:
                        file.write('Website name: ' + apv.get_text(websiteInput.text) + '\n')
                    apv.set_website_text('')    




            elif sys.platform  == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'a') as file:
                        file.write('Website name: ' + apv.get_text(websiteInput.text) + '\n')
                    apv.set_website_text('')    

                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'a') as file:
                        file.write('Website name: ' + apv.get_text(websiteInput.text) + '\n')
                    apv.set_website_text('')    

        except OSError:
            pass

        return None




    def write_email(self, event):
        try:
            if sys.platform  == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Email address: ' + apv.get_text(emailInput.text) + '\n')
                    apv.set_email_text('')    
                        

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'a') as file:
                        file.write('Email address: ' + apv.get_text(emailInput.text) + '\n')
                    apv.set_email_text('')    




            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'a') as file:
                        file.write('Email address: ' + apv.get_text(emailInput.text) + '\n')
                    apv.set_email_text('')    

                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'a') as file:
                        file.write('Email address: ' + apv.get_text(emailInput.text) + '\n')
                    apv.set_email_text('')    

        except OSError:
            pass

        return None




    def write_user(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Username: ' + apv.get_text(userInput.text) + '\n')
                    apv.set_user_text('')    

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'a') as file:
                        file.write('Username: ' + apv.get_text(userInput.text) + '\n')
                    apv.set_user_text('')    




            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'a') as file:
                        file.write('Username: ' + apv.get_text(userInput.text) + '\n')
                    apv.set_user_text('')    

                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'a') as file:
                        file.write('Username: ' + apv.get_text(userInput.text) + '\n')
                    apv.set_user_text('')    

        except OSError:
            pass

        return None




    def write_password(self, event):
        try:
            if sys.platform  == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Password: ' + apv.get_text(passwordInput.text) + '\n')
                    apv.set_password_text('')    

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'a') as file:
                        file.write('Password: ' + apv.get_text(passwordInput.text) + '\n')
                    apv.set_password_text('')    




            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'a') as file:
                        file.write('Password: ' + apv.get_text(passwordInput.text) + '\n')
                    apv.set_password_text('')    

                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'a') as file:
                        file.write('Password: ' + apv.get_text(passwordInput.text) + '\n')
                    apv.set_password_text('')    

        except OSError:
            pass

        return None




    def write_description(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'a') as file:
                        file.write('Description: ' + apv.get_text(descriptionInput.text) + '\n \n \n \n')
                    apv.set_description_text('')    

                elif os.path.isdir(apv._win_dir_two):
                     with open(apv._win_path_two, 'a') as file:
                         file.write('Description: ' + apv.get_text(descriptionInput.text) + '\n \n \n \n')
                     apv.set_description_text('')    
                    




            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                     with open(apv._linux_path_one, 'a') as file:
                        file.write('Description: ' + apv.get_text(descriptionInput.text) + '\n \n \n \n')
                     apv.set_description_text('')    

                elif os.path.isdir(apv._linux_dir_two):
                     with open(apv._linux_path_two, 'a') as file:
                         file.write('Description: ' + apv.get_text(descriptionInput.text) + '\n \n \n \n')
                     apv.set_description_text('')    

        except OSError:
            pass

        return None




    def display_all(self):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'rb') as inFile:
                        string = inFile.read()
                        displayWindow.text = string

                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'rb') as inFile:
                        string = inFile.read()
                        displayWindow.text = string


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'rb') as inFile:
                        string = inFile.read()
                        displayWindow.text = string

                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'rb') as inFile:
                        string = inFile.read()
                        displayWindow.text = string

        except OSError:
            pass

        return None




    def delete_all(self):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    if os.path.exists(apv._win_path_one):
                        os.remove(apv._win_path_one)
                    if os.path.exists('C:\\Afflicted Password Storage\\Supplied.txt'):
                        os.remove('C:\\Afflicted Password Storage\\Supplied.txt')
                    os.rmdir(apv._win_dir_one)

                elif os.path.isdir(apv._win_dir_two):
                    if os.path.exists(apv._win_path_two):
                        os.remove(apv._win_path_two)
                    if os.path.exists('C:\\Afflicted Password Storage\\Supplied.txt'):
                        os.remove('C:\\Afflicted Password Storage\\Supplied.txt')
                    os.rmdir(apv._win_dir_two)

            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    if os.path.exists(apv._linux_path_one):
                        os.remove(apv._linux_path_one)
                    if os.path.exists('/home/' + os.getlogin() + '/.APV/Supplied.txt'):
                        os.remove('/home/' + os.getlogin() + '/.APV/Supplied.txt')
                    os.rmdir(apv._linux_dir_one)

                elif os.path.isdir(apv._linux_dir_two):
                    if os.path.exists(apv._linux_path_two):
                        os.remove(apv._linux_path_two)
                    if os.path.exists('/home/' + os.getlogin() + '/.Afflicted Password Storage/Supplied.txt'):    
                        os.remove('/home/' + os.getlogin() + '/.Afflicted Password Storage/Supplied.txt')
                    os.rmdir(apv._linux_dir_two)

        except OSError:
            pass

        return None




    def search_specific(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    locate = apv.get_text(searchInput.text)
                    with open(apv._win_path_one, 'r') as inFile:
                        t = 0
                        str1 = ""
                        str2 = ""
                        str3 = ""
                        str4 = ""
                        str5 = ""
                        str6 = ""

                        for i, line in enumerate(inFile):
                            if locate in line:
                                str1 = line
                                i = i + 1
                                t = i
                                break

                    t = t + 1    
                    str2 = linecache.getline(_win_path_one, t)
                    

                    t = t + 1
                    str3 = linecache.getline(_win_path_one, t)

                    t = t + 1
                    str4 = linecache.getline(_win_path_one, t)

                    t = t + 1
                    str5 = linecache.getline(_win_path_one, t)

                    t = t + 1
                    str6 = linecache.getline(_win_path_one, t)

                    final = str1 + str2 + str3 + str4 + str5 + str6
                    displayWindow.text = final     


                elif os.path.isdir(apv._win_dir_two):
                    locate = apv.get_text(searchInput.text)
                    with open(apv._win_path_two, 'r') as inFile:
                        t = 0
                        str1 = ""
                        str2 = ""
                        str3 = ""
                        str4 = ""
                        str5 = ""
                        str6 = ""

                        for i, line in enumerate(inFile):
                            if locate in line:
                                str1 = line
                                i = i + 1
                                t = i
                                break

                    t = t + 1    
                    str2 = linecache.getline(_win_path_two, t)
                    

                    t = t + 1
                    str3 = linecache.getline(_win_path_two, t)

                    t = t + 1
                    str4 = linecache.getline(_win_path_two, t)

                    t = t + 1
                    str5 = linecache.getline(_win_path_two, t)

                    t = t + 1
                    str6 = linecache.getline(_win_path_two, t)

                    final = str1 + str2 + str3 + str4 + str5 + str6
                    displayWindow.text = final     


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    locate = apv.get_text(searchInput.text)
                    with open(apv._linux_path_one, 'r') as inFile:
                        t = 0
                        str1 = ""
                        str2 = ""
                        str3 = ""
                        str4 = ""
                        str5 = ""
                        str6 = ""

                        for i, line in enumerate(inFile):
                            if locate in line:
                                str1 = line
                                i = i + 1
                                t = i
                                break

                    t = t + 1    
                    str2 = linecache.getline(_linux_path_one, t)
                    

                    t = t + 1
                    str3 = linecache.getline(_linux_path_one, t)

                    t = t + 1
                    str4 = linecache.getline(_linux_path_one, t)

                    t = t + 1
                    str5 = linecache.getline(_linux_path_one, t)

                    t = t + 1
                    str6 = linecache.getline(_linux_path_one, t)

                    final = str1 + str2 + str3 + str4 + str5 + str6
                    displayWindow.text = final     


                elif os.path.isdir(apv._linux_dir_two):
                    locate = apv.get_text(searchInput.text)
                    with open(apv._linux_path_two, 'r') as inFile:
                        t = 0
                        str1 = ""
                        str2 = ""
                        str3 = ""
                        str4 = ""
                        str5 = ""
                        str6 = ""

                        for i, line in enumerate(inFile):
                            if locate in line:
                                str1 = line
                                i = i + 1
                                t = i
                                break

                    t = t + 1    
                    str2 = linecache.getline(_linux_path_two, t)
                    

                    t = t + 1
                    str3 = linecache.getline(_linux_path_two, t)

                    t = t + 1
                    str4 = linecache.getline(_linux_path_two, t)

                    t = t + 1
                    str5 = linecache.getline(_linux_path_two, t)

                    t = t + 1
                    str6 = linecache.getline(_linux_path_two, t)

                    final = str1 + str2 + str3 + str4 + str5 + str6
                    displayWindow.text = final     


        except OSError:
            pass

        return None




    def edit_specific(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    with open(apv._win_path_one, 'r') as inFile:
                        string = inFile.read()
                        displayWindow.text = string


                elif os.path.isdir(apv._win_dir_two):
                    with open(apv._win_path_two, 'r') as inFile:
                        string = inFile.read()
                        displayWindow.text = string
                    


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    with open(apv._linux_path_one, 'r') as inFile:
                        string = inFile.read()
                        displayWindow.text = string


                elif os.path.isdir(apv._linux_dir_two):
                    with open(apv._linux_path_two, 'r') as inFile:
                        string = inFile.read()
                        displayWindow.text = string

        except OSError:
            pass

        return None




    def save_edit(self, event):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    string = apv.get_text(displayWindow.text)
                    with open(apv._win_path_one, 'w') as outFile:
                        outFile.write(string)


                elif os.path.isdir(apv._win_dir_two):
                    string = apv.get_text(displayWindow.text)
                    with open(apv._win_path_two, 'w') as outFile:
                        outFile.write(string)


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    string = apv.get_text(displayWindow.text)
                    with open(apv._linux_path_one, 'w') as outFile:
                        outFile.write(string)


                elif os.path.isdir(apv._linux_dir_two):
                    string = apv.get_text(displayWindow.text)
                    with open(apv._linux_path_two, 'w') as outFile:
                        outFile.write(string)

        except OSError:
            pass

        return None




    def supplied_key(self, event):
        try:
            tempKey = apv.get_text(keyInput.text)
            length = len(tempKey)
            if length == 32:
                Crypto.UserKey(tempKey)
                displayWindowtext('Write this key down somewhere if you lost it you wont be able to recover your data\nYou must input this key every time you run the program')

            elif length != 32:
                displayWindow.text('Your key must be 32 characters long\nExample: !@#$fd^7B&^4fb<.ZXA~`Fg>;:{[_-)(')

        except OSError:
            pass

        return None




    def print_file(self):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    os.startfile(apv._win_path_one, 'print')


                elif os.path.isdir(apv._win_dir_two):
                    os.startfile(apv._win_path_two, 'print')


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    pass


                elif os.path.isdir(apv._linux_dir_two):
                    pass

        except OSError:
            pass

        return None




    def secure_key(self):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    secure = Crypto.Encrypt_Key(self.key)
                    Crypto.write_key(apv._win_path_one, secure)


                elif os.path.isdir(apv._win_dir_two):
                    secure = Crypto.Encrypt_Key(self.key)
                    Crypto.write_key(apv._win_path_two, secure)
                    


            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    secure = Crypto.Encrypt_Key(self.key)
                    Crypto.write_key(apv._linux_path_one, secure)


                elif os.path.isdir(apv._linux_dir_two):
                    secure = Crypto.Encrypt_Key(self.key)
                    Crypto.write_key(apv._linux_path_two, secure)

        except OSError:
            pass

        return None




    def encrypt(self):
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    Secured = Crypto.Encrypt_File(apv._win_path_one)
                    Crypto.Write_Encrypted(apv._win_path_one, Secured)
                    timeBar.value = 100

                elif os.path.isdir(apv._win_dir_two):
                    Secured = Crypto.Encrypt_File(apv._win_path_two)
                    Crypto.Write_Encrypted(apv._win_path_two, Secured)
                    timeBar.value = 100
                    

            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    Secured = Crypto.Encrypt_File(apv._linux_path_one)
                    Crypto.Write_Encrypted(apv._linux_path_one, Secured)
                    timeBar.value = 100

                elif os.path.isdir(apv._linux_dir_two):
                    Secured = Crypto.Encrypt_File(apv._linux_path_two)
                    Crypto.Write_Encrypted(apv._linux_path_two, Secured)
                    timeBar.value = 100


        except OSError:
            pass

        return None
        




    def decrypt(self):
        
        try:
            if sys.platform == 'win32':
                if os.path.isdir(apv._win_dir_one):
                    Cleaned = Crypto.Decrypt_File(apv._win_path_one)
                    Crypto.Write_Decrypted(apv._win_path_one, Cleaned)
                    timeBar.value = 100
     

                elif os.path.isdir(apv._win_dir_two):
                    Cleaned = Crypto.Decrypt_File(apv._win_path_two)
                    Crypto.Write_Decrypted(apv._win_path_two, Cleaned)
                    timeBar.value = 100

            elif sys.platform == 'linux2':
                if os.path.isdir(apv._linux_dir_one):
                    Cleaned = Crypto.Decrypt_File(apv._linux_path_one)
                    Crypto.Write_Decrypted(apv._linux_path_one, Cleaned)
                    timeBar.value = 100

                elif os.path.isdir(apv._linux_dir_two):
                    Cleaned = Crypto.Decrypt_File(apv._linux_path_two)
                    Crypto.Write_Decrypted(apv._linux_path_two, Cleaned)
                    timeBar.value = 100


        except OSError:
            pass

        return None



    def Pick(self, sender, val):
        Search = False
        val = fileMenu.text
        if val == 'Display All':
            searchInput.opacity = 0
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            self.display_all()
            

        if val == 'Search Specific':
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
           
            searchInput.opacity = 1


        if val == 'Print':
            searchInput.opacity = 0
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            A.print_file()
            

        if val == 'File':
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            searchInput.opacity = 0
           
            searchInput.text = ""


        if val == 'Provide Key':
            keyInput.opacity = 1


        if val == 'Save Key':
            a.secure_key()
    
        return None




    def Pick2(self, sender, val):
        val = editMenu.text
        if val == 'Delete All':
            searchInput.opacity = 0
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            self.delete_all()

        if val == 'Edit Specific':
            searchInput.opacity = 0
            save_Edit_Button.opacity = 1
            display_button.opacity = 1
            a.edit_specific
            

        if val == 'Edit':
            searchInput.opacity = 0
            save_Edit_Button.opacity = 0
            display_button.opacity = 0


        if val == 'Encrypt':
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            A.encrypt()

                       
        if val == 'Decrypt':
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            A.decrypt()


        if val == 'Decrypt':
            save_Edit_Button.opacity = 0
            display_button.opacity = 0
            A.clear_display()


        
        return None            

A = apv()   
#############################################################################################################################################################################################################################################

'''
Now it's time to build the ui setup the main ui class and main method
'''

############################################################################################################################################################################################################################################
#TEXT INPUT SETUP
listingInput = TextInput(pos = (0, 395), size = (210, 30), hint_text = ("Listing name"), multiline = (False))
listingInput.bind(on_text_validate = A.write_listing)



websiteInput = TextInput(pos = (0, 355), size = (210, 30), hint_text = ("Website"), multiline = (False))
websiteInput.bind(on_text_validate = A.write_website)



emailInput = TextInput(pos = (0, 315), size = (210, 30), hint_text = ("Email address"), multiline = (False))
emailInput.bind(on_text_validate = A.write_email)



userInput = TextInput(pos = (0, 275), size = (210, 30), hint_text = ("Username"), multiline = (False))
userInput.bind(on_text_validate = A.write_user)



passwordInput = TextInput(pos = (0, 235), size = (210, 30), hint_text = ("Password"), multiline = (False))
passwordInput.bind(on_text_validate = A.write_password)



descriptionInput = TextInput(pos = (0, 195), size = (210, 30), hint_text = ("Description"), multiline = (False))
descriptionInput.bind(on_text_validate = A.write_description)


displayWindow = TextInput(pos = (250, 30), size = (620, 470))


searchInput = TextInput(pos = (0, 155), size = (210, 30), hint_text = ("Enter listing name"), multiline = (False))
searchInput.bind(on_text_validate = A.search_specific)
searchInput.opacity = 0



keyInput = TextInput(pos = (0, 0), size = (270, 30), hint_text = ("Enter 32 character key"), multiline = (False))
keyInput.opacity = 0
keyInput.bind(on_text_validate = A.supplied_key)


timeBar = ProgressBar(pos = (0, 390), size = (250, 100))
#END TEXT INPUT SETUP
############################################################################################################################################################################################################################################


############################################################################################################################################################################################################################################
#BEGIN SPINNER SETUP
fileMenu = Spinner(text = 'File', values = ('File', 'Display All', 'Print', 'Search Specific', 'Provide Key', 'Save Key'), size = (120, 44), pos = (0, 460))
fileMenu.bind(text = A.Pick)

editMenu = Spinner(text = 'Edit', values = ('Edit', 'Edit Specific',  'Delete All', 'Encrypt', 'Decrypt', 'Clear display'), size = (120, 44), pos = (121, 460))
editMenu.bind(text = A.Pick2)

save_Edit_Button = Button(text = ('Save'), pos = (120, 140), size = (100, 30))
save_Edit_Button.bind(on_press = A.save_edit)
save_Edit_Button.opacity = 0

display_button = Button(text = ('Display'), pos = (0, 140), size = (100, 30))
display_button.bind(on_press = A.edit_specific)
display_button.opacity = 0
#END SPINNER SETUP
############################################################################################################################################################################################################################################


############################################################################################################################################################################################################################################
#BEGIN ROOT WINDOW
Root = Widget(size = (890, 505))
Root.add_widget(listingInput)
Root.add_widget(websiteInput)
Root.add_widget(emailInput)
Root.add_widget(userInput)

Root.add_widget(passwordInput)
Root.add_widget(descriptionInput) 
Root.add_widget(displayWindow)
Root.add_widget(fileMenu)
Root.add_widget(editMenu)
Root.add_widget(searchInput)
Root.add_widget(keyInput)
Root.add_widget(save_Edit_Button)
Root.add_widget(display_button)
Root.add_widget(timeBar)
#END ROOT WINDOW
############################################################################################################################################################################################################################################
#END UI DECLERATION
############################################################################################################################################################################################################################################




############################################################################################################################################################################################################################################
#BEGIN MAIN CLASS
class PasswordApp(App):
    def build(self):     
        return Root
#END MAIN CLASS
############################################################################################################################################################################################################################################



############################################################################################################################################################################################################################################
#BEGIN MAIN
Window.size = (890, 505)
if __name__ == '__main__':
    #Crypto = Afflicted.Afflicted().Security('!@#$%^&*90_+|\]}[{;:.,<>/?`~AS2c')
    Crypto = Afflicted.Afflicted().Security()
    A.default_key()
    PasswordApp().run()    
#END MAIN
############################################################################################################################################################################################################################################
    
