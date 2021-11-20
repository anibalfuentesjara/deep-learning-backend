from django.apps import AppConfig
from webapp.core.classification.classification_model import ClassificationModel


class ClassificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classification'
    def ready(self):
        print("my app ClassificationConfig is ready")
        print("HELLOOOO!!!")
        classification_model = ClassificationModel()
        classification_model.load_model("/home/lecun/anibal/github/deep-learning-backend/webapp/webapp/core/models/config_imagenet_efficientnet_v2_imagenet21k_s_classification_2.json")
