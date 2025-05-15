import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Sample dataset: [browser_switches, idle_time, past_strikes] => [cheat (1) or not (0)]
data = np.array([
    [5, 2.0, 0, 0],
    [20, 0.1, 1, 1],
    [15, 0.5, 0, 1],
    [3, 5.0, 0, 0],
    [18, 0.3, 1, 1],
    [2, 4.0, 0, 0],
    [25, 0.2, 1, 1],
    [1, 3.5, 0, 0]
], dtype=np.float32)

X = torch.tensor(data[:, :3])
y = torch.tensor(data[:, 3:], dtype=torch.float32)

class CheatNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 5)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

model = CheatNet()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(200):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

print("Final Loss:", loss.item())

with torch.no_grad():
    test_student = torch.tensor([[10, 1.0, 1]])
    pred = model(test_student).item()
    print("Cheat probability for student [10 switches, 1.0 idle, 1 strike]:", round(pred, 2))