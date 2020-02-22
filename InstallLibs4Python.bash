#!/bin/bash

filepath= realpath

PKGS=(python-pip3 python3 python3-venv python-catkin-tools)
  
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
cd ./VirtualPython3

PKGS="opencv-python pandas rospkg catkin_pkg pyqt5"

echo Check if all python libarys are installed...

pip3 install --upgrade pip setuptools

pip3 install ${PKGS}


pip3 uninstall -y pyyaml

echo $filepath/VirtualPython3/lib/python3.6/site-packages
export PYTHONPATH=$PYTHONPATH:$filepath/VirtualPython3/lib/python3.6/site-packages
mkdir catkin_build_ws && cd catkin_build_ws
catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so

catkin config --install

mkdir src
cd src
git clone -b melodic https://github.com/ros-perception/vision_opencv.git
cd ..

catkin build cv_bridge
source install/setup.bash --extend
mv install/lib/python3/dist-packages ../lib/python3.6/dist-packages
rm -rf ../catkin_build_ws
cd ../..

pip3 install pyyaml

