## Installation
* The Docker container uses the base image nvcr.io/nvidia/l4t-pytorch:r32.7.1-pth1.10-py3. Navigate to the [Docker](Docker) folder for building the container.
* Cloning Mediapipe folder inside [Docker](Docker) folder
```bash
git clone https://github.com/google/mediapipe.git
```
* Replace the following files inside `/mediapipe` folder with the ones provided in our `/mediape_update` folder
```bash
rm mediapipe/mediapipe/calculators/tensor/image_to_tensor_converter_opencv.cc
rm mediapipe/mediapipe/calculators/tensor/image_to_tensor_converter_gl_buffer.cc
rm mediapipe/mediapipe/calculators/image/affine_transformation_runner_opencv.cc
```
* Build the container
```bash
sudo docker build -t mediapipe -f Dockerfile.HandDetector .
```
* Run the container and mount the `/data` folder in Jetson device to the `/app` folder in the container
```bash
docker run --privileged --runtime nvidia  --device /dev/video0  --network host --rm -v /data:/app/data -e DISPLAY=$DISPLAY -v /tmp:/tmp -ti mediapipe
```
* Run the setup script after spinning up the Docker Container to remove the conflicted Pillow version
```bash
bash dependencies_setup.sh
```
* Cloning [Yolov5](https://github.com/ultralytics/yolov5) 
```bash
git clone https://github.com/ultralytics/yolov5
```
* Replace the `/yolov5/utils/datasets.py` with our updated `/yolov5_update/utils/datasets.py`. Copy the `/weights`, `/data/asl7` and `MainHand.py` from our `/yolov5_update` folder to the original `/yolov5` folder. 
```
rm yolov5/utils/datasets.py
cp yolov5_update/utils/datasets.py yolov5/utils/datasets.py
cp yolov5_update/MainHand.py yolov5
cp yolov5_update/weights yolov5
cp yolov5_update/data/asl7 yolov5/data
```
* To run Pytorch in Jupyter Lab, excecute the following command
```bash
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
```
* Inference could be run directly from python scripts as per [Yolov5](https://github.com/ultralytics/yolov5) tutorials. You could also spin up Jupyter Lab and follow our [Inference notebook](Yolov5_mediapipe_inference.ipynb)   
```bash
jupyter lab --no-browser --ip=0.0.0.0 --allow-root
```

## Reference
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/google/mediapipe.git](https://github.com/google/mediapipe.git)
* [https://github.com/jiuqiant/mediapipe_python_aarch64](https://github.com/jiuqiant/mediapipe_python_aarch64)
* [https://github.com/yockgen/mediapipe_jetson_nano](https://github.com/yockgen/mediapipe_jetson_nano)
