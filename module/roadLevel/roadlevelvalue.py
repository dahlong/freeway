#!/usr/bin/python
# -*- coding: utf-8 -*-
import roadlevel as tisv
import datetime
import unittest
import roadlevel

def getHistoryDateTime(datefrom, dateto) :
    dateList = []
    day = datetime.timedelta(days=1)
    while datefrom <= dateto:
        dateList.append(datefrom.strftime('%Y%m%d'))
        datefrom = datefrom + day
    return dateList


def getRoadLevelValueUrlByDatesList(dateList):
    base_url = "http://tisvcloud.freeway.gov.tw/history/roadlevel/"
    levelValueUrl = []
    for date in dateList:
            file_base_name = "roadlevel_value5_"
            file_extend_name = ".xml.gz"
            for m_time in get24TimesPer5Mins():
                full_file_name = base_url + date + '/' + \
                file_base_name + m_time + file_extend_name
                levelValueUrl.append(full_file_name)

    return levelValueUrl

def get24TimesPer5Mins():
    now = datetime.datetime(2016,01,01,00,00)
    timeList = []
    while now <= datetime.datetime(2016,01,01,23,55):
        five_mins = datetime.timedelta(minutes=5)
        timeList.append(now.strftime('%H%M'))
        now = now + five_mins

    return timeList

def getRoadLevelValuePer5Mints(fromDate, toDate):
    dateList = getHistoryDateTime(fromDate, toDate)
    file_dir = "/home/dahlong/ETC_freewaay/roadlevel/roadlevel_value/"
    for fileurl in getRoadLevelValueUrlByDatesList(dateList):
        #print fileurl
        try:
            print fileurl
            infoValues_xml_root = roadlevel.getXmlroot(fileurl)
        except:
            pass

        value_xpath = "./Infos/Info"
        infoValues = roadlevel.getXmlTagByXpath(infoValues_xml_root,value_xpath)

        for value in infoValues:
            file_name = value.attrib["routeid"]+'.csv'
            full_file_name = file_dir+file_name
            #print full_file_name
            with open(full_file_name,'ab') as fileWriter:
                fileWriter.write(value.attrib["routeid"]+','+value.attrib["datacollecttime"]+','+value.attrib["value"]+','+value.attrib["traveltime"]+'\n')
                #print value.attrib["datacollecttime"],value.attrib["value"],value.attrib["traveltime"]


if __name__ == "__main__":
    datefrom = datetime.date(2013,05,01)
    dateto = datetime.date(2016,04,30)
    getRoadLevelValuePer5Mints(datefrom, dateto)
