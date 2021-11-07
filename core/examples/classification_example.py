import cv2
from core.classification.classification_model import ClassificationModel


# config
classification_config_file_path = "/home/lecun/anibal/github/deep-learning-backend/core/models" \
                                  "/config_imagenet_efficientnet_v2_imagenet21k_s_classification_2.json"
image_path = "/home/lecun/anibal/github/deep-learning-backend/core/test_images/crab.jpg"

# Load model
my_model_1 = ClassificationModel()
my_model_1.load_model(classification_config_file_path)

# Load image
img = cv2.imread(image_path)

# Evaluate model
predictions = my_model_1.eval_model(img)
predictions.print_classification_predictions()

# Display image
cv2.imshow("img", img)
cv2.waitKey(0)
