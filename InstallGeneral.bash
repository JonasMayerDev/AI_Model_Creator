#!/bin/bash

filepath=$1
echo $filepath
PKGS=(python3 python3-venv)
  
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

PKGS="pyqt5 google_images_download"

echo Check if all python libarys are installed...

pip3 install --upgrade pip setuptools

pip3 install ${PKGS}
cd ..
mkdir Pics 
mkdir Models


