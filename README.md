![UPM Logo](https://github.com/howardjs/Unified-Package-Manager/blob/main/media/logos/upm_centered.png)

# The Universal Package Manager (UPM)

[![Github All Releases](https://img.shields.io/github/downloads/howardjs/Universal-Package-Manager/total.svg)](https://github.com/howardjs/Universal-Package-Manager/releases)
[![GitHub release](https://img.shields.io/github/release/howardjs/Universal-Package-Manager/all.svg)](https://github.com/howardjs/Universal-Package-Manager/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date/howardjs/Universal-Package-Manager.svg)](https://github.com/howardjs/Universal-Package-Manager/releases)
[![GitHub license](https://img.shields.io/github/license/howardjs/Universal-Package-Manager.svg)](https://github.com/howardjs/Universal-Package-Manager/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/howardjs/Universal-Package-Manager.svg)](https://github.com/howardjs/Universal-Package-Manager/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/howardjs/Universal-Package-Manager.svg)](https://github.com/howardjs/Universal-Package-Manager/network)

## Overview

The Universal Package Manager is a utility that provides simplified use of multiple widely-used package managers on Linux-based systems. This software was written for newcomers to the Linux package management utilities who don't want to get involved with the command-line interface but has become an all-in-one tool for Linux package management across many services and distributions.

The software is written in [Python](https://www.python.org/) using the [GTK](https://gtk.org/) widget toolkit in conjunction with the [PyGObject](https://pygobject.readthedocs.io/) package for Python graphical applications. This project is open-source and uses the [GNU General Public License v3.0](https://github.com/howardjs/Universal-Package-Manager/blob/main/LICENSE).

## Package manager support

The Universal Package Manager will support the following package managers:


  - [apt](https://en.wikipedia.org/wiki/APT_(software)) (Debian-based operating systems)

  - [dnf](https://en.wikipedia.org/wiki/DNF_(software)) (Fedora-based operating systems)

  - [eopkg](https://github.com/solus-project/package-management) (Solus, a Debian-based operating system)

  - [flatpak](https://en.wikipedia.org/wiki/Flatpak) (Multiple Linux-based operating systems)

  - [pacman](https://en.wikipedia.org/wiki/Arch_Linux#Pacman) (Arch-based operating systems)

  - [snap](https://en.wikipedia.org/wiki/Snap_(package_manager)) (Multiple Linux-based operating systems)

  - [zypper](https://en.wikipedia.org/wiki/ZYpp) (openSUSE-based operating systems)


## Installation

### Prerequisites

  - A [Linux](https://en.wikipedia.org/wiki/Linux)-based operating system

  - [Python 3.6](https://www.python.org/downloads/) or above

### Install as a Python Package (recommended)

```
pip install universal-package-manager
```

### Download and install from binary releases

#### Debian-based operating systems

- Download the `.deb` file from the [latest release](https://github.com/howardjs/Universal-Package-Manager/releases/latest).
- Run `sudo dpkg -i upm-latest.deb` in a terminal.
- You can now run UPM by your application launcher or by typing `upm` in a terminal.

#### Other operating systems

- Download the source code from the [latest release](https://github.com/howardjs/Universal-Package-Manager/releases/latest) and unzip the file.
- Download and install the dependencies with `pip install -r requirements.txt`
- Install the package with `python3 setup.py install`

### Build and install from the source repository

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

## Community

You can interact with the UPM community by joining our official Discord server!

[The UPM Discord Server](https://discord.gg/6s3Cgk9EGR)

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/howardjs/Universal-Package-Manager/blob/main/LICENSE). This project is available for commercial use, modification, distribution, patent use, and private use.
