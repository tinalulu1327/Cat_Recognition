# Cat-Breed
## caffe Installation
[Note]
Before using NecTaR to install Caffe, remember to execute "sudo apt-get update".

[Environment]
Ubuntu 17.04

[Installation]
sudo apt-get update
sudo apt-get install git
mkdir caffe
cd caffe/
git clone https://github.com/BVLC/caffe.git
cd caffe/

sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
sudo apt install caffe-cpu

mkdir build
cd build/
sudo apt install cmake
sudo apt-get install libatlas-base-dev
sudo apt-get install python-numpy
cmake ..
make all
make install
make runtest


## How to install tensorflow object detector
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

cp -r pycocotools ../../models/research/
cd ../../models/research/
protoc object_detection/protos/*.proto --python_out=.

sudo vim ~/.bashrc
( Add line: export PYTHONPATH=$PYTHONPATH:/mnt/models/research:/mnt/models/research/slim
source ~/.bashrc
python object_detection/builders/model_builder_test.py

## command to change filename
ls British_S* | rename 's#British_S#British_s'##g

## issue with Oxford dataset
not all the images have bound box information !!!

## Python output to log
python -u finetune.py | tee log


## use VNC to connect VM
# server
vncserver -geometry 1024x768 -depth 24

# client
# use "Screen Sharing" of MAC

## Flicker API
Key: 13ef101ff4bac39647acb5531d8d0a3c
Secret: 7e873f75e2dc8214

## Flicker image collection
python ImageCollection_Flicker.py /mnt/COMP90055/Dataset/ImageCollection

## Connect to server
ssh -i TreeRecognition.key ubuntu@43.240.99.95
