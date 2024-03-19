
# https://www.modelscope.cn/models/iic/cv_unet_face_fusion_torch/summary

import cv2
from modelscope.pipelines import pipeline
import torch
from utils.logger_settings import api_logger
import argparse

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




if(__name__ == '__main__'):
    program = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100))
    program.add_argument('-t', '--templatePath', help='templatePath',
                        dest='templatePath', type=str)
    program.add_argument('-s', '--srcPath', help='srcPath',
                        dest='srcPath', type=str)
    program.add_argument('-o', '--outPath', help='outPath',
                        dest='outPath', type=str)


    args = program.parse_args()

    templatePath = args.templatePath
    srcPath = args.srcPath
    outPath = args.outPath  