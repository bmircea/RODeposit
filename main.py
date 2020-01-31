import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.graphics.instructions import CanvasBase, Canvas
from kivy.graphics import Color, Rectangle
from kivy.event import EventDispatcher
from kivy.uix.textinput import TextInput

from time import sleep


class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)

        # Arranging Canvas
        with self.canvas:
            Color(1, 1, 1, 1)  # set the colour

            # Seting the size and position of canvas
            self.rect = Rectangle(pos=self.center,
                                  size=(self.width / 2.,
                                        self.height / 2.))

            # Update the canvas as the screen size change
            self.bind(pos=self.update_rect,
                      size=self.update_rect)

            # update function which makes the canvas adjustable.

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class LoginScreen(RelativeLayout):
    def on_enter(self, widget):
        self.passwordInput.focus = True

    def on_pressed(self, widget):
        print("butt pressed")



    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        userLabel = Label(text="[size=24][color=000000]Utilizator:[/color][/size]", markup=True, bold=True, pos_hint={"center_x":0.4, "center_y":.65})
        self.userInput = TextInput(text="", multiline=False, font_size="12dp", pos_hint={"center_x":.55, "center_y":.65}, size_hint=(0.14, None), height=27)
        passwordLabel = Label(text="[size=24][color=000000]Parola:[/color][/size]", markup=True, bold=True, pos_hint={"center_x":0.4, "center_y":.55})
        self.passwordInput = TextInput(text="", multiline=False, password=True, font_size="12dp", pos_hint={"center_x": .55, "center_y": .55}, size_hint=(0.14, None), height=27)



        self.userInput.bind(on_text_validate=self.on_enter)



        self.add_widget(userLabel)
        self.add_widget(self.userInput)
        self.add_widget(passwordLabel)
        self.add_widget(self.passwordInput)


class ToolScreenButton(Button):
    def __init__(self, **kwargs):
        super(ToolScreenButton, self).__init__(**kwargs)
        self.text = "Button"
        self.background_color = (1, 1, 1, 1)
        self.pos_hint = {"center_x":0.1, "center_y":0.9}
        self.size_hint = (0.1, 0.1)
        self.text_size = (self.width, self.height)


class ToolsScreen(RelativeLayout):
    def __init__(self, **kwargs):
        super(ToolsScreen, self).__init__(**kwargs)
        with self.canvas:

            Color(0, 0, 0)
            self.r = Rectangle(pos=(0, self.height/5*4) ,size=(self.width, self.height/5))

            self.bind(pos=self.update_rect, size=self.update_rect)






    def update_rect(self, *args):
        self.r.pos=(0, self.height/5*4)
        self.r.size=(self.width, self.height/5)





class MainApp(App):
    def on_login_pressed(self, widget):
        self.rem_wid_wrap(widget, self.lf)
        self.rem_wid_wrap(widget, self.logo)
        self.create_tools_screen()

    def create_tools_screen(self):
        self.ts = ToolsScreen()
        self.b1 = ToolScreenButton()
        self.b2 = ToolScreenButton()
        self.b3 = ToolScreenButton()

        #Position settings
        self.b1.pos_hint = {"center_x": .10, "center_y": .9}
        self.b2.pos_hint = {"center_x": .25, "center_y": .9}
        self.b3.pos_hint = {"center_x": .40, "center_y": .9}

        #Content settings
        self.b1.text = "Operatiuni"
        self.b2.text = "Situatii Stocuri"
        self.b3.text = "Setari"

        self.ts.add_widget(self.b1)
        self.ts.add_widget(self.b2)
        self.ts.add_widget(self.b3)

        self.rl.add_widget(self.ts)



    def create_login_screen(self, widget, item):
        self.lf = LoginScreen()
        self.loginButton = Button(text="Login", background_color=(0, 0, 0, 1),
                                  pos_hint={"center_x": .5, "center_y": .45}, size_hint=(0.14, None), height=27)
        self.loginButton.bind(on_press=self.on_login_pressed)
        self.lf.add_widget(self.loginButton)

        self.rl.add_widget(self.lf)

    def anim_logo(self, widget, item):
        mva = Animation(pos_hint={"center_x": .5, "center_y": .75}, duration=1.25)
        mva.bind(on_complete=self.create_login_screen)
        mva.start(self.logo)

    def rem_wid_wrap(self, widget, item):
        self.rl.remove_widget(item)

    def build(self):
        #Root Layout
        self.rl = RelativeLayout()
        #Canvas
        canvas = CanvasWidget()
        self.logo = Label(text="[size=40][color=da0404]ROD[/color][color=000000]eposit[/color][/size]", markup=True, bold=True, pos_hint={"center_x":.5, "center_y": .59})
        label = Label(text="[size=24][color=000000]Loading[/color][/size]", markup=True, bold=True, pos_hint={"center_x": .5, "center_y": .53}, opacity=0)


        #Add the widgets to the layout
        self.rl.add_widget(canvas)
        self.rl.add_widget(self.logo)
        self.rl.add_widget(label)



        #Fade in animation, on_complete bind and start
        fin = Animation(opacity=1, duration=2)
        fin.bind(on_complete=self.rem_wid_wrap) #Remove label from widget
        fin.bind(on_complete=self.anim_logo) #Animate the logo
        fin.start(label)





        return self.rl



if __name__ == '__main__':
    MainApp().run()