#!/bin/bash
python3 setup.py sdist bdist_wheel
sudo python setup.py --command-packages=stdeb.command bdist_deb
