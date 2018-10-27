[STRUCTURE]
There are four parts in the project:
1) DataSet related files
    - 'ImageCollection' and 'Preprocess Dataset' folder are stores scripts used
    in the project.

    [Notes] These scripts are separated and each of them is used to solve one
    one single task.

    - 'Dataset' folder stores the final dataset used in the project.

    [Notes] Since the whole dataset is larger than storage limitation of Github,
    the original dataset is not stored.

2) Classification related files
    - In this part, AlexNet related files are stored.
    However, we won't use it in the project.

3) Object detection related files
    - 'Final Model files' folder stores the final model files which could be used
    in the notebook and an Android app.

4) Web related files
    - 'Web' folder stores all the files used to show the static website, which
    is a basic description of the project.

5) Mobile app related files
    - 'Mobile' folder stores all the files used to implement an Android app, and the outcome
    apk file is downloaded by:
    https://www.dropbox.com/sh/6izojq9hlovbky2/AADh4vxs2wzi3fomAN9tEr6oa?dl=0

[GUIDE]
1) Install Tensorflow
2) Download Tensorflow Models:
   https://github.com/tensorflow/models.git
3) Basic procedures:
   - Making DataSet
   - Training model using scripts in the 'Tensorflow Models'
   - Optimize model
   - Export model using scripts in the 'Tensorflow Models'
   - Use 'object_detection.ipynb' to test the result of the model

[HOW TO TEST THE MODEL]
1) Install 'Jupyter'
2) Make sure 'object_detection.ipynb' can access scripts in the 'Tensorflow Models'.
3) Execute the 'object_detection.ipynb'
