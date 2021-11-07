import tensorflow as tf
import numpy as np
import cv2
from typing import List
from core.errors.classification_errors import ModelNotLoadedException
from core.classification.classification_config_reader import ClassificationConfigReader
from core.classification.classification_utils import softmax
from project_utils.singleton import Singleton


class ClassificationResult:

    def __init__(self, class_name, class_probability, class_index):
        self.__class_name = class_name
        self.__class_probability = class_probability
        self.__class_index = class_index

    def get_class_name(self):
        return self.__class_name

    def get_class_probability(self):
        return self.__class_probability

    def get_class_index(self):
        return self.__class_index


class ClassificationPredictions:

    def __init__(self, classification_results_list: List[ClassificationResult]):
        self.__classification_results_list: List[ClassificationResult] = classification_results_list

    def print_classification_predictions(self):
        for classification_result in self.__classification_results_list:
            print("id: {} , name: {} , probability: {}".format(classification_result.get_class_index(),
                  classification_result.get_class_name(), classification_result.get_class_probability()))


class ClassificationModel(metaclass=Singleton):

    def __init__(self):
        self.loaded: bool = False
        self.__imported = None
        self.__model = None
        self.__input_size: (int, int) = (0, 0)
        self.__output_layer_name: str = ""
        self.__classes_names: [str] = []
        self.__num_classes = 0
        self.__num_output_classes = 5

    def load_model(self, config_file: str):
        config_reader = ClassificationConfigReader(config_file)
        self.__imported = tf.saved_model.load(config_reader.get_model_path())
        self.__model = self.__imported.signatures["serving_default"]
        self.__input_size = (config_reader.get_input_width(), config_reader.get_input_height())
        self.__output_layer_name = config_reader.get_output_layer_name()
        self.__classes_names = self.__load_classes_names(config_reader.get_classes_names_file())
        self.__num_classes = len(self.__classes_names)
        self.__num_output_classes = min(self.__num_output_classes, self.__num_classes)
        self.loaded = True
        print("Model loaded successfully")

    def eval_model(self, img) -> ClassificationPredictions:
        if not self.loaded:
            raise ModelNotLoadedException()
        img = self.__preprocess_img(img)
        model_output = self.__model(input_1=img)[self.__output_layer_name][0]
        model_probabilities = softmax(model_output)
        class_index_in_order = np.argsort(-model_probabilities)
        classification_results_list = []
        for index in range(self.__num_output_classes):
            class_i = class_index_in_order[index]
            classification_results_list.append(ClassificationResult(self.__classes_names[class_i], model_probabilities[class_i], class_i))
        return ClassificationPredictions(classification_results_list)

    def __preprocess_img(self, img):
        img = cv2.resize(img, self.__input_size)
        img = np.reshape(img, (1, self.__input_size[0], self.__input_size[1], 3))
        img = (np.float32(img) / 255.0)
        return img

    @staticmethod
    def __load_classes_names(file_path):
        with open(file_path) as file:
            classes_names = file.readlines()
            classes_names = [class_name.rstrip() for class_name in classes_names]
        return classes_names
