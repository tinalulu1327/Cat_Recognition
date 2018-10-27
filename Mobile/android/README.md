# Cat detection Android application with TensorFlow
This folder contains an Android application to do the cat detection process on real-time image.

## Description

A device running Android 5.0 (API 21) or higher is required to run the application due
to the use of the camera2 API, although the native libraries themselves can run
on API >= 14 devices.

## Interfaces:

1. [Classification]
	Using the tensorflow_inception_graph model
        To classify camera frames in real-time, displaying the top results
        in an overlay on the camera image.
2. [Detection]
        Using the multibox model trained using the
        [Tensorflow Object Detection API]
        To detect cat (from 14 categories) in the camera preview in real-time.
3. [Read me]
        To provide all 14 type of cats' background information and the system accuracy on them 

## Running the application

1. There is an Android apk file included in this zip file(in the release floder), the user just needs to transfer the apk file 
to an Android deveice then install it directly.
2. Once the app is installed it can be started via the "Classification", "Detection", and
"Read me", a which have the white HelloKitty as their icon.


## Building in Android Studio using the TensorFlow AAR from JCenter

The simplest way to compile the source code of the application yourself, and try out changes to the
project code is to use AndroidStudio. Simply set this `android` directory as the
project root.

Then edit the `build.gradle` file and change the value of `nativeBuildSystem` to
`'none'` so that the project is built in the simplest way possible:

```None
def nativeBuildSystem = 'none'
```

