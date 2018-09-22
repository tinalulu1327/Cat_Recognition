# How to use Object detection
1. TFRecorder transfer：
Exe dir：/mnt/models/research
python object_detection/dataset_tools/create_pet_tf_record.py \
--label_map_path=object_detection/data/pet_label_map.pbtxt \
--data_dir=`pwd` \
--output_dir=`pwd`

2. Model Trainning
Exe dir：/mnt/models/research
python object_detection/legacy/train.py --logtostderr --pipeline_config_path=faster_rcnn_inception_v2_pets.config --train_dir=./faster_R-CNN_mine/


3. Import Model
Exe dir: /mnt/models/research/object_detection
cd object_detection/
python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path /mnt/tensorflow/models/pbfile/faster_rcnn_resnet101_pets.config --trained_checkpoint_prefix /mnt/tensorflow/models/Train_resnet/model.ckpt-8293 --output_directory /mnt/tensorflow/models/pbfile


4. Image prediction
source /mnt/tensorflow/venv/bin/activate
cd pbfile
python ./research/object_detection/Object_detection_image.py 

5. Evaluation
Exe dir: /mnt/models/research/object_detection
python3 legacy/eval.py --logtostderr --train_dir=../../Train_resnet/ --pipeline_config_path=../../pbfile_resnet/faster_rcnn_resnet101_pets.config --checkpoint_dir=../../Train_resnet/ --eval_dir=/mnt


----
DataSet dir：
/mnt/models/dataset/dataset.tar.gz

