import urllib
import io
import gzip
import xml
import xml.etree.ElementTree as ET

def getXmlString(file_url):
    response = getUrlFile(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    xml_file = decompressed_file.read()
    return xml_file

def getXmlroot(file_url):
    response = getUrlFile(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    xml_file = decompressed_file.read()
    root = ET.fromstring(xml_file)
    return root

def getXmlTagByXpath(xml,xpath):
    road_leve_infos = xml.findall(xpath)
    return road_leve_infos

def getUrlFile(file_url):
    return urllib.urlopen(file_url)
