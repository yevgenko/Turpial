# -*- coding: utf-8 -*-

# Clase para manejar todas las notificaciones de Turpial
#
# Author: Wil Alvarez (aka Satanas)
# Dic 27, 2009

import util
import logging

log = logging.getLogger('Notify')

class Notification:
    def __init__(self):
        self.activate()
        
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def popup(self, title, message, icon=None):
        try:
            import pynotify
            self.integrated = True
        except:
            log.debug("pynotify is not installed")
            self.integrated = False
        
        if self.active:
            if pynotify.init("Turpial"):
                if not icon:
                    icon = util.load_image('turpial_icon_48.png', True)
                else:
                    icon = util.load_image(icon, True)
                n = pynotify.Notification(title, message)
                n.set_icon_from_pixbuf(icon)
                n.show()
                
    def new_tweets_home(self, count):
        if count > 0:
            self.popup('Actualizado timeline', '%i tweets nuevos' % count)