import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import gc
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import time
# defining global variable path
image_path = "assets"

'''function to load folder into arrays and 
then it returns that same array'''
def load_images(path):
    list_of_files = []
    dirName = path
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    return list_of_files

def load_images_from_list(image_list):
    images = []
    i = 1
    for image_path in image_list:
        f = open(image_path, 'rb')
        image= (load_img(image_path))
        image.resize((256 ,192))
        image = img_to_array(image).flatten()
        images.append(image)
        gc.collect()
        if i % 20 == 0:
            print("image", i)
            time.sleep(1)
        f.close()
        i += 1
        #print(type(img))
        #print(img.mode)
    #img.show()
    return images
df = pd.read_csv("fire_aug_database.csv")
df = shuffle(df)
df = df.drop(list(df.columns)[0], axis=1)[0:180]
X = df["file"]
list_files=df["file"].tolist()
parameters = {'bootstrap': True,
              'min_samples_leaf': 4,
              'n_estimators':30,
              'min_samples_split': 10,
              'max_features': 'sqrt',
              'max_depth': 4,
              'max_leaf_nodes': None}
X_images = load_images_from_list(list_files)
y = df["label"].to_list()
train_X, test_X, train_y, test_y = train_test_split(X_images, y, test_size=0.10, random_state=42)
RF_model = RandomForestClassifier(**parameters)
RF_model.fit(train_X, train_y)

RF_predictions = RF_model.predict(test_X)
score = accuracy_score(test_y ,RF_predictions)
print(score)


confusion_matrix(test_y, RF_predictions)

RF_predictions = RF_model.predict(train_X)
score = accuracy_score(train_y ,RF_predictions)
print(score)