#environment variables set
export YOUR_GCS_BUCKET=ssdmobile


#train
gcloud ml-engine jobs submit training `whoami`_object_detection_`date +%s` \
--job-dir=gs://${YOUR_GCS_BUCKET}/train \
--packages dist/object_detection-0.1.tar.gz,slim/dist/slim-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz \
--module-name object_detection.model_tpu_main \
--runtime-version 1.8 \
--scale-tier BASIC_TPU \
--region us-central1 \
-- \
--model_dir=gs://${YOUR_GCS_BUCKET}/train \
--tpu_zone us-central1 \
--pipeline_config_path=gs://${YOUR_GCS_BUCKET}/data/pipeline.config

#evaluation
gcloud ml-engine jobs submit training `whoami`_object_detection_eval_validation_`date +%s` 
--job-dir=gs://${YOUR_GCS_BUCKET}/train/ \
--packages dist/object_detection-0.1.tar.gz,slim/dist/slim-0.1.tar.gz,/tmp/pycocotools/pycocotools-2.0.tar.gz \
--module-name object_detection.legacy.eval \
--runtime-version 1.9 \
--scale-tier BASIC_GPU \
--region us-central1 \
-- \
--eval_dir=gs://${YOUR_GCS_BUCKET}/eval/ \
--pipeline_config_path=gs://${YOUR_GCS_BUCKET}/data/pipeline.config \
--checkpoint_dir=gs://${YOUR_GCS_BUCKET}/train/

