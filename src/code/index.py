# -*- coding: utf-8 -*-
import oss2
import json
import os
from wand.image import Image
import subprocess
from skimage import metrics
import cv2


def handler(event, context):
    evt = json.loads(event)
    creds = context.credentials
    auth = oss2.StsAuth(creds.access_key_id,
                        creds.access_key_secret, creds.security_token)
    endpoint = "oss-{}-internal.aliyuncs.com".format(context.region)
    if evt.get('region') and evt.get('region') != context.region:
        endpoint = "oss-{}.aliyuncs.com".format(evt.get('region'))
    bucketName = evt.get('bucket')
    bucket = oss2.Bucket(auth, endpoint, bucketName)
    image = evt['image']
    (_, filename) = os.path.split(image)
    image_path = '/tmp/{}'.format(filename)
    new_image_path = '/tmp/new_{}'.format(filename)
    bucket.get_object_to_file(image, image_path)
    quality = evt['quality']
    (fn, extension) = os.path.splitext(filename)
    if extension == '.png':
        subprocess.check_call('./pngquant --quality {}-{} {}'.format(
            int(quality*0.75), int(quality*1.2), image_path), shell=True)
        new_image_path = '/tmp/{}-fs8.png'.format(fn)
    else:
        with Image(filename=image_path) as img:
            img.compression_quality = quality
            img.save(filename=new_image_path)
    dst = evt['dst']
    bucket.put_object_from_file(os.path.join(dst, filename), new_image_path)

    if evt.get("get_ssim"):
        print("start compute SSIM ...")
        try:
            img1 = cv2.imread(image_path)
            img2 = cv2.imread(new_image_path)
            img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            ssim = metrics.structural_similarity(img1_gray, img2_gray)
        except Exception as e:
            raise e
        finally:
            os.remove(image_path)
            os.remove(new_image_path)

        return ssim
    else:
        return -1
