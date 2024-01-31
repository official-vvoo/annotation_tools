from PySide6.QtGui import QKeyEvent, QPixmap, QImage
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from mainUI import Ui_MainWindow

# from PySide6.QtCore import QDir
import os
import cv2
import json
import numpy as np

CONST_EXT_MASK = ".txt"
CONST_EXT_LABEL = ".json"

CONST_LIST_IMAGE = [".jpg", ".png"]

def check_path(path, make:bool=False):
    if os.path.exists(path):
        return True
    else:
        if make:
            os.makedirs(path)
            return True
        else:
            False

def mask_bbox(image, boxes):
    h, w, c = image.shape
    for box in boxes:
        xn, yn, wn, hn = [float(x) for x in box[1:]]
        pt1 = (int(xn*w-(wn*w/2)), int(yn*h-(hn*h/2)))
        pt2 = (int(xn*w+(wn*w/2)), int(yn*h+(hn*h/2)))
        image = cv2.rectangle(image, pt1, pt2, color=(0, 0, 0))
        image = cv2.putText(image, box[0], pt1, 1, 2, (0, 0, 0), 2)
    
    return image

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
        
        self.view_option = None
        self.masks_path = None
        self.label = None
        self.mask_path = None

    def main(self):
        
        # click buttons
        self.loadImageButton.clicked.connect(self.load_image)
        self.loadMaskButton.clicked.connect(self.load_mask)
        self.loadLabelButton.clicked.connect(self.load_label)

        self.viewBboxButton.clicked.connect(self.select_bbox_view_option)
        self.viewSegmButton.clicked.connect(self.select_segm_view_option)
        self.viewClasButton.clicked.connect(self.select_clas_view_option)

    def load_image(self):
        window = QFileDialog()
        self.images_path = window.getExistingDirectory()
        self.imageListViewer.clear()
        self.image_list = [x for x in os.listdir(self.images_path) if os.path.splitext(x)[-1] in CONST_LIST_IMAGE ]

        self.image_list.sort()
        for f in self.image_list:
            self.imageListViewer.addItem(f)

    def load_mask(self):
        window = QFileDialog()
        self.masks_path = window.getExistingDirectory()
        self.mask_list = [x for x in os.listdir(self.masks_path) if os.path.splitext(x)[-1] == CONST_EXT_MASK]
    
    def load_label(self):
        window = QFileDialog()
        labels_path = window.getOpenFileName()
        if os.path.splitext(labels_path)[-1] == CONST_EXT_LABEL:
            self.labels_path = labels_path
            with open(self.labels_path, 'r+') as f:
                self.label = json.loads(f)
    
    def select_bbox_view_option(self):
        self.view_option = "bbox"
        print(self.view_option)

    def select_segm_view_option(self):
        self.view_option = "segmentation"
        print(self.view_option)

    def select_clas_view_option(self):
        self.view_option = "class"
        print(self.view_option)

    def select_image_masks(self, image_name):
        masks_name = image_name.replace(os.path.splitext(image_name)[-1], CONST_EXT_MASK)
        self.mask_path = os.path.join(self.masks_path, masks_name)
        if os.path.exists(self.mask_path) == False:
            self.mask_path = None
            return False
        
        with open(os.path.join(self.mask_path), 'r') as f:
            masks = f.readlines()

        self.maskInfoEdit.setPlainText(''.join(masks))
        masks = [x.split('\n')[0].split(' ') for x in masks]
        
        return masks

    def select_image_labels(self, image_name):
        pass

    def display_image_with_masks(self, image_name, image_masks):
        if self.masks_path:
            self.mask_info = self.select_image_masks(image_name)
            if self.mask_info:
                image_masks = mask_bbox(image_masks, self.mask_info)
            else:
                self.maskInfoEdit.clear()
        height, width, channel = image_masks.shape
        bytesPerLine = 3 * width
        qImg = QImage(image_masks, width, height, bytesPerLine, QImage.Format_RGB888)
        self.imageMaskViewer.setPixmap(QPixmap.fromImage(qImg))# , IMREAD_COLOR)
        self.imageMaskViewer.setScaledContents(True)

    def display_image_with_labels(self, image_name, image_labels):
        if self.label:
            self.label_info = self.select_image_labels(image_name)
            if self.view_option == "bbox":
                image_labels = cv2.rectangle(image_labels, ())
            elif self.view_option == "segmentation":
                image_labels = cv2.polylines(image_labels, self.label_info  )

        height, width, _ = image_labels.shape
        bytesPerLine = 3 * width
        qImg = QImage(image_labels, width, height, bytesPerLine, QImage.Format_RGB888)
        self.imageLabelViewer.setPixmap(QPixmap.fromImage(qImg))
        self.imageLabelViewer.setScaledContents(True)

    def image_selection_changed(self):
        image_name = self.imageListViewer.currentItem().text()
        print(os.path.join(self.images_path, image_name))
        image = cv2.imread(os.path.join(self.images_path, image_name))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
        ## display image in Mask Info tab
        if self.tabWidget.currentWidget().objectName() == self.MaskTab.objectName():
            self.display_image_with_masks(image_name, image)

        ## display image in Label Info tab
        if self.tabWidget.currentWidget().objectName() == self.LabelTab.objectName():
        # self.imageLabelViewer.setPixmap(QPixmap(os.path.join(self.images_path, image_name)))
            self.display_image_with_labels(image_name, image)
    
    # press keybaord
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_S:
            text = self.maskInfoEdit.toPlainText()
            if self.mask_path == None:
                print('pass')
            with open(os.path.join(self.mask_path), 'w') as f:
                f.write(text)
            

if __name__ == "__main__":
    app = QApplication()
    win = MyApp()
    win.show()
    app.exec()