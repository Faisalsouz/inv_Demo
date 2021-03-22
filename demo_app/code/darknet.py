# from bs4 import BeautifulSoup
# import requests
# from pprint import pprint
# import json
# import csv
# import pandas as pd
# import os
# from django.core.files.storage import default_storage
# from django.core.files import File
# from django.http import HttpResponse
# from zipfile import ZipFile
#
#




from demo_app.code.dn_main import *

import os
import cv2
#from PIL import Image
def prediction (image,out_name,thold  = 0.50):
    '''

    :param image: in memoery image or img path
    :param thresh: threshhold of the model dectiontion. higher the threshold less classed dectected by model
    :return: none
    :outname=name of img if you want to save it.
    '''
    # from dn_img_main import *
    cfg_file = "./demo_app/code/yolo-obj.cfg"
    obj_file = "./demo_app/code/obj.data"
    weights = "./demo_app/code/yolo-obj_best.weights"
    #folder = './demo_app/code/data'
    #network,classnames,classcolor=load_network(config_file=cfg_file,data_file=obj_file,weights=weights)

            #os.path.encode('utf-8')
            #path=os.path.join(folder,f)
            #pathb=path.encode('utf-8')
    img=cv2.imread(image,cv2.COLOR_BGR2RGB)
    #img=cv2.imread(image)


            #print(img)
    i=0
    res=performDetect(imagePath=image,configPath=cfg_file,weightPath=weights,metaPath=obj_file,thresh=thold,showImage=False)
    print(res)
    while i<len(res):
        res_type = res[i][0]
        if 'rec_add' in res_type:
            color_box=(0,0,255)
        elif 'date' in res_type:
            color_box=(21, 64, 158)
        elif 'Inv_num' in res_type:
            color_box=(144, 12, 63  )
        elif 'Kunden_num' in res_type:
            color_box=(168, 30, 136  )
        elif 'Cell' in res_type:
            color_box=(34, 110, 22)
        elif 'Total' in res_type:
            color_box=(21, 236, 133 )
        elif 'Tax' in res_type:
            color_box=(21, 236, 133 )
        elif 'column' in res_type:
            color_box = (200, 50, 22)

        center_x = int(res[i][2][0])
        center_y = int(res[i][2][1])
        width = int(res[i][2][2])
        height = int(res[i][2][3])

        UL_x = int(center_x - width / 2)  # Upper Left corner X coord
        UL_y = int(center_y - height / 2)  # Upper left Y
        LR_x = int(center_x + width / 2)
        LR_y = int(center_y - height / 2)
        cv2.rectangle(img, (UL_x, UL_y), (UL_x + width, UL_y + height), color_box, 4)  #
        # put label on bounding box
        font = cv2.FONT_HERSHEY_SIMPLEX  #
        cv2.putText(img, res_type, (center_x, center_y), font, 2, color_box, 2, cv2.LINE_AA)  #
        i = i + 1
        print('starting second loop over same image')
    cv2.imwrite(os.path.join('./output',out_name), img)
    print('jobDone!!')







