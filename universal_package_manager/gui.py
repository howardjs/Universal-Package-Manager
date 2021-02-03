# Third-party imports
import gi
import os

# Initialize GTK
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Arrays
package_managers = [
    "apt",
    "pacman",
    "yum",
    "zypper"
]

class GtkWindow(Gtk.Window):

    def __init__(self):
        # Create Gtk.Window instance
        Gtk.Window.__init__(self, title="The Universal Package Manager")
        self.set_default_size(800, 600)

        # Create package manager selector widgets
        self.package_manager_selector_box = Gtk.Box(spacing=10)
        self.package_manager_selector_box.set_margin_left(10)
        self.package_manager_selector_box.set_margin_top(10)
        self.package_manager_selector_label = Gtk.Label()
        self.package_manager_selector_label.set_label("Package Manager:")
        self.package_manager_selector_label.set_size_request(30,30)
        self.package_manager_selector_label.set_halign(Gtk.Align.START)
        self.package_manager_selector_label.set_valign(Gtk.Align.START)
        self.package_manager_selector_box.pack_start(self.package_manager_selector_label, False, True, 1)
        self.package_manager_selector = Gtk.ComboBoxText()
        self.package_manager_selector.set_entry_text_column(0)
        self.package_manager_selector.set_size_request(100, 30)
        self.package_manager_selector.set_halign(Gtk.Align.START)
        self.package_manager_selector.set_valign(Gtk.Align.START)
        for package_manager in package_managers:
            self.package_manager_selector.append_text(package_manager)
        self.package_manager_selector.set_active(0)
        self.package_manager_selector_box.pack_start(self.package_manager_selector, False, True, 1)

        # Add widgets to the window
        self.add(self.package_manager_selector_box)

        # Show the window
        self.show_all()
        self.connect("destroy", Gtk.main_quit)
        Gtk.main()

    # Button has been clicked
    def button_clicked(self, widget):
        print("Clicked!")