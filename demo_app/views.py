from django.shortcuts import render
# from demo_app.models import Document
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.http import HttpResponse
from pdf2image import convert_from_path, convert_from_bytes
import os
from demo_app.code.darknet import prediction
from demo_app.code import *
from demo_app.code.dn_main import performDetect
#import supporting material of darknet to run both, prediction and perfromDetech function below
#from demo_app.code.dn_main import performDetect
from PIL import Image
import numpy as np

#from demo_main.demo_app.code.main_scraper impoer_py
#import csv
# Create your views here.
# def main_page(request):
#     return render(request,'page1.html',{})

def home(reqeust):
    if reqeust.method == 'POST' and reqeust.FILES['myfile']:#django gets the file naem in dictionry file
        fl=reqeust.FILES['myfile'].read()# memnory fiel is mostly not processed by libraries so need read()
        file_name=reqeust.FILES['myfile'].name
        if file_name.endswith('.pdf'):
            pages=convert_from_bytes(fl,300)#other option is read from file path.
            i=1
            for page in pages:#iteration over the pages
                save_pages = 'Page_no' + str(i) + ".jpg"
                #print(type(page))
                page.save(os.path.join('./media', file_name + save_pages), 'JPEG')
                print(os.getcwd())
                prediction(os.path.join('./media', file_name + save_pages),save_pages)
                #resquestion .file.name just gives you nam of file
                i += 1

                print('file{} and pages_No{} is processed'.format(file_name, save_pages))


        elif file_name.endswith('.jpg'):
            fs = FileSystemStorage()
            #print(type(fl))
            fs.save('./media/'+file_name, fl)
            prediction(fl,file_name)
        #print(filename)
    context={}
    return render(reqeust,'page1.html',context)
def scraper_main(reqeust):

    if reqeust.method == 'POST' and reqeust.FILES['myfile']:

        myfile = reqeust.FILES['myfile']

        #fs = FileSystemStorage()
        #filename = fs.save('file_1.xlsx', myfile)
        uploaded_file_url = myfile#fs.url(filename)
        if myfile:
            scraper_py(myfile)

        return render(reqeust, 'em_scrap.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(reqeust, 'em_scrap.html')
# async def output(request):
#
#     res= await scraper_py(file)
#
#     return render(request, 'em_scrap.html')
#        # return(res)

def download_zip(request):
    res = test_zip()
    return (res)



    #return render(request,'em_scrap.html', {'output_k': out})


def how_to(reqeust):

    context={}
    return render(reqeust,'Howto.html',context)

