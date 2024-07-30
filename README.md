# Skin-Texture and Acne Classification

### Overview

The "Skin-Texture and Acne Classification" project aims to develop a machine learning model capable of classifying skin texture (normal, oily, and dry) and predicting acne levels using images. The project leverages deep learning techniques and pre-trained models to achieve accurate classifications.

### Models and Performance
#### Skin Texture Classification:

###### dataset:https://www.kaggle.com/datasets/shakyadissanayake/oily-dry-and-normal-skin-types-dataset
###### Model: EfficientNet
###### Test Accuracy: 0.86
###### Details: EfficientNet was chosen for its efficiency in terms of parameter count and computation while maintaining high performance on image classification tasks. It proved effective in distinguishing between normal, oily, and dry skin textures.

#### Acne Classification:

###### dataset:https://www.kaggle.com/datasets/rutviklathiyateksun/acne-grading-classificationdataset
###### Model: InceptionV3
###### Test Accuracy: 0.98
###### Details: InceptionV3, known for its depth and inception modules, provided excellent performance in classifying acne levels. The model's ability to capture fine-grained features helped achieve high accuracy.

##### Key Features:

1.Real-time Image Classification: The web application allows users to upload images or capture them using a camera. The backend  processes these images to predict both skin texture and acne levels.
2.Dual Model Integration: The project integrates two distinct models for different tasks, showcasing the ability to handle multi-class classification problems efficiently.

##### Highlights 

High Accuracy: The project achieved a remarkable accuracy of 0.98 for acne classification using InceptionV3, demonstrating the model's robustness and effectiveness in identifying various acne levels.

Efficient Classification: EfficientNet's implementation for skin texture classification achieved a notable accuracy of 0.86, proving its capability to distinguish among different skin types with fewer resources.



