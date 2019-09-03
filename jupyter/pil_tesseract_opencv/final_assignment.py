import zipfile

from PIL import Image
from PIL import ImageDraw
import io
import pytesseract
import cv2 as cv
import numpy as np


def get_img_from_zip(zip_file, img_filename):
    img_bytes = zip_archive.open(img_filename).read()
    img = Image.open(io.BytesIO(img_bytes))

    return img


def show_faces(img, faces):
    img_redacted = img.copy()
    img_draw = ImageDraw.Draw(img_redacted)

    for x, y, w, h in faces.tolist():
        img_draw.rectangle((x, y, x + w, y + h), outline="white")

    display(img_redacted)


# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# zip files
test_zip = 'readonly/small_img.zip'
large_zip = 'readonly/images.zip'

# Checking the Zip
zip_archive = zipfile.ZipFile(test_zip)
zip_archive_files = zip_archive.namelist()
print(zip_archive_files)

# extract images
i = 1
img_info = {}

for f in zip_archive_files:
    print(f"[{i}/{len(zip_archive_files)}]: Processing file: [{f}]")

    # get img from zip
    img = get_img_from_zip(zip_archive, f)

    # prepare image
    # - resize
    # - make greyscale
    #     resize_coef = 0.5
    #     img_w = int(img.size[0] * resize_coef)
    #     img_h = int(img.size[1] * resize_coef)
    img_prepared = img.convert("L")

    #     print(f"Original image: id [{id(img)}]; size [{img.size}]")
    #     print(f"Redacted image: id [{id(img_prepared)}]; size [{img_prepared.size}]")

    #     display(img)
    #     display(img_prepared)

    # convert image [PIL -> OpenCV]
    #     img_cv = np.array(img_prepared)
    img_cv = np.array(img_prepared)
    #     print(type(img_cv))

    #     img_cv = np.array(img_gray)
    #     img_cv_gray = cv.cvtColor(img_cv, cv.COLOR_BGR2GRAY)

    print("======== [default] ========")
    #     faces = face_cascade.detectMultiScale(cv.threshold(img_cv, 155, 255, cv.THRESH_BINARY)[1])
    #     show_faces(img, faces)

    display(Image.fromarray(cv.threshold(img_cv, 140, 255, cv.THRESH_BINARY)[1], "L"))

    #     # check image for faces [default]
    #     print("======== [default] ========")
    #     faces = face_cascade.detectMultiScale(img_cv)
    #     show_faces(img, faces)

    #     # check image for faces [1.05]
    #     print("======== [1.05] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.05)
    #     show_faces(img, faces)

    #     # check image for faces [1.10]
    #     print("======== [1.10] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.10)
    #     show_faces(img, faces)

    #     # check image for faces [1.15]
    #     print("======== [1.15] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.15)
    #     show_faces(img, faces)

    #     # check image for faces [1.20]
    #     print("======== [1.20] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.20)
    #     show_faces(img, faces)

    #     # check image for faces [1.25]
    #     print("======== [1.25] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.25)
    #     show_faces(img, faces)

    #     # check image for faces [1.5]
    #     print("======== [1.5] ========")
    #     faces = face_cascade.detectMultiScale(img_cv, 1.5)
    #     show_faces(img, faces)

    # adding extracted images to dict
    #     img_info[f] = {'img': img}

    i += 1
    break

# display(img_cv_tmp)
# display(img_info)

