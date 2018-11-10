import face_recognition
import os
import numpy as np
import glob
import sys
from PIL import Image
root_path = os.path.dirname(sys.modules['__main__'].__file__)

def convert_imgs_to_vectors(folder, name, ans):
    directory = os.path.join(root_path, 'dataset_updated' + folder, 'training_set', name)
    for filepath in glob.iglob(directory + '/*.jpg'):
        try:
            num = int(filepath[-8:-4])
            filepath = os.path.join(directory, filepath)
            print(filepath)
            print(filepath)
            image = face_recognition.load_image_file(filepath)
            if (face_recognition.face_encodings(image) != []):
                ans.append(np.concatenate((np.array(face_recognition.face_encodings(image)[0]),
                                           np.array([num]), np.array([1 if folder=='' else 2]))))
        except Exception:
            print('Error')
    return ans

def collect_imgs_from_folders(name):
    ans = convert_imgs_to_vectors('', name, [])
    print(ans[0])
    #ans = convert_imgs_to_vectors(' 2', name, ans)
    ans = np.asmatrix(ans)
    print(ans.shape)
    print(ans[0])
    np.savetxt(name + "1.csv", ans, delimiter=",")
    return ans

painting_ans = collect_imgs_from_folders('painting')


print(painting_ans.shape)
#results = face_recognition.compare_faces([biden_encoding], unknown_encoding)