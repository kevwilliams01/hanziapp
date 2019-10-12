import kivy
import pytesseract
from PIL import Image
from dragonmapper import hanzi
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserListView
import time
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
font_path = r"C:\Users\KevanWilliams\Downloads\simsun.ttc"
font_path2 = r"C:\Users\KevanWilliams\Downloads\pinyin.TTF"



class StartScreen(Screen):
    pass




class MyWidget(BoxLayout):
    #text_input = ObjectProperty(None)
    #text_output = ObjectProperty(None)









    def open(self, path, filename):
        f = open(os.path.join(path, filename[0]))
        print(f)


    def selected(self, filename):

        image = Image.open(os.path.join(filename[0]))
        code_spaced = pytesseract.image_to_string(image, lang='chi_sim')
        word = hanzi.to_pinyin(code_spaced)
        from kivy.uix.label import Label
        self.clear_widgets()
        self.add_widget(Label(text=code_spaced, font_name=font_path))
        self.add_widget(Label(text=word, font_name=font_path2))

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_" + timestr)
        print("Captured")





class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):

        return kv



if __name__ == "__main__":
    MyApp().run()