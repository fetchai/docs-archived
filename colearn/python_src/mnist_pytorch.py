# ------------------------------------------------------------------------------
#
#   Copyright 2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
from torchsummary import summary
from torchvision import transforms, datasets
import torch.utils.data

import torch.nn as nn
import torch.nn.functional as nn_func

# define some constants
batch_size = 64
seed = 42
n_rounds = 20
train_fraction = 0.9
learning_rate = 0.001
height = 28
width = 28
n_classes = 10
num_test_batches = 10

no_cuda = False
cuda = not no_cuda and torch.cuda.is_available()
device = torch.device("cuda" if cuda else "cpu")
kwargs = {'num_workers': 1, 'pin_memory': True} if cuda else {}

# Load the data
data = datasets.MNIST('/tmp/mnist', transform=transforms.ToTensor(), download=True)
n_train = int(train_fraction * len(data))
n_test = len(data) - n_train
train_data, test_data = torch.utils.data.random_split(data, [n_train, n_test])

train_dataloader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True, **kwargs)
test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=True, **kwargs)


# Define the model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5, 1)
        self.conv2 = nn.Conv2d(20, 50, 5, 1)
        self.fc1 = nn.Linear(4 * 4 * 50, 500)
        self.fc2 = nn.Linear(500, n_classes)

    def forward(self, x):
        x = nn_func.relu(self.conv1(x.view(-1, 1, height, width)))
        x = nn_func.max_pool2d(x, 2, 2)
        x = nn_func.relu(self.conv2(x))
        x = nn_func.max_pool2d(x, 2, 2)
        x = x.view(-1, 4 * 4 * 50)
        x = nn_func.relu(self.fc1(x))
        x = self.fc2(x)
        return nn_func.log_softmax(x, dim=1)


model = Net()
opt = torch.optim.Adam(model.parameters(), lr=learning_rate)
criterion = torch.nn.NLLLoss()

# Train and evaluate the model
for round in range(n_rounds):
    # train model
    model.train()

    for batch_idx, (data, labels) in enumerate(train_dataloader):
        opt.zero_grad()

        # Data needs to be on same device as model
        data = data.to(device)
        labels = labels.to(device)

        output = model(data)

        loss = criterion(output, labels)
        loss.backward()
        opt.step()

    # evaluate model
    model.eval()
    total_score = 0
    all_labels = []
    all_outputs = []
    with torch.no_grad():
        for batch_idx, (data, labels) in enumerate(test_dataloader):
            if batch_idx == num_test_batches:
                break
            data = data.to(device)
            labels = labels.to(device)
            output = model(data)
            total_score += criterion(output, labels)
    avg_loss = float(total_score / (num_test_batches * batch_size))
    print(f"Average loss at round {round} is {avg_loss}")
