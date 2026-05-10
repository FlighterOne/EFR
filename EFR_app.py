from kivy.lang import Builder

from kivymd.app import MDApp


class Example(MDApp):
    def build(self):
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:

        MDBottomNavigationItem:
            name: 'Food'
            text: 'Food'
            icon: ''

            MDLabel:
                text: 'Your foods notes'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'Training'
            text: 'Training'
            icon: ''

            MDLabel:
                text: 'Your trainings notes'
                halign: 'center'
                
        MDBottomNavigationItem:
            name: 'Tracker'
            text: 'Tracker'
            icon: ''

            MDLabel:
                text: 'Your tracker'
                halign: 'center'
                
        MDBottomNavigationItem:
            name: 'Settings'
            text: 'Settings'
            icon: ''

            MDLabel:
                text: 'Settings'
                halign: 'center'
'''
        )


Example().run()