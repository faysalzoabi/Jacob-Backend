# !/usr/bin/env python
import time
# from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.views import APIView
import os
from project.base.apps.tags.models import Pdf_documents


class FileView(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        myfile = request.FILES['filepond']
        print("name of file", myfile)
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # file_name = f'/media-files/{filename}'
        instance = Pdf_documents(report=myfile)
        print('instance', instance.save())
        self.convertingPDFtoHTML(myfile)
        return HttpResponse("Working upload")

    # def convertingPDFtoHTML(self, myfile):
    #     while not os.path.exists(f'/media-files/documents/{myfile}'):
    #         time.sleep(1)
    #     if os.path.isfile(f'/media-files/documents/{myfile}'):
    #         os.system(f'pdf2htmlEX --zoom 1.3 /media-files/documents/{myfile} --dest-dir /htmls/')

    def convertingPDFtoHTML(self, myfile):
        while not os.path.exists(f'/pdfs/{myfile}'):
            time.sleep(1)
        if os.path.isfile(f'/pdfs/{myfile}'):
            os.system(f'pdf2htmlEX --zoom 1.3 /pdfs/{myfile} --dest-dir /htmls/')