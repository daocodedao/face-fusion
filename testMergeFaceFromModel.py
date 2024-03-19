
# https://www.modelscope.cn/models/iic/cv_unet_face_fusion_torch/summary

import cv2
import platform
import torch
from utils.logger_settings import api_logger
from utilMergeFaceFromModel import mergeFace

if platform.system() == "linux":
    template_path = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_template.jpg'
    user_path = 'https://modelscope.oss-cn-beijing.aliyuncs.com/test/images/facefusion_user.jpg'
else:
    template_path = './images/liudehua.jpg'
    user_path = './images/zhoujielun.jpg'

outPath = "./out/mergeface.jpg"
mergeFace(template_path, user_path, outPath)
print("done")