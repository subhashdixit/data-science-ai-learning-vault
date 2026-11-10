# 🖼️ Convolutional Neural Networks (CNNs)

> [!blue] 💙 **CNNs for Computer Vision**
> Convolutional Neural Networks designed for processing grid-structured data like images. Learn about convolutional layers, pooling, and modern CNN architectures.

---

## 📚 Topics Covered

### Core Concepts
- **Convolutional Layers** - Filters, kernels, feature maps
- **Pooling Layers** - Max pooling, average pooling
- **Padding & Stride** - Controlling output dimensions
- **CNN Architectures** - LeNet, AlexNet, VGG, ResNet, Inception
- **Transfer Learning** - Using pre-trained models
- **Data Augmentation** - Improving generalization
- **Object Detection** - YOLO, R-CNN, Faster R-CNN
- **Image Segmentation** - U-Net, Mask R-CNN

---

## 🎯 Learning Objectives

By the end of this section, you should be able to:
- [ ] Understand how convolutional layers extract features
- [ ] Build CNN architectures for image classification
- [ ] Apply transfer learning with pre-trained models
- [ ] Implement data augmentation strategies
- [ ] Use CNNs for object detection and segmentation
- [ ] Fine-tune models on custom datasets
- [ ] Visualize what CNNs learn (activation maps, filters)

---

## 📝 Key Notes

### [[convolutional-layers|Convolutional Layers]]
- How convolution operation works
- Filter size, stride, padding
- Feature map computation

### [[pooling-layers|Pooling]]
- Max pooling vs average pooling
- Spatial dimension reduction
- Translation invariance

### [[cnn-architectures|CNN Architectures]]
- **LeNet-5** (1998) - First successful CNN
- **AlexNet** (2012) - ImageNet breakthrough
- **VGG** (2014) - Deep uniform architecture
- **ResNet** (2015) - Residual connections
- **Inception** (2014) - Multi-scale features
- **EfficientNet** (2019) - Compound scaling

### [[transfer-learning|Transfer Learning]]
- Feature extraction approach
- Fine-tuning strategies
- Domain adaptation

---

## 💻 Code Examples

> [!green] ✅ **Simple CNN in PyTorch**
> ```python
> import torch.nn as nn
> 
> class SimpleCNN(nn.Module):
>     def __init__(self, num_classes=10):
>         super(SimpleCNN, self).__init__()
>         
>         # Convolutional layers
>         self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
>         self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
>         self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
>         
>         # Pooling
>         self.pool = nn.MaxPool2d(2, 2)
>         
>         # Fully connected layers
>         self.fc1 = nn.Linear(128 * 4 * 4, 512)
>         self.fc2 = nn.Linear(512, num_classes)
>         
>         # Activations and regularization
>         self.relu = nn.ReLU()
>         self.dropout = nn.Dropout(0.5)
>         
>     def forward(self, x):
>         # Conv block 1
>         x = self.relu(self.conv1(x))
>         x = self.pool(x)  # 32x32 -> 16x16
>         
>         # Conv block 2
>         x = self.relu(self.conv2(x))
>         x = self.pool(x)  # 16x16 -> 8x8
>         
>         # Conv block 3
>         x = self.relu(self.conv3(x))
>         x = self.pool(x)  # 8x8 -> 4x4
>         
>         # Flatten
>         x = x.view(x.size(0), -1)
>         
>         # Fully connected layers
>         x = self.relu(self.fc1(x))
>         x = self.dropout(x)
>         x = self.fc2(x)
>         
>         return x
> ```

> [!green] ✅ **Transfer Learning with Pre-trained ResNet**
> ```python
> import torch
> import torchvision.models as models
> import torch.nn as nn
> 
> # Load pre-trained ResNet
> model = models.resnet50(pretrained=True)
> 
> # Freeze all layers
> for param in model.parameters():
>     param.requires_grad = False
> 
> # Replace final layer for custom task
> num_features = model.fc.in_features
> model.fc = nn.Linear(num_features, num_classes)
> 
> # Only train the final layer
> optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)
> ```

> [!green] ✅ **Data Augmentation**
> ```python
> from torchvision import transforms
> 
> train_transform = transforms.Compose([
>     transforms.RandomResizedCrop(224),
>     transforms.RandomHorizontalFlip(),
>     transforms.RandomRotation(10),
>     transforms.ColorJitter(brightness=0.2, contrast=0.2),
>     transforms.ToTensor(),
>     transforms.Normalize(mean=[0.485, 0.456, 0.406],
>                        std=[0.229, 0.224, 0.225])
> ])
> ```

---

## ⚠️ Common Pitfalls

> [!red] ⚠️ **Overfitting on Small Datasets**
> - **Problem:** CNN memorizes training images instead of learning features
> - **Solution:** Use data augmentation, dropout, transfer learning, regularization

> [!red] ⚠️ **Wrong Input Dimensions**
> - **Problem:** Image size mismatch causes errors in fully connected layers
> - **Solution:** Use adaptive pooling or calculate dimensions carefully

> [!red] ⚠️ **Forgetting to Normalize Images**
> - **Problem:** Poor convergence and performance
> - **Solution:** Normalize with ImageNet mean/std or dataset statistics

> [!red] ⚠️ **Training Everything from Scratch**
> - **Problem:** Requires huge datasets and computational resources
> - **Solution:** Start with transfer learning, then consider training from scratch

---

## 💡 Best Practices

> [!yellow] 💡 **Architecture Design**
> - Start with **3x3 convolutions** (proven effective)
> - Use **batch normalization** after each conv layer
> - Apply **ReLU activation** after batch norm
> - Stack multiple conv layers before pooling
> - Use **global average pooling** instead of FC layers when possible

> [!yellow] 💡 **Transfer Learning Strategy**
> 1. **Small dataset, similar domain:** Freeze all layers, train only classifier
> 2. **Small dataset, different domain:** Freeze early layers, fine-tune later layers
> 3. **Large dataset, similar domain:** Fine-tune all layers with small learning rate
> 4. **Large dataset, different domain:** Train from scratch or fine-tune extensively

> [!yellow] 💡 **Data Augmentation**
> - **Always use:** Random horizontal flip, random crop, normalization
> - **Sometimes use:** Rotation, color jitter, random erasing
> - **Avoid:** Vertical flip (unless data supports it), excessive distortion

> [!yellow] 💡 **Performance Optimization**
> - Use **mixed precision training** (FP16) for faster training
> - Enable **cudnn.benchmark** for faster convolutions
> - Use **larger batch sizes** when possible (GPU memory permitting)
> - Apply **gradient accumulation** for effective larger batches

---

## 🔬 Advanced Topics

> [!purple] 🔮 **Modern Architectures**
> - **ResNet:** Skip connections enable very deep networks (152+ layers)
> - **DenseNet:** Dense connections for feature reuse
> - **EfficientNet:** Compound scaling (width, depth, resolution)
> - **Vision Transformer (ViT):** Transformers for image classification
> - **ConvNeXt:** Modernized CNN design matching transformer performance

> [!purple] 🔮 **Object Detection**
> - **YOLO (You Only Look Once):** Real-time single-stage detector
> - **Faster R-CNN:** Two-stage detector with region proposals
> - **RetinaNet:** Focal loss for class imbalance
> - **EfficientDet:** Efficient multi-scale object detection

> [!purple] 🔮 **Segmentation**
> - **U-Net:** Encoder-decoder with skip connections for medical imaging
> - **Mask R-CNN:** Instance segmentation (object detection + masks)
> - **DeepLab:** Atrous convolution for semantic segmentation
> - **Segment Anything (SAM):** Foundation model for segmentation

> [!purple] 🔮 **Visualization Techniques**
> - **Activation Maps:** Visualize feature maps at different layers
> - **Grad-CAM:** Class activation mapping for interpretability
> - **Filter Visualization:** Show what filters learn
> - **t-SNE:** Visualize learned embeddings

---

## 🔗 Related Topics

- [[04-Deep-Learning/Neural-Networks/README|Neural Networks]] - Foundational concepts
- [[04-Deep-Learning/Transformers/README|Transformers]] - Vision Transformers
- [[02-Statistics-and-Data/Data-Visualization/README|Data Visualization]] - Visualizing results
- [[03-Machine-Learning/Supervised-Learning/README|Supervised Learning]] - Classification fundamentals

---

## 📚 Resources

**Courses:**
- Stanford CS231n: CNNs for Visual Recognition
- Fast.ai Practical Deep Learning
- PyTorch Image Models (timm) Documentation

**Papers:**
- "ImageNet Classification with Deep CNNs" (AlexNet, 2012)
- "Very Deep CNNs for Large-Scale Image Recognition" (VGG, 2014)
- "Deep Residual Learning for Image Recognition" (ResNet, 2015)
- "EfficientNet: Rethinking Model Scaling for CNNs" (2019)
- "An Image is Worth 16x16 Words: Transformers for Image Recognition" (ViT, 2020)

**Libraries:**
- **torchvision** - PyTorch vision models and datasets
- **timm** - PyTorch Image Models (state-of-the-art models)
- **albumentations** - Advanced data augmentation
- **detectron2** - Facebook's object detection library

---

**Tags:** #cnn #computer-vision #image-classification #transfer-learning #object-detection
**Difficulty:** 🔥🔥🔥 Advanced
**Last Updated:** 2026-11-11
