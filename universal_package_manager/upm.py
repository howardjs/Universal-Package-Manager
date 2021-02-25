# Third-party imports
import sys
from PySide6 import Qt
from PySide6 import QtWidgets

# Arrays
package_managers = [
    "apt",
    "dnf",
    "eopkg",
    "flatpak",
    "pacman",
    "zypper"
]

def main():
    # Define QApplication
    app = QtWidgets.QApplication(sys.argv)
    
    # Define QMainWindow
    window = QtWidgets.QMainWindow()
    window.setFixedSize(800, 600)

    # Show widgets
    window.show()

    # Bind exit call
    sys.exit(app.exec_())

# Run main
main()