from app import model_pred

new_data = {'Age': 68,
            'RestingBP': 150,
            'Cholesterol': 195,
            'Oldpeak': 0.0,
            'FastingBS': 1,
            'MaxHR': 132,
            }


def test_predict():
    prediction = model_pred(new_data)
    assert prediction == 1
