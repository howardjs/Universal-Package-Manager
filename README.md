![UPM Logo](https://github.com/howardjs/Unified-Package-Manager/blob/main/media/logos/upm_centered.png)

# The Universal Package Manager (UPM)

## Overview

The Universal Package Manager is a utility that provides simplified use of multiple widely-used package managers on Linux-based systems. This software was written for newcomers to the Linux package management utilities who don't want to get involved with the command-line interface but has become an all-in-one tool for Linux package management across many services and distributions.

The software is written in Python using the GTK widget toolkit in conjunction with the PyGObject package for Python graphical applications. This project is open-source and uses the [GNU General Public License v3.0](https://github.com/howardjs/Universal-Package-Manager/blob/main/LICENSE).

## Package manager support

The Universal Package Manager will support the following package managers:


  - apt (Debian-based operating systems)

  - flatpak (Multiple Linux-based operating systems)

  - pacman (Arch-based operating systems)

  - snap (Multiple Linux-based operating systems)

  - yum (Fedora-based operating systems)

  - zypper (openSUSE-based operating systems)


## Installation

### Prerequisites

  - A Linux-based operating system

  - Python 3 or above

### Install as a Python Package

```
pip install universal-package-manager
```

### Install from the source repository

Clone the GitHub repository:

```
git clone https://github.com/howardjs/Universal-Package-Manager.git
```

After you clone the repository, install all of the requirements:

```
pip install -r requirements.txt
```

Finally, install the package:

```
python3 setup.py install
```


## Contributing

Pull requests are encouraged. For major changes with the project please open an issue about what you would like to change. Thank you for contributing to the UPM project.

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/howardjs/Universal-Package-Manager/blob/main/LICENSE). This project is available for commercial use, modification, distribution, patent use, and private use.
