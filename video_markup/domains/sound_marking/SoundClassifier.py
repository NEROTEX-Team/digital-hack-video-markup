import torch
import torchaudio

class SoundClassifier(torch.nn.Module):
    def __init__(self):
        super(SoundClassifier, self).__init__()
        self.conv1 = torch.nn.Conv1d(1, 16, kernel_size=3)
        self.pool = torch.nn.MaxPool1d(2)
        self.fc1 = torch.nn.Linear(16 * 49, 10)  # Предполагая, что входной размер 100

    def forward(self, x):
        x = self.pool(torch.nn.functional.relu(self.conv1(x)))
        x = x.view(-1, 16 * 49)
        x = torch.nn.functional.relu(self.fc1(x))
        return x

def classify_sound(audio_path, model):
    waveform, sample_rate = torchaudio.load(audio_path)
    output = model(waveform)
    _, predicted = torch.max(output, 1)
    return predicted.item()