import face_recognition
import os
import numpy as np
import sys
import getopt
from PIL import Image

root_path = os.path.dirname(sys.modules['__main__'].__file__)

def choose_nearest(inputfile, outputfile):
    paintings = np.genfromtxt('painting.csv', delimiter=',')
    filepath = os.path.join(root_path, inputfile)
    image = face_recognition.load_image_file(filepath)
    photo = face_recognition.face_encodings(image)[0]

    nearest_img_index = np.argmin(np.array([np.sum(np.sqrt((photo - vector[0])**2)) for vector in paintings]))

    folder = '' if paintings[nearest_img_index, -1] == 1 else ' 2'
    name = str(int(paintings[nearest_img_index, -2])).zfill(4)
    directory = os.path.join(root_path, 'dataset_updated' + folder, 'training_set', 'painting', name + '.jpg')
    image = Image.open(directory)
    if outputfile == '':
        image.show()
    else:
        image.save(os.path.join(root_path, outputfile))


def main(argv):
    inputfile = ''
    outputfile = ''
    ans_photo =''
    try:
        opts, args = getopt.getopt(argv, "hi:o:")
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i"):
            inputfile = arg

        elif opt in ("-o") and inputfile != '':
            outputfile = arg

    choose_nearest(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])