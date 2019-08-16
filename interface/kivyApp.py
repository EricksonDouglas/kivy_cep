from kivy.app  import App
from kivy.core.window                       import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
import re
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition

import sys
sys.path.append("..")
from libs.validador import Validador


Window.size = (500, 300)
Config.set('graphics', 'resizable', False)
Config.write()

class FloatInput(TextInput):
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

class Tela1(Screen):
    name: "menu"
    def bt_validar(self):
        result = Validador.cep(self.ids["cep"].text)
        if result:
            if result["valido"] == 1:
                self.manager.ids["result"].ids["lb_result"].text = "{} É Valido".format(self.ids["cep"].text).center(20)
                self.manager.ids["result"].ids["lb_result"].font_size = "50"
            else:
                if len(result["repetitivo"])==1:
                    text = "{} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                elif len(result["repetitivo"])==2:
                    if result["repetitivo"][0] == result["repetitivo"][1]:
                        text = "{} é um digito repetitivo alternado em par".format(result["repetitivo"][0])
                    else:
                        text = "os números {r[0]} e {r[1]} são digito repetitivo alternado em par".format(r=result["repetitivo"])

                self.manager.ids["result"].ids["lb_result"].text = "[size=50][b]{}[/b][/size]\n{}".format(str(self.ids["cep"].text+"- Não é valido").center(100),text)
                self.manager.ids["result"].ids["lb_result"].font_size = "15"

            self.manager.current = 'result'

        else:
            self.ids["lb_menu"].text = "-> CEP Inválido <-"




class Tela2(Screen):
    name: "result"
    def volta_tela(self):
        self.manager.ids["menu"].ids["cep"].text = ""
        self.manager.ids["menu"].ids["lb_menu"].text = ""
        self.manager.current = "menu"

class ScreenManagement(ScreenManager): pass
class ValidadorAPP(App): pass




if __name__ == '__main__': ValidadorAPP().run()
