#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import os
import nibabel as nib
import shutil

def get_hipvlousum(username, MRI_Name):
    print('gethip')
    pred_path =  r'D:\AD_Prediction\Project\ADMS\static\requiredimages\expert'
    basename =  username + "/upload/"
    pred_path = os.path.join(pred_path, basename)

    #pred_path = "../static/requiredimages/expert/" + username + "/upload/"
    # 单独测试用
    # pred_path = "../static/requiredimages/admin/Pred/"
    if not os.path.exists(pred_path):
        os.makedirs(pred_path)
    tlabel = nib.load(pred_path +  MRI_Name)
    label = tlabel.get_fdata()
    label = label.transpose(2,1,0)
    label = label[::-1,::-1,:]
    bool_label = label.astype(np.bool)
    hipvolu_sum = np.sum(bool_label)
    print(hipvolu_sum)
    if 1000 <= hipvolu_sum <= 2000:
        hipvolu_sum *= 2.5
    elif 500 < hipvolu_sum < 1000:
        hipvolu_sum *= 4
    elif 300 <=hipvolu_sum <=500:
        hipvolu_sum *= 6
    elif 200 < hipvolu_sum <300:
        hipvolu_sum *= 10
    elif 150 < hipvolu_sum <= 200:
        hipvolu_sum *= 15
    elif 100 < hipvolu_sum <= 150:
        hipvolu_sum *= 20
    elif 1 < hipvolu_sum <= 100:
        hipvolu_sum *= 25
    if hipvolu_sum:
        print(hipvolu_sum)
        hipvolu_sum = int(hipvolu_sum)
        return hipvolu_sum
    else:
        print("数量为空！")
        return 0

def get_PredHipvlouSum(MRI_Name):
    print('getpred')
    pred_path = r'D:\AD_Prediction\Project\ADMS\static\requiredimages\admin\Pred/'

    # 单独测试用
    # pred_path = "../static/requiredimages/admin/Pred/"
    if not os.path.exists(pred_path):
        os.makedirs(pred_path)
    tlabel = nib.load(pred_path +  MRI_Name)
    label = tlabel.get_fdata()
    label = label.transpose(2,1,0)
    label = label[::-1,::-1,:]
    bool_label = label.astype(np.bool)
    hipvolu_sum = np.sum(bool_label)
    print(hipvolu_sum)
    if 1000 <= hipvolu_sum <= 2000:
        hipvolu_sum *= 2.5
    elif 500 < hipvolu_sum < 1000:
        hipvolu_sum *= 4
    elif 300 <=hipvolu_sum <=500:
        hipvolu_sum *= 6
    elif 200 < hipvolu_sum <300:
        hipvolu_sum *= 10
    elif 150 < hipvolu_sum <= 200:
        hipvolu_sum *= 15
    elif 100 < hipvolu_sum <= 150:
        hipvolu_sum *= 20
    elif 1 < hipvolu_sum <= 100:
        hipvolu_sum *= 25
    if hipvolu_sum:
        print(hipvolu_sum)
        hipvolu_sum = int(hipvolu_sum)
        return hipvolu_sum
    else:
        print("数量为空！")
        return 0



# if __name__ == '__main__':
#     name = "ADNI_002_S_0295_13722.nii"
#     name1 = "ADNI_002_S_0295_MR_HarP_135_final_release_2015_Br_20150226095012465_S13408_I474728.nii"
#     name2 = "ADNI_002_S_0295_13722-dense-uU-pred.nii"
#     name3 = "ADNI_002_S_0413_14437-dense-uU-pred.nii"
#     name4 = "ADNI_002_S_0413_MR_HarP_135_final_release_2015_Br_20150226110131972_S13893_I474824.nii"
    # get_hipvlousum(username=None, MRI_Name=name)
    # get_hipvlousum(username=None, MRI_Name=name1)
    # get_hipvlousum(username=None, MRI_Name=name2)
    # get_hipvlousum(username=None, MRI_Name=name3)
    # get_hipvlousum(username=None, MRI_Name=name4)


