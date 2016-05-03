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
    #root = ET.fromstring(xml_file)
    return xml_file

def getXmlroot(file_url):
    response = getUrlFile(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    xml_file = decompressed_file.read()
    root = ET.fromstring(xml_file)
    return root


def getAttributeValueByXpath(file_url, xPath, attribute):
    response = getUrlFile(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    xml_file = decompressed_file.read()
    root = ET.fromstring(xml_file)
    #return root.find(xPath).attrib[attribute]
    return root.findall(xPath)

def getAllByXpathStartWith(file_url, xPth):
    response = getUrlFile(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    xml_file = decompressed_file.read()

    root = ET.fromstring(xml_file)
    return root.getroot()

def getUrlFile(file_url):
    return urllib.urlopen(file_url)

def hello():
    return "hi"

def test_suit():
    test_getAttributeValueByXpath()

def test_getAttributeValueByXpath():
    print getAttributeValueByXpath('http://tisvcloud.freeway.gov.tw/roadlevel_value.xml.gz',"./Infos/Info[@routeid='nfb2196']","value")

    x_path = "./Infos/Info[@routeid='"+"nfb2196"+"']"
    print getAttributeValueByXpath('http://tisvcloud.freeway.gov.tw/roadlevel_value.xml.gz',x_path,"value")


if __name__=="__main__":
    test_suit()
