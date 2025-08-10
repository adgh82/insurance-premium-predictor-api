import pickle
import numpy as np


def scale_input(age, height, weight, is_diabetic=False, is_bp_issue=False,
                is_transplant=False, is_chronic=False, is_allergy=False,
                is_cancer=False, num_surgery=0):
    bmi = round(weight / ((height / 100) ** 2), 1)
    with open('std_scaler.pkl', 'rb') as scaler_file:
        standard_scaler = pickle.load(scaler_file)
    scaled_num_data = standard_scaler.transform([[age, height, weight, bmi]])

    diabetic = 0
    non_diabetic = 0
    if is_diabetic:
        diabetic = 1
    else:
        non_diabetic = 1

    scaled_num_data = append_data(scaled_num_data, diabetic)
    scaled_num_data = append_data(scaled_num_data, non_diabetic)

    bp = 0
    no_bp = 0
    if is_bp_issue:
        bp = 1
    else:
        no_bp = 1

    scaled_num_data = append_data(scaled_num_data, no_bp)
    scaled_num_data = append_data(scaled_num_data, bp)

    transplant = 0
    no_transplant = 0
    if is_transplant:
        transplant = 1
    else:
        no_transplant = 1

    scaled_num_data = append_data(scaled_num_data, no_transplant)
    scaled_num_data = append_data(scaled_num_data, transplant)

    chronic = 0
    no_chronic = 0
    if is_chronic:
        chronic = 1
    else:
        no_chronic = 1

    scaled_num_data = append_data(scaled_num_data, chronic)
    scaled_num_data = append_data(scaled_num_data, no_chronic)

    allergy = 0
    no_allergy = 0
    if is_allergy:
        allergy = 1
    else:
        no_allergy = 1

    scaled_num_data = append_data(scaled_num_data, no_allergy)
    scaled_num_data = append_data(scaled_num_data, allergy)

    cancer = 0
    no_cancer = 0
    if is_cancer:
        cancer = 1
    else:
        no_cancer = 1

    scaled_num_data = append_data(scaled_num_data, no_cancer)
    scaled_num_data = append_data(scaled_num_data, cancer)

    surgery_0 = 0
    surgery_1 = 0
    surgery_2 = 0
    surgery_3 = 0
    if num_surgery == 0:
        surgery_0 = 1
    elif num_surgery == 1:
        surgery_1 = 1
    elif num_surgery == 2:
        surgery_2 = 1
    else:
        surgery_3 = 1

    scaled_num_data = append_data(scaled_num_data, surgery_0)
    scaled_num_data = append_data(scaled_num_data, surgery_1)
    scaled_num_data = append_data(scaled_num_data, surgery_2)
    scaled_num_data = append_data(scaled_num_data, surgery_3)

    return scaled_num_data


def append_data(src, new_data):
    modified_src = np.append(src, [[new_data]], axis=1)
    return modified_src


def get_prediction(data_point):
    with open('linear_reg_model.pkl', 'rb') as model_file:
        elastic_net_model = pickle.load(model_file)

    return elastic_net_model.predict(data_point)
