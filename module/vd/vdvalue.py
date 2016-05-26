#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from module.roadLevel import roadlevel as tisv
from module.roadLevel import roadlevelvalue as roadlevelvalue
import datetime
import vdinfo
import urllib

def getVdValueUrlByDateList(dateList):
    base_url = "http://tisvcloud.freeway.gov.tw/history/vd/"
    levelValueUrl = []
    for date in dateList:
            file_base_name = "vd_value5_"
            file_extend_name = ".xml.gz"
            for m_time in roadlevelvalue.get24TimesPer5Mins():
                full_file_name = base_url + date + '/' + \
                file_base_name + m_time + file_extend_name
                levelValueUrl.append(full_file_name)

    return levelValueUrl

def getVdValuePer5Mints(fromDate, toDate):
    file_name = "vdValue.csv"
    dateList = roadlevelvalue.getHistoryDateTime(fromDate, toDate)
    file_dir = "/home/dahlong/ETC_freewaay/vd/vd_value/"
    full_file_name =  file_dir + file_name
    for fileurl in getVdValueUrlByDateList(dateList):
        #print fileurl
        try:
            print fileurl
            infoValues_xml_root = tisv.getXmlroot(fileurl)
        except:
            pass

        value_xpath = "./Infos/Info"
        infoValues = tisv.getXmlTagByXpath(infoValues_xml_root,value_xpath)

        for value in infoValues:
            try:
                routeid = getRouteIdByVdid(value.attrib["vdid"])[0].attrib["routeid"]
            except:
                routeid = ""
                pass
            #file_name = routeid +'.csv'
            #full_file_name = file_dir+file_name
            #print full_file_name
            w_string  = routeid+','+value.attrib["datacollecttime"]
            for child in value :
                w_string = w_string + ',' +child.attrib["speed"]+','+child.attrib["vsrid"]
                for gchild in child:
                    if gchild.attrib["carid"] == 'S': # S: small car, M: median car , T
                        w_string = w_string +','+ gchild.attrib["carid"]+','+gchild.attrib["volume"]

        print w_string
        with open(full_file_name,'ab') as fileWriter:
            fileWriter.write(w_string+'\n')
            #print routeid,value.attrib["datacollecttime"],value.attrib["volumn"]

def getRouteIdByVdid(vdid):
    vdinfo_root = vdinfo.getvdInfoRoot()
    info_xpath = "./Infos/Info[@vdid='"+vdid+"']"
    infos = tisv.getXmlTagByXpath(vdinfo_root,info_xpath)
    return infos

def getvdValueFilesPer5Mins(fromDate, toDate):
    dateList = roadlevelvalue.getHistoryDateTime(fromDate, toDate)
    file_dir = "/home/dahlong/ETC_freewaay/vd/vd_value/data_files/"

    for fileurl in getVdValueUrlByDateList(dateList):
        my_file_name = fileurl.split('/')[-1]
        my_file_dir = fileurl.split('/')[-2]
        my_file_full_dir = file_dir + my_file_dir + '/'

        if not os.path.exists(my_file_full_dir):
            os.makedirs(my_file_full_dir)

        urllib.urlretrieve(fileurl, filename=my_file_full_dir+my_file_name)


if __name__=="__main__":
    datefrom = datetime.date(2015,01,01)
    dateto = datetime.date(2015,01,03)

    #getVdValuePer5Mints(datefrom,dateto)
    getvdValueFilesPer5Mins(datefrom,dateto)


    '''
    info = getRouteIdByVdid("nfbVD-T88-W-1.051-M-Loop")
    print info[0].attrib["routeid"]

    vd_value_root = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/vd_info.xml.gz')
    vd_value_xml = tisv.getXmlString('http://tisvcloud.freeway.gov.tw/vd_value5.xml.gz')
    print vd_value_xml

    datelist = roadlevelvalue.getHistoryDateTime(datefrom,dateto)
    for fileurl in getVdValueUrlByDateList(datelist):
        print fileurl
    '''
