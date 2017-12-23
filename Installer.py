import sys
import os
import kivy
import fnmatch
import Afflicted
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


class Installer(object):
    _win_dir = 'C:\\Password Vault\\'    
    _linux_dir = '/home/' + os.getlogin() + '/.APV/'	
   	

    
    def write_user(self, event):
       	if sys.platform == 'win32':
            _temp_u = username_input.text
	    _temp_p = self._win_dir + '\\' + _temp_u
	    _temp_uname = _temp_u + '.txt'	
	    os.makedirs(_temp_p)		
	    file = open(_temp_p + _temp_uname, 'w')
	    file.close()
	    file = open(_temp_p + 'Logs.txt', 'w')
	    file.close()
	    file = open(_temp_p + 'Authorized User.txt', 'w')
	    file.close()
	    with open(_temp_p + 'Authorized User.txt', 'a') as file:
	        file.write(_temp_u + '\n')
		file.close()
            _temp_s = 'Sucess files have been generated in: ' + _temp_p + '\n'	 		
	    display_window.text = _temp_s
	    p_bar.value = 50	
	    username_input.text = ''
	    return None
	elif sys.platform == 'linux2':
	    _temp_u = username_input.text
	    _temp_p = self._linux_dir + _temp_u
	    _temp_uname = _temp_u + '.txt'
	    os.makedirs(_temp_p)
	    file = open(_temp_p + '/' + _temp_uname, 'w')
	    file.close()		
	    file = open(_temp_p + '/' + 'Logs.txt', 'w')
	    file.close()
            file = open(_temp_p + '/' + 'Authorized User.txt', 'w')
	    file.close()
	    with open(self.walk_directories(self._linux_dir, 'Authorized User.txt'), 'a') as file:
                file.write(_temp_u + '\n')
		file.close()
	    _temp_s = 'Sucess files have been generated in: ' + _temp_p + '\n'	 		
	    display_window.text = _temp_s
	    p_bar.value = 50
	    username_input.text = ''
	    return None



    def write_password(self, event):
        if sys.platform == 'win32':
	    _temp_p = password_input.text
	    _temp_s = self.walk_directories(self._win_dir, 'Authorized User.txt')
	    with open(temp_s, 'a') as file: 
	        file.write(_temp_p)
		file.close()
	    p_bar.value = 90	
	    display_window.text = 'Success: User account has been created'
	    password_input.text = ''
	    return None
		
	elif sys.platform == 'linux2':
	    _temp_p = password_input.text
	    _temp_s = self.walk_directories(self._linux_dir, 'Authorized User.txt')
	    with open(_temp_s, 'a') as file:
		file.write(_temp_p)
		file.close()
		p_bar.value = 90
		display_window.text = 'Success: User account has been created'
            	password_input.text = ''
	        return None	

    def finalize(self, event):
	if sys.platform == 'win32':
  	    _temp_s = self.walk_directories(self._win_dir, 'Authorized User.txt')
	    _temp_f = Crypto.Encrypt_File(_temp_s)
	    Crypto.Write_Encrypted(_temp_s, _temp_f)
	    p_bar.value = 100
	    display_window.text = 'Setup is complete, you can now run the main program! \n\nWhen promted to log in please enter the following decryption key\n\n' + Crypto._key + '\n\nThis is a one time key, you wont have to worry about it ever again!'
	    return None
	
	elif sys.platform == 'linux2':
	    _temp_s = self.walk_directories(self._linux_dir, 'Authorized User.txt')	
	    _temp_f = Crypto.Encrypt_File(_temp_s)
	    Crypto.Write_Encrypted(_temp_s, _temp_f)
	    p_bar.value = 100
	    display_window.text = 'Setup is complete, you can now run the main program! \n\nWhen promted to log in please enter the following decryption key\n\n' + Crypto._key + '\n\nThis is a one time key, you wont have to worry about it ever again!'
	    return None

    def walk_directories(self, Dir, pattern):
	root = Dir	
	for root, directories, files in os.walk(Dir):
	    for basename in files:
	        if fnmatch.fnmatch(basename, pattern):
		    _file_path = os.path.join(root, basename)
	return _file_path



# Installer class Instantiation
I = Installer()

############################################################################################################################################################################################################################################
#Widgets
Root = Widget(size = (250, 250)) #Main widget

username_input = TextInput(pos = (0, 220), size = (200, 30), hint_text = ('Create Username: '), multiline = (False))
username_input.bind(on_text_validate = I.write_user)

password_input = TextInput(pos = (0,190), size = (200, 30), hint_text = ('Create Password: '), multiline = (False))
password_input.bind(on_text_validate = I.write_password)

p_bar = ProgressBar(pos = (0, 1), size = (250, 5))
display_window = TextInput(pos = (239, 0), size = (310, 249))

encrypt_button = Button(text = ('Encrypt Files'), pos = (0, 140), size = (100, 30))
encrypt_button.bind(on_press = I.finalize)


Root.add_widget(username_input)
Root.add_widget(password_input)
Root.add_widget(p_bar)
Root.add_widget(display_window)
Root.add_widget(encrypt_button)
############################################################################################################################################################################################################################################
#BEGIN MAIN CLASS
class InstallerApp(App):
    def build(self):     
        return Root
#END MAIN CLASS
############################################################################################################################################################################################################################################



############################################################################################################################################################################################################################################
#BEGIN MAIN
Window.size = (550, 250)
if __name__ == '__main__':
    Crypto = Afflicted.Afflicted().Security()
    Crypto.UserKey(';tY-U3(V)(8Q3FU"7?$`?19]Y`0`cA#7')	
    InstallerApp().run()    
#END MAIN
############################################################################################################################################################################################################################################
    

