THIS DOCUMENT LISTS THE PROCEDURES WE CREATE THE FINAL MODEL.
STRONGLY SUGGEST TO REFER THE OFFICIAL INSTRUCTION OF TENSORFLOW
WHICH IS MUCH EASY TO FOLLOW.
https://github.com/tensorflow/models/tree/master/research/object_detection

[BASIC PROCEDURES]
1. TFRecorder file generator：
Exe dir：PATH_OF_'MODELS'DOWNLOADED_FROM_GITHUB/models/research
python object_detection/dataset_tools/create_pet_tf_record.py \
--label_map_path=LABEL_MAP_FILE_ADDRESS \
--data_dir=PATH_OF_DATASET \
--output_dir=PATH_OF_EXPECTED_OUTPUT_DIR

2. Model Training
Exe dir：PATH_OF_'MODELS'DOWNLOADED_FROM_GITHUB/models/research
screen python3 object_detection/legacy/train.py --logtostderr --pipeline_config_path=PATH_OF_CONFIG_FILE --train_dir=PATH_OF_TRAIN_OUTPUT_DIR


3. Import Model
Exe dir: PATH_OF_'MODELS'DOWNLOADED_FROM_GITHUB/models/research/object_detection
cd object_detection/
python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path PATH_OF_CONFIG_FILE  --trained_checkpoint_prefix PATH_OF_TRAINED_CHECKPOINT --output_directory PATH_OF_TRAIN_OUTPUT_DIR

4. Evaluation
Exe dir: PATH_OF_'MODELS'DOWNLOADED_FROM_GITHUB/models/research/object_detection
python3 legacy/eval.py --logtostderr --train_dir=PATH_OF_TRAIN_OUTPUT_DIR --pipeline_config_path=PATH_OF_CONFIG_FILE --checkpoint_dir=PATH_OF_TRAINED_CHECKPOINT --eval_dir=PATH_OF_EVAL_DIR

5. Use tensorboard
pip3 show tensorflow
cd /root/.local/lib/python3.6/site-packages/tensorboard
screen python3 main.py --logdir=PATH_OF_TRAIN_OUTPUT_DIR

[CREATE SUMMARIZE_GRAPH]
bazel build tensorflow/tools/graph_transforms:transform_graph
bazel-bin/tensorflow/tools/graph_transforms/summarize_graph --in_graph=PATH_TO_FROZEN_GRAPH
