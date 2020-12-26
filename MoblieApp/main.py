
from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.animation import Animation 
from kivy.uix.behaviors import ButtonBehavior 
from hoverable import HoverBehavior

import json ,glob,random
from datetime import datetime
from pathlib import Path


Builder.load_file('design.kv')  

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        
    def login(self,uname,pword):
        with open("users.json") as f: 
            users = json.load(f) 
        if uname in users and users[uname]['password']==pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or Password"

class SignUpScreen(Screen): 
    def add_user(self,uname,pword): 
        with open("users.json","r") as f: 
            users = json.load(f)
        print(users)
        users[uname] = {"username":uname,"password":pword,"created":datetime.now().strftime("%y-%m-%d %H-%M-%S")} 
        with open("users.json","w") as f: 
            users = json.dump(users,f)

        self.manager.current = "sign_up_succss"
    
       
class SignUpScucuss(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen" 

class LoginScreenSuccess(Screen):
    def get_qoutes(self,feling):
        feling =feling.lower()
        avaliable_feling = glob.glob('qoutes/*txt')  
        avaliable_feling = [Path(filename).stem for 
                           filename in avaliable_feling] 
        for feling in avaliable_feling:
            with open(f"qoutes/{feling}.txt") as f:
                qoutes = f.readlines() 
                print(random.choice(qoutes)) 
            self.ids.quotes.text = random.choice(qoutes)  
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen" 

class ImageButten(ButtonBehavior,HoverBehavior,Image):
    pass

class RootWidget(ScreenManager):  
    pass 


class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()  


