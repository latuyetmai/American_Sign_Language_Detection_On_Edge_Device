## Installation
* The Docker container uses the base image nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3. Navigate to the [Docker](Docker) folder for building the container.
* Build the container
```bash
docker build -t yolov5 -f Dockerfile.yolov5 .
```
* Run the container and mount the `/data` folder in Jetson device to the `/app` folder in the container
```bash
docker run -ti --rm --runtime nvidia  --device /dev/video0 --network host --privileged -e DISPLAY=$DISPLAY -v /data:/app/data yolov5
```
* Cloning [Yolov5](https://github.com/ultralytics/yolov5) 
```bash
git clone https://github.com/ultralytics/yolov5
```
* To run Pytorch in Jupyter Lab, excecute the following command
```bash
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
```
* Inference could be run directly from python scripts as per [Yolov5](https://github.com/ultralytics/yolov5) tutorials. You could also spin up Jupyter Lab and follow our [Inference notebook](Yolov5_mediapipe_inference.ipynb)
* Spin up Jupyter Lab and follow our [notebook](Yolov5_inference.ipynb) for running real time inference
```bash
jupyter lab --no-browser --ip=0.0.0.0 --allow-root
```

## Reference
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
