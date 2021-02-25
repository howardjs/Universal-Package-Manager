import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="universal-package-manager",
    version="0.0.5",
    author="Garrett Howard",
    author_email="garrett@mersh.com",
    description="A unified graphical interface for Linux package managers such as apt, pacman, zypper, etc.",
    url="https://github.com/howardjs/Universal-Package-Manager",
    packages=['universal_package_manager'],
    entry_points = {
        'console_scripts' : ['upm=upm:main']
    },
    data_files = [
        ('share/applications', ['upm.desktop'])
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6'
)
