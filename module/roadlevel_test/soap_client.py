#!/usr/bin/python
# -*- coding: utf-8 -*-

import TisvCloudData as tisv
'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_value.xml.gz'
xPath = "./Infos/Info[@routeid='nfb2196']"
travel_time = "./Infos/Info[@level='1']"

xml = tisv.getXmlString(file_url)
print xml

result =  tisv.getAttributeValueByXpath(file_url,travel_time,"level")
print result
'''
#==============================
'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
print tisv.getXmlString(file_url)
gat = u"快速公路72號(公館交流道到頭屋二交流道)"
roadSection = "./Infos/Info[@roadsection='"+gat+"']"
print tisv.getAttributeValueByXpath(file_url,roadSection,"routeid")
'''
#==============================
#'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
#print tisv.getXmlString(file_url)
gat = u"快速公路72號(公館交流道到頭屋二交流道)"
roadSection = "./Infos/Info[@roadsection='"+gat+"']"
roadType = "./Infos/Info[@roadtype='1']"
freeway_1 =  tisv.getAttributeValueByXpath(file_url,roadType,"roadsection")
#for section in freeway_1:
#    print section.attrib["roadsection"],section.attrib["roadtype"],section.attrib["fromkm"],section.attrib["tokm"]

#'''
#++++++++++++++++++++++++++++++
'''
file_url = 'http://tisvcloud.freeway.gov.tw/roadlevel_info.xml.gz'
root = tisv.getXmlroot(file_url)
for ele in root.iter()
'''
