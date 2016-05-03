#!/usr/bin/python
# -*- coding: utf-8 -*-
import tisv_cloud_data as tisv

#'''
def getRoadLevelInfo(xml,xpath):
    road_leve_infos = xml.findall(xpath)
    return road_leve_infos

#def getRoadLLevelValue(xml,xpath):
#    road_leve_values = xml.findall(xpath)
#    return road_leve_values

road_level_value_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/roadlevel_value.xml.gz')
road_level_info_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz')

# freeway 1
#value_xpath = "./Infos/Info[@locationpath='166']"
#freeway 3
#value_xpath = "./Infos/Info[@locationpath='28']"
#freeway 5
value_xpath = "./Infos/Info[@locationpath='154']"

RoadLevelValue_freeway_1 = getRoadLevelInfo(road_level_info_xml,value_xpath)

for info in RoadLevelValue_freeway_1:
    roadlevel_value_xpath = "./Infos/Info[@routeid='"+info.attrib["routeid"]+"']"
    #print roadlevel_value_xpath
    value = getRoadLevelInfo(road_level_value_xml,roadlevel_value_xpath)

    print info.attrib["roadsection"].encode("utf-8"),\
    'startKM :',info.attrib["fromkm"], \
    'endKM :',info.attrib["tokm"],\
    'speed :',value[0].attrib["value"],\
    'traveltime :',value[0].attrib["traveltime"],\
    'locationpath',info.attrib['locationpath']

    #if info.attrib["tokm"] == "374K+400":
    #    exit

#'''

'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_value.xml.gz'
#xPath = "./Infos/Info[@routeid='nfb2196']"
#travel_time = "./Infos/Info[@level='1']"
gat = u"國道一號"
xpath = "./Info/Info[starts-with(@roadsection,"+gat+")]"

#xml = tisv.getXmlString(file_url)
road_level_infos_xml = tisv.getXmlroot('http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz')
#print xml

infos =  tisv.getAttributeValueByXpath(file_url,xpath,"level")
for info in infos:
    #print info.items()
    #print info.attrib["routeid"],'speed :',info.attrib["value"],'travelTime :',info.attrib["traveltime"]
    xpath_1 = "./Infos/Info[@routeid='"+info.attrib["routeid"]+"']"
    #print xpath_1
    roadSection = getRoadLevelInfo(road_level_infos_xml,xpath_1)
    print roadSection.attrib["roadsection"].encode("utf-8"),'speed :',info.attrib["value"],'travelTime :',info.attrib["traveltime"] \
    , 'fromkm :',roadSection.attrib["fromkm"],' tokm :',roadSection.attrib["tokm"]

'''
#==============================

'''
file_url2 = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
routeid = "nfb2196"
roadid = "./Infos/Info[@routeid='nfb2189']"
#roadid = "./Infos/Info"
print roadid
road_leve_infos = tisv.getAttributeValueByXpath(file_url2,roadid,"roadSection")
print road_leve_infos[0].attrib["roadsection"].encode("utf-8")
#for info in road_leve_infos:
#    print info.attrib["roadsection"].encode("utf-8")
'''

'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
#print tisv.getXmlString(file_url)
gat = u"快速公路72號(公館交流道到頭屋二交流道)"
roadSection = "./Infos/Info[@roadsection='"+gat+"']"
print tisv.getAttributeValueByXpath(file_url,roadSection,"routeid")
'''
#==============================
'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
#print tisv.getXmlString(file_url)
#roadType = "./Infos/Info[@locationpath='166']"
roadType = "./Infos/Info"
freeway_1 =  tisv.getAttributeValueByXpath(file_url,roadType,"roadsection")
for section in freeway_1:
    print section.attrib["roadsection"].encode("utf-8"),section.attrib["routeid"],section.attrib["locationpath"],section.attrib["fromkm"],section.attrib["tokm"]

'''
#++++++++++++++++++++++++++++++

'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
root = tisv.getXmlroot(file_url)
for ele in root.iter()
'''

#==============================
'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
gat = u"國道一號"
xpath = "./Info/Info[starts-with(@roadsection,"+gat+")]"
freeway_1 =  tisv.getAllByXpathStartWith(file_url,xpath)
for section in freeway_1:
    print section.attrib["roadsection"].encode("utf-8"),section.attrib["routeid"],section.attrib["roadtype"],section.attrib["fromkm"],section.attrib["tokm"]
'''
