#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from module.roadLevel import roadlevel as tisv

vd_info_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/vd_info.xml.gz')

def getvdInfoRoot():
    return vd_info_xml

def saveVDInfotoFile():
    #info_xpath = "./Infos/Info[@locationpath='166']"
    info_xpath = "./Infos/Info"
    infos = tisv.getXmlTagByXpath(vd_info_xml,info_xpath)
    dir_path = "/home/dahlong/ETC_freewaay/vd/vd_info/"
    file_name = "vd_info.csv"
    file_path = dir_path+file_name
    print file_path
    file = open(file_path,'w')
    infos = tisv.getXmlTagByXpath(vd_info_xml,info_xpath)
    print info_xpath
    for info in infos:
        w_string = info.attrib["roadsection"].encode("utf-8")+','+\
        info.attrib["vdid"].encode("utf-8")+','+\
        info.attrib["routeid"]+','+\
        info.attrib["locationpath"]+','+info.attrib["vdtype"]+'\n'
        #with open(file_path,'ab') as file:
        file.write(w_string)

    file.close()

if __name__ == "__main__":
    saveVDInfotoFile()
    #xmlString = tisv.getXmlString('http://tisvcloud.freeway.gov.tw/vd_info.xml.gz')
    #print xmlString
