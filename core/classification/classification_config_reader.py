import json


class ClassificationConfigReader:
    """
    Python class that reads a config file for classification models. The required parameters in the config file
    are the following:

    MODEL_PATH: Path of the tensorflow model with the structure saved_model.pb, variables
    INPUT_WIDTH: Image input width
    INPUT_HEIGHT: Image input height
    OUTPUT_LAYER_NAME: name of the tensorflow output layer
    CLASSES_NAMES_FILE: name of the file containing the labels of each class. this file must have one line with the
                        name of each class
    """

    __model_path_key = "MODEL_PATH"
    __input_width_key = "INPUT_WIDTH"
    __input_height_key = "INPUT_HEIGHT"
    __output_layer_name_key = "OUTPUT_LAYER_NAME"
    __classes_names_file_key = "CLASSES_NAMES_FILE"

    def __init__(self, file_path: str):
        file = open(file_path)
        my_obj = json.load(file)
        file.close()
        self.__model_path: str = my_obj[self.__model_path_key]
        self.__input_width: int = my_obj[self.__input_width_key]
        self.__input_height: int = my_obj[self.__input_height_key]
        self.__output_layer_name: str = my_obj[self.__output_layer_name_key]
        self.__classes_names_file: str = my_obj[self.__classes_names_file_key]

    def get_model_path(self):
        return self.__model_path

    def get_input_width(self):
        return self.__input_width

    def get_input_height(self):
        return self.__input_height

    def get_output_layer_name(self):
        return self.__output_layer_name

    def get_classes_names_file(self):
        return self.__classes_names_file
