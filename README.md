# Pytorch-VAE
This is an implementation of the VAE (Variational Autoencoder) for Cifar10

You can download dataset here -- https://www.kaggle.com/thedownhill/art-images-drawings-painting-sculpture-engraving

## Example

Photo                      |  Nearest painting//engraving
:-------------------------:|:-------------------------:
![](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/photo.jpg)  |  ![](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/ans_photo.jpg)
![](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/photo1.jpg) | ![](https://github.com/SashaMalysheva/VKHack2018/blob/master/img/ans1_photo.jpg)


## Setup

```
conda env create
python setup.py develop
```

### To train on new dataset:

To initialize training, simply go ahead

```
./main.py --train
 [--dataset {mnist,cifar10,cifar100}]
 [--kernel-num KERNEL_NUM] [--z-size Z_SIZE]
 [--epochs EPOCHS] [--batch-size BATCH_SIZE]
 [--sample-size SAMPLE_SIZE] [--lr LR]
 [--weight-decay WEIGHT_DECAY]
 [--loss-log-interval LOSS_LOG_INTERVAL]
 [--image-log-interval IMAGE_LOG_INTERVAL]
 [--resume] [--checkpoint-dir CHECKPOINT_DIR]
 [--sample-dir SAMPLE_DIR] [--no-gpus]
```

dataset == 'mnist', 'cifar10', 'cifar100'

It will convert imgs from срщщыут dataset 

### To test 

```
./main.py --еуые
 [--dataset {mnist,cifar10,cifar100}]
 [--kernel-num KERNEL_NUM] [--z-size Z_SIZE]
 [--epochs EPOCHS] [--batch-size BATCH_SIZE]
 [--sample-size SAMPLE_SIZE] [--lr LR]
 [--weight-decay WEIGHT_DECAY]
 [--loss-log-interval LOSS_LOG_INTERVAL]
 [--image-log-interval IMAGE_LOG_INTERVAL]
 [--resume] [--checkpoint-dir CHECKPOINT_DIR]
 [--sample-dir SAMPLE_DIR] [--no-gpus]
```
