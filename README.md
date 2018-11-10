# VKHack2018

Find nearest face from dataset

You can download dataset here -- https://www.kaggle.com/thedownhill/art-images-drawings-painting-sculpture-engraving

## Example

![Photo](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/photo.jpg)
![Nearest painting](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/ans_photo.jpg)

![Photo](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/photo1.jpg)
![Engraving painting](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/ans_photo1.jpg)

## Setup

```
conda env create
python setup.py develop
```

### To train on new dataset:

```
convert_dataset_to_latent_vector.py -d name_of_dataset -f path_to_dataset -o answer_csv_name 
```

name_of_dataset == 'sculpture', 'painting', 'iconography', 'engraving', 'drawings'

It will convert imgs from datasets to latent space and create csv with this vectors

### To test on your own picture

```
find_nearest_img.py -d name_of_dataset -i path_to_photo -o path_to_output_photo 
```

It will save nearest photo to path_to_output_photo or show it
