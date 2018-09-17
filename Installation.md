# Cloud Server preparation

## NecTaR instance creation
[OS]
NeCTAR Ubuntu 17.10 (Artful) amd64

## Necessary Software Installation

# update system
sudo apt-get update
sudo apt-get -y upgrade
# install git
sudo apt-get install git

# install tensorflow
https://www.tensorflow.org/install/install_linux#use_pip_in_a_virtual_environment
mkdir ./tensorflow
cd tensorflow/
virtualenv --system-site-packages -p python3 venv
source ./venv/bin/activate
pip install --upgrade pip
pip install --upgrade tensorflow
(venv)$ python -c "import tensorflow as tf; print(tf.__version__)"

# install tensorflow object detector
sudo apt-get install protobuf-compiler python-pil python-lxml python-tk
pip install --user Cython
pip install --user contextlib2
pip install --user jupyter
pip install --user matplotlib

git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make

git clone https://github.com/tensorflow/models.git
cd models/

cp -r ~/cocoapi/PythonAPI/pycocotools ../../models/research/
cd ../../models/research/
# check whether Installation is ok
protoc object_detection/protos/*.proto --python_out=.

# install pillow
pip install pillow

export PYTHONPATH=$PYTHONPATH:/mnt/models/research:/mnt/models/research/slim
python object_detection/builders/model_builder_test.py

# install numpy
sudo apt-get install python-numpy

## How to use X2go
sudo service x2goserver start

## command to change filename
ls British_S* | rename 's#British_S#British_s'##g

## issue with Oxford dataset
not all the images have bound box information !!!

## Python output to log
python -u finetune.py | tee log
