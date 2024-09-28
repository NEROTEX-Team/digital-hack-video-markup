import torch

def detect_objects(frames):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = []
    for frame in frames:
        results.append(model(frame))
    return results