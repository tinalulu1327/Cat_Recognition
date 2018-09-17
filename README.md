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
python export_inference_graph.py \
--input_type image_tensor \
--pipeline_config_path /mnt/models/research/faster_rcnn_inception_v2_pets.config \
--trained_checkpoint_prefix /mnt/models/research/faster_R-CNN_mine/model.ckpt-5723 \
--output_directory /mnt/models/research/object_detection/pbfile


4. Image prediction
Exe dir: /mnt/models/research/object_detection
python Object_detection_image.py


----
DataSet dir：
/mnt/models/dataset/dataset.tar.gz
