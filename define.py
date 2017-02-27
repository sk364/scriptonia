import urllib.request, urllib.parse
import xml.etree.ElementTree as ET
import sys

def get_url(word):
    url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
    apikey = '7d31f212-49ed-48a4-b5ce-a110bb0ac4b0'
    word = urllib.parse.quote(word)
    return url + word + '?key=' + apikey

def get_response(word):
    url = get_url(word)
    HTTPResponse = urllib.request.urlopen(url)
    return HTTPResponse.read().decode()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
        xml_root = ET.fromstring(get_response(word))
        for entry in xml_root.findall('entry'):
            def_tag = entry.find('def')
            if def_tag is None:
                continue
            definition = def_tag.find('dt')
            if definition is None or len(definition.text) < 3:
                continue
            definition = definition.text
            ew = entry.find('ew')
            if ew is None:
                continue
            fl = entry.find('fl')
            print(entry.find('ew').text)
            if fl is not None:
                print('\t', fl.text)
            if definition[0] == ':':
                definition = definition[1:]
            print('\t', definition)
