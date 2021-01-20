from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout, MDNavigationDrawer
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import OneLineListItem, OneLineRightIconListItem, MDList, IconRightWidget, TwoLineListItem
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.textfield import MDTextField
from kivy.core.audio import SoundLoader
import os
import random


class MenuScreen(Screen):
    def __init__(self, main_app, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.main_app = main_app
        scroll = ScrollView()
        lst = MDList()
        lst.add_widget(OneLineListItem(text='Screen 1', on_press=self.change_screen))
        lst.add_widget(OneLineListItem(text='Screen 2', on_press=self.change_screen))
        scroll.add_widget(lst)
        self.add_widget(scroll)

    def change_screen(self, btn):
        if btn.text == 'Screen 1':
            self.main_app.sm.current = 'screen1'
        elif btn.text == 'Screen 2':
            self.main_app.sm.current = 'screen2'


class Screen1(Screen):
    def __init__(self, main_app, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.main_app = main_app
        self.add_widget(MDLabel(text='Screen 1'))


class Screen2(Screen):
    def __init__(self, main_app, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.main_app = main_app
        self.add_widget(MDLabel(text='Screen 2'))


class MusicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(self, name='menu'))
        self.sm.add_widget(Screen1(self, name='screen1'))
        self.sm.add_widget(Screen2(self, name='screen2'))
        return self.sm


if __name__ == '__main__':
    MusicApp().run()
