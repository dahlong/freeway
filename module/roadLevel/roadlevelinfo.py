#!/usr/bin/python
# -*- coding: utf-8 -*-
import roadlevel as tisv

#road_level_value5_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/roadlevel_value5.xml.gz')

# freeway 1
#info_xpath = "./Infos/Info[@locationpath='166']"
#freeway 3
#info_xpath = "./Infos/Info[@locationpath='28']"
#freeway 5
#info_xpath = "./Infos/Info[@locationpath='154']"

road_level_info_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz')

def saveFreeWay1PathtoFile():
    info_xpath = "./Infos/Info[@locationpath='166']"
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    startKm = "0K+000"
    dir_path = "/home/dahlong/ETC_freewaay/roadlevel/roadlevel_info/"
    file_name = "freeway1_section.csv"
    file_path = dir_path+file_name
    print file_path
    file = open(file_path,'w')
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    print info_xpath
    for info in infos:
        w_string = info.attrib["roadsection"].encode("utf-8")+','+\
        info.attrib["routeid"]+','+\
        info.attrib["fromkm"]+','+info.attrib["tokm"]+'\n'
        file.write(w_string)

    file.close()

def saveFreeWay3PathtoFile():
    info_xpath = "./Infos/Info[@locationpath='28']"
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    startKm = "0K+000"
    dir_path = "/home/dahlong/ETC_freewaay/roadlevel/roadlevel_info/"
    file_name = "freeway3_section.csv"
    file_path = dir_path+file_name
    print file_path
    file = open(file_path,'w')
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    print info_xpath
    for info in infos:
        w_string = info.attrib["roadsection"].encode("utf-8")+','+\
        info.attrib["routeid"]+','+\
        info.attrib["fromkm"]+','+info.attrib["tokm"]+'\n'
        file.write(w_string)

    file.close()

def saveFreeWay5PathtoFile():
    info_xpath = "./Infos/Info[@locationpath='154']"
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    startKm = "0K+000"
    dir_path = "/home/dahlong/ETC_freewaay/roadlevel/roadlevel_info/"
    file_name = "freeway5_section.csv"
    file_path = dir_path+file_name
    print file_path
    file = open(file_path,'w')
    infos = tisv.getXmlTagByXpath(road_level_info_xml,info_xpath)
    print info_xpath
    for info in infos:
        w_string = info.attrib["roadsection"].encode("utf-8")+','+\
        info.attrib["routeid"]+','+\
        info.attrib["fromkm"]+','+info.attrib["tokm"]+'\n'
        file.write(w_string)

    file.close()

if __name__ == "__main__":
    saveFreeWay5PathtoFile()
    saveFreeWay3PathtoFile()
    saveFreeWay1PathtoFile()
