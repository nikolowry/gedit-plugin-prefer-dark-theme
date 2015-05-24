from gi.repository import GObject, Gedit, Gtk

class PreferDarkThemePlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "PreferDarkPlugin"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", True)

    def do_deactivate(self):
        Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", False)

    def do_update_state(self):
        pass
