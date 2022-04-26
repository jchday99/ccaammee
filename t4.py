from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: 'vertical'
    size: root.size

    Camera:
        id: camera
        resolution: (720,1280)
        play: False
        canvas.before:
            PushMatrix
            Rotate:
                angle: -90
                origin: self.center
        canvas.after:
            PopMatrix

    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
'''


class TestCamera(App):

    def build(self):
        return Builder.load_string(kv)


TestCamera().run()