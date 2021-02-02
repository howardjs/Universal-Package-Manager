import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="universal-package-manager",
    version="0.0.1",
    author="Garrett Howard",
    author_email="garrett@mersh.com",
    description="A unified graphical interface for Linux package managers such as apt, pacman, zypper, etc.",
    url="https://github.com/howardjs/Universal-Package-Manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6'
)