## Real time inference with live camera on Nvidia Jetson Xavier NX Device

The following models were implemented on the Jetson device:
1. [__Yolov5 with Pose Estimation__](yolov5_pose_estimation): Our best model uses [Google MediaPipe's](https://github.com/google/mediapipe.git) pose estimation for hand detecting as an image preprocessing step. The images are then sent to [Yolov5](https://github.com/ultralytics/yolov5) model for inference.
2. [__Yolov5__](yolov5): based on the original [Yolov5](https://github.com/ultralytics/yolov5) architecture.
3. [__EfficientDet__](efficientdet): customized real time inference with camera developed from the [Yet Another EfficientDet](https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git) architecture.

## Installation
Each model contains Dockerfiles and dependencies for installing the required packages on the Nvidia Jetson Xavier NX. 

The Docker container for [Yolov5 with Pose Estimation](yolov5_pose_estimation) could also be used for inference with [Yolov5](yolov5) and [EfficientDet](efficientdet) models. However, this container size is 8.92 GB and requires special set ups (detailed instructions provided [here](yolov5_pose_estimation)). Therefore, we recommend choosing the lighter weight containers if you're only interested in running [Yolov5](yolov5) or [EfficientDet](efficientdet) models.


## Demos 

Realtime inference with [Yolov5 with Pose Estimation](yolov5_pose_estimation):

https://user-images.githubusercontent.com/74551083/163217588-6e7ac718-c07f-46db-bdaa-e692a202a3a4.mp4
