## Building a Deep Neural Network with PyTorch in 15 Minutes - YouTube Video Notes

This video demonstrates how to quickly build a deep learning model using PyTorch. 

**Challenge:** Build a deep neural network in 15 minutes without using any documentation or pre-existing code.

**Constraints:**

* **Time Limit:** 15 minutes
* **No Documentation/Pre-existing Code:**  One-minute penalty for referencing external resources
* **No Copilot:** Copilot subscription expired

**Rewards:**

* **Failure:** $50 Amazon Gift Card to viewers
* **Success:** Bragging rights

**Introduction to PyTorch:**

* PyTorch is an open-source deep learning framework, predominantly used in Python.
* Developed by Facebook.
* Accelerates deep learning model building.
* Used in state-of-the-art models and deep learning research.

**Steps:**

1. **Import Dependencies:**
   * `from torch import nn`
   * `from torch.optim import Adam`
   * `from torch.utils.data import DataLoader`
   * `from torchvision import datasets`
   * `from torchvision.transforms import ToTensor`

2. **Import Data:**
   * Download MNIST dataset, which consists of 10 classes (0-9) of handwritten digits.
   * `train = datasets.MNIST(root="data", download=True, train=True, transform=ToTensor())`
   * Create a data loader: `dataset = DataLoader(train, batch_size=32)`

3. **Create the Neural Network Class:**
   * Define a class `ImageClassifier` that inherits from `nn.Module`.
   * Define an `__init__` method to initialize the model:
     * Create a sequential model `self.model = nn.Sequential(...)`
     * Add convolutional layers:
       * `nn.Conv2d(1, 32, kernel_size=3)` - Input channels: 1 (grayscale), Output channels: 32, Kernel size: 3x3
       * `nn.Conv2d(32, 64, kernel_size=3)` - Input channels: 32, Output channels: 64, Kernel size: 3x3
       * `nn.Conv2d(64, 128, kernel_size=3)` - Input channels: 64, Output channels: 128, Kernel size: 3x3
     * Flatten the output using `nn.Flatten()`
     * Add a linear layer: `nn.Linear(128 * 22 * 22, 10)` - Input size: 128 channels * adjusted image size (28-6), Output size: 10 (number of classes)

   * Define a `forward` method:
     * Takes input `x` and passes it through the model: `return self.model(x)`

4. **Set up Training Components:**
   * Instantiate the neural network: `clf = ImageClassifier()`
   * Move the model to the GPU: `clf.to('cuda')`
   * Create an optimizer: `opt = Adam(clf.parameters(), lr=1e-3)`
   * Create a loss function: `loss_fn = nn.CrossEntropyLoss()`

5. **Training Loop:**
   * Define a `train()` function:
     * Loop through a specified number of epochs (10 in this case).
     * Loop through each batch in the dataset.
     * Unpack the data (`x`, `y`).
     * Move data to the GPU: `x, y = x.to('cuda'), y.to('cuda')`
     * Generate predictions: `y_hat = clf(x)`
     * Calculate loss: `loss = loss_fn(y_hat, y)`
     * Zero out gradients: `opt.zero_grad()`
     * Calculate gradients: `loss.backward()`
     * Update weights: `opt.step()`
     * Print the epoch and loss for each batch.
   * Save the model state:
     * `torch.save(clf.state_dict(), 'model_state.pt')`

6. **Make Predictions:**
   * Load the saved model:
     * `clf.load_state_dict(torch.load('model_state.pt'))`
   * Load an image using Pillow: `image = Image.open('image_1.jpg')`
   * Convert the image to a tensor: `image_tensor = ToTensor()(image)`
   * Unsqueeze the tensor: `image_tensor = image_tensor.unsqueeze(0)`
   * Move the tensor to the GPU: `image_tensor = image_tensor.to('cuda')`
   * Make a prediction: `prediction = clf(image_tensor)`
   * Find the class with the highest probability: `prediction = torch.argmax(prediction)`
   * Print the predicted class.

**Key Points:**

* PyTorch uses a more dynamic approach compared to TensorFlow, where training flow is typically handled by `compile` and `fit` methods.
* The model architecture involves convolutional layers to extract features from the images, followed by a flattening layer and a linear layer for classification.
* The optimizer (Adam) and the loss function (Cross Entropy Loss) are crucial for the training process.
* The training loop iterates through epochs and batches, calculating loss, updating gradients, and saving the model state.
* To make predictions, the saved model state is loaded, the input image is processed, and the model outputs a prediction based on the trained weights.

**Outcome:**

The model successfully trained within the 15-minute time limit, achieving a good prediction accuracy. The video demonstrates the ease of building a deep learning model using PyTorch.

**Note:** This is a simplified overview of the process. The actual implementation may involve more complex steps and considerations.