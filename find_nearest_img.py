import face_recognition
import os
import numpy as np
import sys
import getopt
from PIL import Image
import pickle
import argparse
import logging

root_path = os.path.dirname(sys.modules['__main__'].__file__)

def choose_nearest(dataset_name, inputfile, outputfile):
    with open(dataset_name + '.p', 'rb') as fp:
        paintings = pickle.load(fp)

    filepath = os.path.join(root_path, inputfile)
    image = face_recognition.load_image_file(filepath)
    photo = face_recognition.face_encodings(image)[0]

    key = min(paintings.items(), key=lambda x: np.sum(np.sqrt((photo - np.array(x[1]))**2)))[0]

    folder = '' if key[0] == '1' else ' 2'
    name = key[1:]
    directory = os.path.join(root_path, 'dataset_updated' + folder, 'training_set', dataset_name, name + '.jpg')
    image = Image.open(directory)
    if outputfile == '':
        image.show()
    else:
        image.save(os.path.join(root_path, outputfile))


def _parse_config():


    parser = argparse.ArgumentParser(
        description='Nearest img for given image',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--d",
                        help="name_of_dataset 'sculpture', 'painting', 'iconography', 'engraving', 'drawings'")
    parser.add_argument("--i",
                        help="inputfile")
    parser.add_argument("--o",
                        help="outputfile")
    config = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s | %(message)s',
        handlers=[
            logging.StreamHandler()
        ],
        level=logging.INFO
    )

    return config

def main(config):
    inputfile = config.i
    outputfile = config.o
    dataset_name = config.d
    choose_nearest(dataset_name, inputfile, outputfile)

if __name__ == "__main__":
    main(_parse_config())