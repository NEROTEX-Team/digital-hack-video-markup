import torchvision.transforms as transforms
from torchvision import models

def classify_scene(frames):
    model = models.resnet18(pretrained=True)
    model.eval()
    preprocess = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    results = []
    for frame in frames:
        input_tensor = preprocess(frame)
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = model(input_batch)
        results.append(output)
    return results