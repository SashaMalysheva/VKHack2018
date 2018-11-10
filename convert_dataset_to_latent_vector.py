import face_recognition
import os
import numpy as np
import glob
import sys
import getopt
import pickle

path = os.path.abspath(__file__)
root_path = os.path.dirname(path)



def convert_imgs_to_vectors(folder, name, inputfile, ans):
    if inputfile != '':
        directory = inputfile
    else:
        directory = os.path.join(root_path, 'dataset_updated' + folder, 'training_set', name)
    print(directory)
    for filepath in glob.iglob(directory + '/*.jpg'):
        try:
            name_of_img = filepath.split('/')[-1][:-4]
            print('Name', name_of_img)
            filepath = os.path.join(directory, filepath)
            print(filepath)
            image = face_recognition.load_image_file(filepath)

            if (face_recognition.face_encodings(image) != []):
                folder_name = '1' if folder == '' else '2'
                print('Here',  folder_name + name_of_img)
                ans[folder_name + name_of_img] = np.array(face_recognition.face_encodings(image)[0])
        except Exception:
            print('Error')
            pass
    return ans

def collect_imgs_from_folders(name, inputfile, outputfile):
    ans = convert_imgs_to_vectors('', name, inputfile, {})
    ans = convert_imgs_to_vectors(' 2', name, inputfile, ans)

    print(len(ans))
    outputfile = outputfile if outputfile!='' else name
    with open(outputfile + '.p', 'wb') as fp:
        pickle.dump(ans, fp, protocol=pickle.HIGHEST_PROTOCOL)
    return ans

def main(argv):
    inputfile = ''
    outputfile = ''
    dataset_name = ''
    try:
        opts, args = getopt.getopt(argv, "hi:d:")
    except getopt.GetoptError:
        print('parameters -d <name_of_dataset> -f <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -d <name_of_dataset> -f <inputfile> -o <outputfile>') #
            sys.exit()
        elif opt in ("-f"):
            inputfile = arg
        elif opt in ("-d"):
            dataset_name = arg
        elif opt in ("-o") and inputfile != '':
            outputfile = arg

    collect_imgs_from_folders(dataset_name, inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])