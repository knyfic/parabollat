#!/bin/bash

pip install pygobject matplotlib numpy

echo "[Desktop Entry]
Name=Parabollat
Exec=python3 $HOME/.local/share/parabollat/parabollat.py
Icon=$HOME/.local/share/parabollat/parabollat.png
Terminal=false
Type=Application
Categories=GTK;Application;" > parabollat.desktop

 cp parabollat.desktop $HOME/.local/share/applications/
 
 chmod +755 $HOME/.local/share/parabollat.py

echo "installation complete.please do not change the directory where you installed the app. otherwise the application will not work.desktop has been created, you can open the parabollota from your application menu.
"

