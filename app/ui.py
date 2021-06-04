from kivy.app import App
from kivy.base import ExceptionHandler
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

import os
import shutil
import app.script

Builder.load_file('MyLayout.kv')

Window.size = (650, 500)
Window.title = 'Converter'

# class E(ExceptionHandler)

class MyLayout(Widget):

    def selected(self, dirname):
        app.script.yourpath = dirname[0]

    def pressed(self, wpercent, quality, size):
        try:
            new_folder = os.path.join(app.script.yourpath[:app.script.yourpath.rfind('\\') + 1], 'jpgimgs')
            if os.path.exists(new_folder):
                new_folder = os.path.join(new_folder, size)
                if os.path.exists(new_folder):
                    shutil.rmtree(new_folder)
                    os.mkdir(new_folder)
                else:
                    os.mkdir(new_folder)
            else:
                os.mkdir(new_folder)
                new_folder = os.path.join(new_folder, size)
                os.mkdir(new_folder)
            app.script.convert(wpercent, quality, new_folder)
        except:
            print('Choose correct folder!')


class Application(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    Application().run()
