import json
import cv2
from webapp.core.image_processing.image_reading_utils import base64_to_numpy
from webapp.core.classification.classification_model import ClassificationModel
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class Classification(View):
    name = "classify_image"
    classification_model = ClassificationModel()
    classification_model.load_model("/home/lecun/anibal/github/deep-learning-backend/webapp/webapp/core/models/config_imagenet_efficientnet_v2_imagenet21k_s_classification_2.json")

    def post(self, request):
        input_json = json.loads(request.body)
        image_base64 = input_json["image_base64"]
        img = base64_to_numpy(image_base64)
        output = self.classification_model.eval_model(img)
        response_data = output.to_obj()
        return HttpResponse(json.dumps(response_data), content_type="application/json")
