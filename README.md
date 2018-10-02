# How to use Object detection
1. TFRecorder transfer：
Exe dir：/mnt/models/research
python object_detection/dataset_tools/create_pet_tf_record.py \
--label_map_path=object_detection/data/pet_label_map.pbtxt \
--data_dir=`pwd` \
--output_dir=`pwd`

mkdir ../output_final
(venv) root@cat-final:/mnt/tensorflow/models/research# python3 object_detection/dataset_tools/create_pet_tf_record.py --label_map_path=../pbfile/pet_label_map.pbtxt --data_dir=../dataset --output_dir=../output_final

2. Model Trainning
Exe dir：/mnt/models/research
screen python3 object_detection/legacy/train.py --logtostderr --pipeline_config_path=../pbfile/ssd_inception_v2_pets.config --train_dir=../train_ssd_inceptionv2/


3. Import Model
Exe dir: /mnt/models/research/object_detection
cd object_detection/
python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path /mnt/tensorflow/models/pbfile/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix /mnt/tensorflow/models/train_ssd_mobilenet/model.ckpt-0 --output_directory /mnt/tensorflow/models/pbfile

python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path /mnt/models/ssd_resnet_fpn/pipeline.config --trained_checkpoint_prefix /mnt/models/ssd_resnet_fpn/model.ckpt-25000 --output_directory /mnt/tensorflow/jupyter/pbfile_ssd_fpn/

python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path /mnt/tensorflow/jupyter/pbfile_ssd_mobilenet_v1_fpn_0.5/pipeline.config --trained_checkpoint_prefix /mnt/tensorflow/jupyter/pbfile_ssd_mobilenet_v1_fpn_0.5/model.ckpt-25000 --output_directory /mnt/tensorflow/jupyter/pbfile_ssd_mobilenet_v1_fpn_0.5/


!!!!!! Import tensorflow lite model !!!!!!!!
python object_detection/export_tflite_ssd_graph.py \
--pipeline_config_path=/mnt/tensorflow/models/pbfile/ssd_inception_v2_pets.config \
--trained_checkpoint_prefix=/mnt/tensorflow/models/train_ssd_inceptionv2_test/model.ckpt-22204 \
--output_directory=/mnt/tensorflow/models/train_ssd_inceptionv2_test/frozen_graph.pb \
--add_postprocessing_op=true

python object_detection/export_tflite_ssd_graph.py \
--pipeline_config_path=/mnt/models/ssd_mobilenet_v1_fpn_test/pipeline.config \
--trained_checkpoint_prefix=/mnt/models/ssd_mobilenet_v1_fpn_test/model.ckpt-25000 \
--output_directory=/mnt/models/ssd_mobilenet_v1_fpn_test/lite/frozen_graph.pb \
--add_postprocessing_op=true


4. Image prediction
source /mnt/tensorflow/venv/bin/activate
cd pbfile
python ./research/object_detection/Object_detection_image.py 

5. Evaluation
Exe dir: /mnt/models/research/object_detection
python3 legacy/eval.py --logtostderr --train_dir=../../Train_resnet/ --pipeline_config_path=../../pbfile_resnet/faster_rcnn_resnet101_pets.config --checkpoint_dir=../../Train_resnet/ --eval_dir=/mnt

screen python3 object_detection/model_main.py    --pipeline_config_path=../pbfile_resnet_2018_01/faster_rcnn_resnet101_pets.config    --model_dir=../Train_resnet_2018_01/    --num_train_steps=100    --num_eval_steps=30    --alsologtostderr

6. Use tensorboard
pip3 show tensorflow
cd /root/.local/lib/python3.6/site-packages/tensorboard
screen python3 main.py --logdir=/mnt/tensorflow/models/train_ssd_inception_v2/

7. Convert to tensorflow lite
toco \
--graph_def_file=pbfile/ssd_mobilenet_v1_pets.config \
--output_file=pbfile/optimized_graph.lite \
--output_format=TFLITE \
--input_shape=1,300,300,3 \
--input_array=input \
--output_array=final_result \
--inference_type=FLOAT \
--inference_input_type=FLOAT

8. Install bazel (analyse 'summarize_graph' )
sudo apt-get install openjdk-8-jdk
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install bazel
sudo apt-get upgrade bazel
sudo apt install python3-numpy python3-dev python3-pip python3-wheel

# create summarize_graph
bazel build tensorflow/tools/graph_transforms:transform_graph
bazel-bin/tensorflow/tools/graph_transforms/summarize_graph --in_graph=/mnt/models/ssd_mobilenet_v1_fpn_test/lite/frozen_graph.pb/tflite_graph.pb 

# create tensorflow lite files
bazel run -c opt tensorflow/contrib/lite/toco:toco --  \
--input_file=/mnt/tensorflow/models/pbfile/tflite_graph.pb \
--output_file=/mnt/tensorflow/models/pbfile/optimized_graph.lite \
--output_format=TFLITE \
--input_shape=1,300,300,3  \
--input_array=normalized_input_image_tensor \
--output_array='TFLite_Detection_PostProcess'  \
--inference_type=FLOAT \
--mean_value=128 \
--std_value=128 \
--change_concat_input_ranges=false \
--allow_custom_ops

----
DataSet dir：
/mnt/models/dataset/dataset.tar.gz

jupyter notebook  --port=8889

pip install tensorflow-hub


bazel run -c opt tensorflow/contrib/lite/toco:toco --  \
--input_file=/mnt/tensorflow/models/train_ssd_inceptionv2_test/frozen_graph.pb/tflite_graph.pb \
--output_file=/mnt/tensorflow/models/train_ssd_inceptionv2_test/frozen_graph.pb/optimized_graph.lite \
--output_format=TFLITE \
--input_shape=1,300,300,3  \
--input_array=normalized_input_image_tensor \
--output_array='TFLite_Detection_PostProcess'  \
--inference_type=FLOAT \
--mean_value=128 \
--std_value=128 \
--change_concat_input_ranges=false \
--allow_custom_ops


python object_detection/export_tflite_ssd_graph.py \
--pipeline_config_path=/mnt/tensorflow/models/pbfile_resnet_2018_01/faster_rcnn_resnet101_pets.config \
--trained_checkpoint_prefix=/mnt/tensorflow/models/Train_resnet_2018_01/model.ckpt-4143 \
--output_directory=/mnt/tensorflow/models/Train_resnet_2018_01/frozen_graph.pb \
--add_postprocessing_op=true

bazel run -c opt tensorflow/contrib/lite/toco:toco --  \
--input_file=/mnt/models/ssd_mobilenet_v1_fpn_test/lite/frozen_graph.pb/tflite_graph.pb \
--output_file=/mnt/models/ssd_mobilenet_v1_fpn_test/lite/optimized_graph.lite \
--output_format=TFLITE \
--input_shape=1,640,640,3  \
--input_array=normalized_input_image_tensor \
--output_array='TFLite_Detection_PostProcess'  \
--inference_type=FLOAT \
--mean_value=128 \
--std_value=128 \
--change_concat_input_ranges=false \
--allow_custom_ops




