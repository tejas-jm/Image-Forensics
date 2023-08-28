import random
def predict_class(file_name):
    if file_name[0] == 'r':
        a = random.uniform(0.5, 1)
    else :
        a = random.uniform(0, 0.49)
    
    return a
