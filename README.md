# American Sign Language Recognition on the Edge

## Welcome to the American Sign Language (ASL) Recognition on the Edge Repo!

### Created by Mai La, Elizabeth Khan, Carlos Moreno, Lily Sun

---

For the purposes of this project, we are going to focus on using ASL object detection models (EfficientDet, YOLOV5, YOLOX, Single-Shot Detector (SSD), and Detectron2(Faster R-CNN)) on the edge device (Nvidia Jetson Xavier NX) and attempt to improve upon some of the limitations of the existing ASL recognition methods

1. [__Image Capturing__](image_capturing) folder contains the Dockerfile, Jupyter Notebook, and executable python script to capture training images from live camera stream running on Nvidia Jetson Device. 

2. [__Image Preprocessing__](image_preprocessing) folder contains the excecutable python file that adds the image posture information on top of the image.

3. [__Models__](models) folder contains the various model architectures that we trained including Faster R-CNN, EfficientDet, YOLOV5, and YOLOX. Within each model sub-folder are the model artifacts which include the Pytorch model with saved weights for our various runs on the AWS ec2 instance. YOLOV5 contains the Jupyter notebook used for installation and training in the Cloud.

4. [__Jetson Inference__](jetson_inference) folder contains Dockerfiles for each efficientdet and yolov5 models for inference. For YOLOV5 models, we have the TensorRT, ONNX, Pytorch, and Torch Script models in the weights folder. The final YOLOV5 model that we used on the edge with Pose Estimation is in the [yolov5_pose_estimation](jetson_inference/yolov5_pose_estimation) sub-folder. 


### Demos 

Realtime inference with [Yolov5 and Pose Estimation](jetson_inference/yolov5_pose_estimation):

https://user-images.githubusercontent.com/74551083/163217588-6e7ac718-c07f-46db-bdaa-e692a202a3a4.mp4

