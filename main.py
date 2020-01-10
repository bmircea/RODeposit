import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.animation import Animation
import kivy.event

from time import sleep


class LoadingScreen(RelativeLayout):
    pass




class MainApp(App):
    def animate(self, instance):  #Animate the Loading... text
        #Define fadein and fadeout animations
        fout = Animation(opacity=0, duration=2)
        fin = Animation(opacity=1, duration=2)

        #Run the animations
        fout.start(instance)
        instance.text="[size=24]Loading..[/size]"
        fin.start(instance)
        fout.start(instance)
        instance.text = "[size=24]Loading...[/size]"
        fin.start(instance)

    def build(self):
        ls = LoadingScreen()
        label = Label(text="[size=24]Loading.[/size]", markup=True, bold=True, pos_hint={"center_x": .5, "center_y": .53}, on_press = self.animate)
        ls.add_widget(label)
        return ls



if __name__ == '__main__':
    MainApp().run()