## Installation
* The Docker container uses the base image nvcr.io/nvidia/l4t-ml:r32.6.1-py3. Navigate to the [Docker](Docker) folder for building the container.
* Build the container
```bash
sudo docker build -t inference:v1.0 -f Dockerfile.inference
```
* Run the container and mount the `/data` folder in Jetson device to the `/app` folder in the container
```bash
docker run -ti --rm --runtime nvidia  --device /dev/video0 --network host --privileged -e DISPLAY=$DISPLAY -v /data:/app/data inference:v1.0 bash
```
* Cloning [EfficientDet](https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git) 
```bash
git clone  https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git
```
* Spin up Jupyter Lab and follow our [notebook](Efficientdet_inference.ipynb) for running real time inference
```bash
jupyter lab --no-browser --ip=0.0.0.0 --allow-root
```

## Reference
* [https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git](https://github.com/zylo117/Yet-Another-EfficientDet-Pytorch.git)
