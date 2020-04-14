#!/bin/bash

#AI_Model_Creator; an easy to use AI cumputer vision model creator.
#Copyright (C) 2020  Jonas Mayer

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by    
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#You can contact me by mail: bysuxaxofficial@gmail.com

filepath=$1
echo $filepath
PKGS=(python3.6 python3-venv)
  
echo Check if Everything reqired is installed


for ((i=0 ;i < ${#PKGS[@]};i++))
do
    
    PKG_OK=$(dpkg-query -W --showformat='${Status}\n' ${PKGS[$i]} |grep "install ok installed") 
    echo Checking for ${PKGS[$i]}: $PKG_OK
    if [ "" == "${PKG_OK}" ]; then
    echo "Package is not installed. Install: ${PKGS[$i]}"
    sudo apt-get --force-yes --yes install ${PKGS[$i]}
    fi
    
done

cd $filepath
python3 -m venv ./VirtualPython3

. VirtualPython3/bin/activate
cp ./activate_this.py ./VirtualPython3/bin/activate_this.py
cd ./VirtualPython3
pip3 install Pillow==6.2.2
pip3 install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

PKGS="pyqt5==5.14.2 google_images_download==2.8.0"

echo Check if all python libarys are installed...

pip3 install pip==20.0.2 setuptools==46.1.3

pip3 install ${PKGS}
cd ..
mkdir Pics 
mkdir Models


