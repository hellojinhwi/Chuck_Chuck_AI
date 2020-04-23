"""
Mask R-CNN
Train on the toy Balloon dataset and implement color splash effect.

Copyright (c) 2018 Matterport, Inc.
Licensed under the MIT License (see LICENSE for details)
Written by Waleed Abdulla

------------------------------------------------------------

Usage: import the module (see Jupyter notebooks for examples), or run from
       the command line as such:

    # Train a new model starting from pre-trained COCO weights
    python3 balloon.py train --dataset=/path/to/balloon/dataset --weights=coco

    # Resume training a model that you had trained earlier
    python3 balloon.py train --dataset=/path/to/balloon/dataset --weights=last

    # Train a new model starting from ImageNet weights
    python3 balloon.py train --dataset=/path/to/balloon/dataset --weights=imagenet

    # Apply color splash to an image
    python3 balloon.py splash --weights=/path/to/weights/file.h5 --image=<URL or path to file>

    # Apply color splash to video using the last weights you trained
    python3 balloon.py splash --weights=last --video=<URL or path to file>
"""

import os
import sys
import json
import datetime
import numpy as np
import skimage.draw

# from keras import backend as K
# import keras
# import tensorflow as tf
# from keras.backend.tensorflow_backend import set_session
# config = tf.ConfigProto()
# config.gpu_options.allow_growth = True #allows dynamic growth
# config.gpu_options.visible_device_list = "2" #set GPU number
# set_session(tf.Session(config=config))

# Root directory of the project
ROOT_DIR = os.getcwd()
if ROOT_DIR.endswith(os.path.join(ROOT_DIR, "mrcnn")):
    # Go up two levels to the repo root
    ROOT_DIR = os.path.dirname(os.path.dirname(ROOT_DIR))

# Import Mask RCNN
sys.path.append(ROOT_DIR)
from mrcnn.config import Config
from mrcnn import model as modellib, utils

# Path to trained weights file
COCO_WEIGHTS_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Directory to save logs and model checkpoints, if not provided
# through the command line argument --logs
DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

DATASET_DIR = os.path.join(ROOT_DIR, "pills_dataset")
############################################################
#  Configurations
############################################################


class PillsConfig(Config):
    """Configuration for training on the toy  dataset.
    Derives from the base Config class and overrides some values.
    """
    # Give the configuration a recognizable name
    NAME = "pills"

    # We use a GPU with 12GB memory, which can fit two images.
    # Adjust down if you use a smaller GPU.
    IMAGES_PER_GPU = 2

    # Number of classes (including background)
    NUM_CLASSES = 1 + 63  # Background + pills

    # Number of training steps per epoch
    STEPS_PER_EPOCH = 100

    # Skip detections with < 90% confidence
    DETECTION_MIN_CONFIDENCE = 0.9


############################################################
#  Dataset
############################################################

class PillsDataset(utils.Dataset):

    def load_pills(self, dataset_dir, subset):
        """Load a subset of the pills dataset.
        dataset_dir: Root directory of the dataset.
        subset: Subset to load: train or val
        """
        # Esome, K-Contin, levo, Piropen, Roidipen
        # Add classes. We have only one class to add.

        #csv, tsv 파일로 classname 작성 후 불러와도 됨. (test용으로 제작되었음.)
        self.add_class("pills", 1, "에스원엠프정40mg")
        self.add_class("pills", 2, "케이콘틴서방정")
        self.add_class("pills", 3, "레보살탄정5/160밀리그램")
        self.add_class("pills", 4, "피로펜정")
        self.add_class("pills", 5, "로이디펜캡슐")
        self.add_class("pills", 6, "카발린캡슐50mg")
        self.add_class("pills", 7, "가르젠정")
        self.add_class("pills", 8, "노퍼스캡슐")
        self.add_class("pills", 9, "뉴로펜익스프레스엘정")
        self.add_class("pills", 10, "닥터베아제정")
        self.add_class("pills", 11, "덱스피드연질캡슐")
        self.add_class("pills", 12, "록스펜정")
        self.add_class("pills", 13, "리렉사정")
        self.add_class("pills", 14, "뮤레스캡슐")
        self.add_class("pills", 15, "미노씬캡슐50mg")
        self.add_class("pills", 16, "서울파모티딘정20mg")
        self.add_class("pills", 17, "세라진정")
        self.add_class("pills", 18, "속시판정")
        self.add_class("pills", 19, "스토마신캡슐")
        self.add_class("pills", 20, "씬지록신정100mg")
        self.add_class("pills", 21, "아웃콜로프캡슐")
        self.add_class("pills", 22, "알닥톤필름코팅정25밀리그람")
        self.add_class("pills", 23, "알러딘정")
        self.add_class("pills", 24, "알피록소펜정")
        self.add_class("pills", 25, "애드빌리퀴겔연질캡슐")
        self.add_class("pills", 26, "에이프록센연질캡슐")
        self.add_class("pills", 27, "엔테론정50밀리그램")
        self.add_class("pills", 28, "엠피스정")
        self.add_class("pills", 29, "올나펜연질캡슐")
        self.add_class("pills", 30, "월드로신캡슐")
        self.add_class("pills", 31, "이부로엔연질캡슐")
        self.add_class("pills", 32, "이지엔6스트롱연질캡슐")
        self.add_class("pills", 33, "이지엔6애니연질캡슐")
        self.add_class("pills", 34, "캐롤디연질캡슐")
        self.add_class("pills", 35, "아스피린프로텍트정100밀리그람")
        self.add_class("pills", 36, "케이캡정50mg")
        self.add_class("pills", 37, "코데날정")
        self.add_class("pills", 38, "크록신정250밀리그램")
        self.add_class("pills", 39, "클라펜정")
        self.add_class("pills", 40, "타미진정")
        self.add_class("pills", 41, "페인엔젤이부연질캡슐")
        self.add_class("pills", 42, "퓨록심정250mg")
        self.add_class("pills", 43, "후리졸정")
        self.add_class("pills", 44, "다우제큐정")
        self.add_class("pills", 45, "레바스타정")
        self.add_class("pills", 46, "렉스펜정")
        self.add_class("pills", 47, "록소탄정")
        self.add_class("pills", 48, "메디락디에스장용캡슐")
        self.add_class("pills", 49, "배노신캡슐")
        self.add_class("pills", 50, "비엠쿨에프캡슐")
        self.add_class("pills", 51, "스티렌투엑스정")
        self.add_class("pills", 52, "써스펜8시간이알서방정650mg")
        self.add_class("pills", 53, "아세라노세미정")
        self.add_class("pills", 54, "에어낙정")
        self.add_class("pills", 55, "엘도스캡슐")
        self.add_class("pills", 56, "유로박솜정")
        self.add_class("pills", 57, "유티린정60mg")
        self.add_class("pills", 58, "캐롤에프정")
        self.add_class("pills", 59, "타이레놀정500밀리그람")
        self.add_class("pills", 60, "파크러캡슐")
        self.add_class("pills", 61, "펠루비정")
        self.add_class("pills", 62, "후루존정150밀리그램")
        self.add_class("pills", 63, "훼스탈골드정")


        self.class_name_to_ids = {'에스원엠프정40mg':1, '케이콘틴서방정':2, '레보살탄정5/160밀리그램':3, '피로펜정':4, '로이디펜캡슐':5, '카발린캡슐50mg':6, '가르젠정':7,
         '노퍼스캡슐':8, '뉴로펜익스프레스엘정':9, '닥터베아제정':10, '덱스피드연질캡슐':11, '록스펜정':12, '리렉사정':13, '뮤레스캡슐':14, '미노씬캡슐50mg':15, '서울파모티딘정20mg':16, '세라진정':17, '속시판정':18, '스토마신캡슐':19, '씬지록신정100mg':20,
         '아웃콜로프캡슐':21, '알닥톤필름코팅정25밀리그람':22, '알러딘정':23, '알피록소펜정':24, '애드빌리퀴겔연질캡슐':25, '에이프록센연질캡슐':26, '엔테론정50밀리그램':27,
         '엠피스정':28, '올나펜연질캡슐':29, '월드로신캡슐':30, '이부로엔연질캡슐':31, '이지엔6스트롱연질캡슐':32, '이지엔6애니연질캡슐':33, '캐롤디연질캡슐':34, '아스피린프로텍트정100밀리그람':35,
          '케이캡정50mg':36, '코데날정':37, '크록신정250밀리그램':38, '클라펜정':39, '타미진정':40, '페인엔젤이부연질캡슐':41, '퓨록심정250mg':42, '후리졸정':43, '다우제큐정':44, '레바스타정':45, '렉스펜정':46, '록소탄정':47, '메디락디에스장용캡슐':48,
          '배노신캡슐':49, '비엠쿨에프캡슐':50, '스티렌투엑스정':51, '써스펜8시간이알서방정650mg':52, '아세라노세미정':53, '에어낙정':54, '엘도스캡슐':55,
          '유로박솜정':56, '유티린정60mg':57, '캐롤에프정':58, '타이레놀정500밀리그람':59, '파크러캡슐':60, '펠루비정':61, '후루존정150밀리그램':62, '훼스탈골드정':63}
        # Train or validation dataset?
        assert subset in ["train", "val"]
        dataset_dir = os.path.join(dataset_dir, subset)

        # Load annotations
        # VGG Image Annotator saves each image in the form:
        # { 'filename': '28503151_5b5b7ec140_b.jpg',
        #   'regions': {
        #       '0': {
        #           'region_attributes': {},
        #           'shape_attributes': {
        #               'all_points_x': [...],
        #               'all_points_y': [...],
        #               'name': 'polygon'}},
        #       ... more regions ...
        #   },
        #   'size': 100202
        # }
        # We mostly care about the x and y coordinates of each region
        annotations = json.load(open(os.path.join(dataset_dir, "via_region_data.json")))
        annotations = list(annotations.values())  # don't need the dict keys

        # The VIA tool saves images in the JSON even if they don't have any
        # annotations. Skip unannotated images.
        annotations = [a for a in annotations if a['regions']]

        # Add images
        for a in annotations:
            # Get the x, y coordinaets of points of the polygons that make up
            # the outline of each object instance. There are stores in the
            # shape_attributes (see json format above)

            if type(a['regions']) is dict:
                polygons = [r['shape_attributes'] for r in a['regions'].values()]
                class_names = [list(r['region_attributes']['name'].keys())[0] for r in a['regions'].values()]
            else:
                polygons = [r['shape_attributes'] for r in a['regions']] 
                class_names = [list(r['region_attributes']['name'].keys())[0] for r in a['regions']]   
            # polygons = [r['shape_attributes'] for r in a['regions'].values()]
            # class_names = [s['region_attributes']['name'].keys()[0] for s in a['regions'].values()]
                print(polygons)
                print(class_names)

            
            # load_mask() needs the image size to convert polygons to masks.
            # Unfortunately, VIA doesn't include it in JSON, so we must read
            # the image. This is only managable since the dataset is tiny.
            image_path = os.path.join(dataset_dir, a['filename'])
            image = skimage.io.imread(image_path)
            height, width = image.shape[:2]

            self.add_image(
                "pills",
                image_id=a['filename'],  # use file name as a unique image id
                path=image_path,
                width=width, height=height,
                polygons=polygons,
                class_names = class_names
                )

    def load_mask(self, image_id):
        """Generate instance masks for an image.
       Returns:
        masks: A bool array of shape [height, width, instance count] with
            one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks.
        """
        # If not a fashion dataset image, delegate to parent class.
        image_info = self.image_info[image_id]
        if image_info["source"] != "pills":
            return super(self.__class__, self).load_mask(image_id)

        # Convert polygons to a bitmap mask of shape
        # [height, width, instance_count]
        info = self.image_info[image_id]
        mask = np.zeros([info["height"], info["width"], len(info["polygons"])],
                        dtype=np.uint8)
        class_ids = np.ones([mask.shape[-1]])
        for i, p in enumerate(info["polygons"]):
            # Get indexes of pixels inside the polygon and set them to 1
            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
            mask[rr, cc, i] = 1

        for i,cname in enumerate(info["class_names"]):
            class_ids[i] = self.class_name_to_ids[cname]
        # Return mask, and array of class IDs of each instance. Since we have
        # one class ID only, we return an array of 1s
        # Map class names to class IDs.
        return mask.astype(np.bool), class_ids

    def image_reference(self, image_id):
        """Return the path of the image."""
        info = self.image_info[image_id]
        if info["source"] == "pills":
            return info["path"]
        else:
            super(self.__class__, self).image_reference(image_id)


def train(model):
    """Train the model."""
    # Training dataset.
    dataset_train = PillsDataset()
    dataset_train.load_pills(args.dataset, "train")
    dataset_train.prepare()

    # Validation dataset
    dataset_val = PillsDataset()
    dataset_val.load_pills(args.dataset, "val")
    dataset_val.prepare()

    # *** This training schedule is an example. Update to your needs ***
    # Since we're using a very small dataset, and starting from
    # COCO trained weights, we don't need to train too long. Also,
    # no need to train all layers, just the heads should do it.
    print("Training network heads")
    model.train(dataset_train, dataset_val,
                learning_rate=config.LEARNING_RATE,
                # epochs=60,
                epochs=1000,
                layers='heads')


def color_splash(image, mask):
    """Apply color splash effect.
    image: RGB image [height, width, 3]
    mask: instance segmentation mask [height, width, instance count]

    Returns result image.
    """
    # Make a grayscale copy of the image. The grayscale copy still
    # has 3 RGB channels, though.
    gray = skimage.color.gray2rgb(skimage.color.rgb2gray(image)) * 255
    # We're treating all instances as one, so collapse the mask into one layer
    mask = (np.sum(mask, -1, keepdims=True) >= 1)
    # Copy color pixels from the original color image where mask is set
    if mask.shape[-1] > 0:
        # We're treating all instances as one, so collapse the mask into one layer
        mask = (np.sum(mask, -1, keepdims=True) >= 1)
        splash = np.where(mask, image, gray).astype(np.uint8)
    else:
        splash = gray.astype(np.uint8)
    return splash


def detect_and_color_splash(model, image_path=None, video_path=None):
    assert image_path or video_path

    # Image or video?
    if image_path:
        # Run model detection and generate the color splash effect
        print("Running on {}".format(args.image))
        # Read image
        image = skimage.io.imread(args.image)
        # Detect objects
        r = model.detect([image], verbose=1)[0]
        # Color splash
        splash = color_splash(image, r['masks'])
        # Save output
        file_name = "splash_{:%Y%m%dT%H%M%S}.png".format(datetime.datetime.now())
        skimage.io.imsave(file_name, splash)
    elif video_path:
        import cv2
        # Video capture
        vcapture = cv2.VideoCapture(video_path)
        width = int(vcapture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vcapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = vcapture.get(cv2.CAP_PROP_FPS)

        # Define codec and create video writer
        file_name = "splash_{:%Y%m%dT%H%M%S}.avi".format(datetime.datetime.now())
        vwriter = cv2.VideoWriter(file_name,
                                  cv2.VideoWriter_fourcc(*'MJPG'),
                                  fps, (width, height))

        count = 0
        success = True
        while success:
            print("frame: ", count)
            # Read next image
            success, image = vcapture.read()
            if success:
                # OpenCV returns images as BGR, convert to RGB
                image = image[..., ::-1]
                # Detect objects
                r = model.detect([image], verbose=0)[0]
                # Color splash
                splash = color_splash(image, r['masks'])
                # RGB -> BGR to save image to video
                splash = splash[..., ::-1]
                # Add image to video writer
                vwriter.write(splash)
                count += 1
        vwriter.release()
    print("Saved to ", file_name)


############################################################
#  Training
############################################################

if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Train Mask R-CNN to detect fashion.')
    parser.add_argument("command",
                        metavar="<command>",
                        help="'train' or 'splash'")
    parser.add_argument('--dataset', required=False,
                        metavar="/procdata/",
                        help='Directory of the dataset')
    parser.add_argument('--weights', required=True,
                        metavar="/weights.h5",
                        help="Path to weights .h5 file or 'coco'")
    parser.add_argument('--logs', required=False,
                        default=DEFAULT_LOGS_DIR,
                        metavar="/logs/",
                        help='Logs and checkpoints directory (default=logs/)')
    parser.add_argument('--image', required=False,
                        metavar="path or URL to image",
                        help='Image to apply the color splash effect on')
    parser.add_argument('--video', required=False,
                        metavar="path or URL to video",
                        help='Video to apply the color splash effect on')
    args = parser.parse_args()

    # Validate arguments
    if args.command == "train":
        assert args.dataset, "Argument --dataset is required for training"
    elif args.command == "splash":
        assert args.image or args.video,\
               "Provide --image or --video to apply color splash"

    print("Weights: ", args.weights)
    print("Dataset: ", args.dataset)
    print("Logs: ", args.logs)
    
    # Configurations
    if args.command == "train":
        config = PillsConfig()
    else:
        class InferenceConfig(PillsConfig):
            # Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1
        config = InferenceConfig()
    config.display()

    # Create model
    if args.command == "train":
        model = modellib.MaskRCNN(mode="training", config=config,
                                  model_dir=args.logs)
    else:
        model = modellib.MaskRCNN(mode="inference", config=config,
                                  model_dir=args.logs)

    # Select weights file to load
    if args.weights.lower() == "coco":
        weights_path = COCO_WEIGHTS_PATH
        # Download weights file
        if not os.path.exists(weights_path):
            utils.download_trained_weights(weights_path)
    elif args.weights.lower() == "last":
        # Find last trained weights
        weights_path = model.find_last()[1]
    elif args.weights.lower() == "imagenet":
        # Start from ImageNet trained weights
        weights_path = model.get_imagenet_weights()
    else:
        weights_path = args.weights

    # Load weights
    print("Loading weights ", weights_path)
    if args.weights.lower() == "coco":
        # Exclude the last layers because they require a matching
        # number of classes
        model.load_weights(weights_path, by_name=True, exclude=[
            "mrcnn_class_logits", "mrcnn_bbox_fc",
            "mrcnn_bbox", "mrcnn_mask"])
    else:
        model.load_weights(weights_path, by_name=True)

    # Train or evaluate
    if args.command == "train":
        train(model)
    elif args.command == "splash":
        detect_and_color_splash(model, image_path=args.image,
                                video_path=args.video)
    else:
        print("'{}' is not recognized. "
              "Use 'train' or 'splash'".format(args.command))