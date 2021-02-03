![UPM Logo](https://github.com/howardjs/Unified-Package-Manager/blob/main/media/logos/upm_centered.png)

# The Universal Package Manager (UPM)

## Overview

The Universal Package Manager is a utility that provides simplified use of multiple widely-used package managers on Linux-based systems.

## Package manager support

The Universal Package Manager will support the following package managers:


  - apt (Debian-based operating systems)

  - flatpak (Multiple Linux-based operating systems)

  - pacman (Arch-based operating systems)

  - snap (Multiple Linux-based operating systems)

  - yum (Fedora-based operating systems)

  - zypper (openSUSE-based operating systems)


## Installation

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
