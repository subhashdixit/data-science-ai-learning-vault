# 🧠 Neural Networks

**💙 Neural Networks Fundamentals**
Foundation of deep learning - feed-forward neural networks, backpropagation, activation functions, and optimization techniques.

---

## 📚 Topics Covered

### Core Concepts
- **Perceptrons & Multi-Layer Perceptrons (MLP)**
- **Backpropagation Algorithm**
- **Activation Functions** (ReLU, Sigmoid, Tanh, Softmax)
- **Loss Functions** (MSE, Cross-Entropy)
- **Optimization Algorithms** (SGD, Adam, RMSprop)
- **Regularization** (L1/L2, Dropout, Early Stopping)
- **Batch Normalization**
- **Weight Initialization** (Xavier, He)

---

## 🎯 Learning Objectives

By the end of this section, you should be able to:
- [ ] Understand how neural networks learn through backpropagation
- [ ] Choose appropriate activation functions for different tasks
- [ ] Implement gradient descent optimization
- [ ] Apply regularization techniques to prevent overfitting
- [ ] Initialize weights properly
- [ ] Build and train a neural network from scratch
- [ ] Use PyTorch/TensorFlow for neural network implementation

---

## 📝 Key Notes

### [[neural-network-basics|Neural Network Basics]]
- Architecture and components
- Forward propagation
- Universal approximation theorem

### [[backpropagation|Backpropagation]]
- Chain rule application
- Gradient computation
- Computational graphs

### [[activation-functions|Activation Functions]]
- ReLU vs Sigmoid vs Tanh
- Dying ReLU problem
- Advanced activations (Leaky ReLU, GELU, Swish)

### [[optimization-algorithms|Optimization]]
- SGD with momentum
- Adam optimizer
- Learning rate scheduling

### [[regularization-techniques|Regularization]]
- Dropout implementation
- Batch normalization
- Early stopping strategies

---

## 💻 Code Examples

**✅ Simple Neural Network in PyTorch**
```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Initialize model
model = SimpleNN(input_size=784, hidden_size=128, output_size=10)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

---

## ⚠️ Common Pitfalls

**⚠️ Vanishing/Exploding Gradients**
- **Problem:** Gradients become too small or too large during backpropagation
- **Solution:** Use ReLU activation, batch normalization, gradient clipping, proper weight initialization

**⚠️ Overfitting**
- **Problem:** Model memorizes training data instead of learning patterns
- **Solution:** Use dropout, L2 regularization, data augmentation, early stopping

**⚠️ Dead ReLU Neurons**
- **Problem:** ReLU neurons output zero for all inputs
- **Solution:** Use Leaky ReLU, adjust learning rate, check weight initialization

---

## 💡 Best Practices

**💡 Activation Function Selection**
- Use **ReLU** for hidden layers (default choice)
- Use **Softmax** for multi-class classification output
- Use **Sigmoid** for binary classification output
- Try **Leaky ReLU** or **ELU** if experiencing dying ReLU

**💡 Optimization Tips**
- Start with **Adam optimizer** (adaptive learning rate)
- Use **learning rate scheduling** to improve convergence
- Monitor **training and validation loss** to detect overfitting
- Implement **gradient clipping** for stability

**💡 Weight Initialization**
- Use **Xavier/Glorot** initialization for sigmoid/tanh
- Use **He initialization** for ReLU activation
- Never initialize all weights to zero (symmetry breaking)

---

## 🔬 Advanced Topics

**🔮 Advanced Architectures**
- **Residual Connections** (ResNet) - Skip connections to enable deeper networks
- **Highway Networks** - Gated connections for gradient flow
- **DenseNet** - Dense connections between layers

**🔮 Advanced Optimization**
- **AdamW** - Adam with decoupled weight decay
- **Lookahead Optimizer** - Maintains slow and fast weights
- **LAMB** - Layer-wise Adaptive Moments (for large batch training)

**🔮 Normalization Techniques**
- **Layer Normalization** - Alternative to batch norm
- **Group Normalization** - For small batch sizes
- **Instance Normalization** - For style transfer

---

## 🔗 Related Topics

- [[04-Deep-Learning/CNNs/README|CNNs]] - Convolutional layers for images
- [[04-Deep-Learning/RNNs-LSTMs/README|RNNs]] - Recurrent networks for sequences
- [[03-Machine-Learning/Supervised-Learning/README|Supervised Learning]] - ML foundations
- [[01-Foundations/Math/Linear-Algebra/README|Linear Algebra]] - Mathematical foundation
- [[01-Foundations/Math/Calculus/README|Calculus]] - Derivatives and gradients

---

## 📚 Resources

**Books:**
- Deep Learning (Goodfellow, Bengio, Courville) - Chapter 6
- Neural Networks and Deep Learning (Michael Nielsen)

**Courses:**
- Fast.ai Practical Deep Learning
- Andrew Ng's Deep Learning Specialization
- MIT 6.S191: Introduction to Deep Learning

**Papers:**
- "Understanding the difficulty of training deep feedforward neural networks" (Glorot & Bengio, 2010)
- "Batch Normalization: Accelerating Deep Network Training" (Ioffe & Szegedy, 2015)
- "Adam: A Method for Stochastic Optimization" (Kingma & Ba, 2014)

**Tools:**
- PyTorch Documentation
- TensorFlow/Keras Tutorials
- Neural Network Playground (visualization)

---

**Tags:** #neural-networks #deep-learning #backpropagation #optimization #activation-functions
**Difficulty:** 🔥🔥🔥 Advanced
**Last Updated:** 2026-11-11
