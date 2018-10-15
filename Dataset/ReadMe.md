This folder stores TFRecorder files generated using the following command:

[Execution dir：PATH_OF_'MODELS'DOWNLOADED_FROM_GITHUB/models/research]
python object_detection/dataset_tools/create_pet_tf_record.py \
--label_map_path=LABEL_MAP_FILE_ADDRESS \
--data_dir=PATH_OF_DATASET \
--output_dir=PATH_OF_EXPECTED_OUTPUT_DIR
