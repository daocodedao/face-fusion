
# https://www.modelscope.cn/models/iic/cv_unet_face_fusion_torch/summary

import cv2
from modelscope.pipelines import pipeline
import torch
from utils.logger_settings import api_logger

device = "cuda:0"
if torch.cuda.device_count() > 0:
    device = "cuda:1"

# exit(0)
def mergeFace(template_path, user_path, outPath):
    api_logger.info(f"template_path={template_path} user_path={user_path} outPath={outPath}")
    image_face_fusion = pipeline('face_fusion_torch',
                                model='damo/cv_unet_face_fusion_torch', 
                                model_revision='v1.0.3',
                                device="cuda:0")

    print(template_path)
    result = image_face_fusion(dict(template=template_path, user=user_path))

    cv2.imwrite(outPath, result['output_img'])
    api_logger.info('finished!')