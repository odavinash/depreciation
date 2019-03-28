from django.db import models
import uuid
import os
import xlrd
from collections import OrderedDict
import simplejson as json


# Create your models here.


def get_upload_path_excel(instance, filename):
    return os.path.join('excel', '', '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1]))

def get_upload_path_json(instance, filename):
    return os.path.join('json', '', '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1]))

class Depreciation(models.Model):

    depreciation_id = models.AutoField(primary_key=True, null=False)
    excel_path = models.FileField(upload_to=get_upload_path_excel, help_text='excel file', blank=True, default='')
    json_path = models.FileField(upload_to=get_upload_path_json, help_text='json file', blank=True, default='')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        excel_file_path = self.excel_path.url[1:]
       	wb = xlrd.open_workbook(excel_file_path)
        sh = wb.sheet_by_index(0)
        depreciation_list = []
        depreciation_brand_list = []
        depreciation_model_list = []
        depreciation_brand_model_list = []

        keys = []

        for rownum in range(1, sh.nrows):
            depreciation = OrderedDict()
            row_values = sh.row_values(rownum)

            if rownum == 1:
                keys = row_values
                continue;

            #For all data
            for i, key_val in enumerate(keys):
                if type(key_val) is float:
                    key_val = int(key_val)
                depreciation[key_val] = int(row_values[i]) if type(row_values[i]) is float else row_values[i]
            depreciation_list.append(depreciation)

            depreciation_brand_list.append(row_values[2])

            depreciation_model_list.append(row_values[3])

            depreciation_brand_model = OrderedDict()
            depreciation_brand_model['MarkaAdı'] = row_values[2]
            depreciation_brand_model['TipAdı'] = row_values[3]
            depreciation_brand_model_list.append(depreciation_brand_model)

        #Serialize the list of dicts to JSON
        depreciation_brand_list = set(depreciation_brand_list)
        depreciation_brand_list = list(depreciation_brand_list)
        depreciation_brand_list.sort()
        j = json.dumps(depreciation_brand_list)
        with open('media/json/depreciation_brand.json', 'w') as f:
        	f.write(j)

        depreciation_model_list = set(depreciation_model_list)
        depreciation_model_list = list(depreciation_model_list)
        depreciation_model_list.sort()
        print(depreciation_model_list)
        j = json.dumps(depreciation_model_list)
        with open('media/json/depreciation_model.json', 'w') as f:
        	f.write(j)

        j = json.dumps(depreciation_brand_model_list)
        with open('media/json/depreciation_brand_model.json', 'w') as f:
            f.write(j)

        j = json.dumps(depreciation_list)
        with open('media/json/depreciation.json', 'w') as f:
        	f.write(j)















# class Depreciation(models.Model):

#     depreciation_id = models.AutoField(primary_key=True, null=False)
#     excel_path = models.FileField(upload_to=get_upload_path_excel, help_text='excel file', blank=True, default='')
#     json_path = models.FileField(upload_to=get_upload_path_json, help_text='json file', blank=True, default='')
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         excel_file_path = self.excel_path.url[1:]
#         wb = xlrd.open_workbook(excel_file_path)
#         sh = wb.sheet_by_index(0)
#         depreciation_list = []
#         depreciation_brand_list = []
#         depreciation_model_list = []
#         depreciation_brand_model_list = []

#         for rownum in range(2, sh.nrows):
#             depreciation = OrderedDict()
#             row_values = sh.row_values(rownum)
#             depreciation['MarkaKodu'] = row_values[0]
#             depreciation['TipKodu'] = row_values[1]
#             depreciation['MarkaAdı'] = row_values[2]
#             depreciation['TipAdı'] = row_values[3]
#             depreciation['2019'] = row_values[4]
#             depreciation['2018'] = row_values[5]
#             depreciation['2017'] = row_values[6]
#             depreciation['2016'] = row_values[7]
#             depreciation['2015'] = row_values[8]
#             depreciation['2014'] = row_values[9]
#             depreciation['2013'] = row_values[10]
#             depreciation['2012'] = row_values[11]
#             depreciation['2011'] = row_values[12]
#             depreciation['2010'] = row_values[13]
#             depreciation['2009'] = row_values[14]
#             depreciation['2008'] = row_values[15]
#             depreciation['2007'] = row_values[16]
#             depreciation['2006'] = row_values[17]
#             depreciation['2005'] = row_values[18]

#             depreciation_brand_list.append(row_values[2])

#             depreciation_model_list.append(row_values[3])

#             depreciation_list.append(depreciation)

#             depreciation_brand_model = OrderedDict()
#             depreciation_brand_model['MarkaAdı'] = row_values[2]
#             depreciation_brand_model['TipAdı'] = row_values[3]
#             depreciation_brand_model_list.append(depreciation_brand_model)

#         #Serialize the list of dicts to JSON
#         depreciation_brand_list = set(depreciation_brand_list)
#         depreciation_brand_list = list(depreciation_brand_list)
#         j = json.dumps(depreciation_brand_list)
#         with open('media/json/depreciation_brand.json', 'w') as f:
#             f.write(j)

#         depreciation_model_list = set(depreciation_model_list)
#         depreciation_model_list = list(depreciation_model_list)
#         j = json.dumps(depreciation_model_list)
#         with open('media/json/depreciation_model.json', 'w') as f:
#             f.write(j)

#         j = json.dumps(depreciation_brand_model_list)
#         with open('media/json/depreciation_brand_model.json', 'w') as f:
#             f.write(j)

#         j = json.dumps(depreciation_list)
#         with open('media/json/depreciation.json', 'w') as f:
#             f.write(j)