import unittest
from pyexpat import ExpatError

import xmltodict


class XMLToDict(unittest.TestCase):
    def test_SimpleXMLToDict(self):
        testDict = xmltodict.parse("<a>test</a>")
        self.assertDictEqual({"a": "test"}, testDict)

    def test_XMLWithAttributeToDict(self):
        testDict = xmltodict.parse('<a id="9" >test</a>')
        self.assertDictEqual(testDict, {"a": {'#text': 'test', '@id': '9'}})

    def test_EmptyStringToDict(self):
        self.assertRaises(ExpatError, lambda: xmltodict.parse(""))

    def test_WrongXMLFormatToDict(self):
        self.assertRaises(ExpatError, lambda: xmltodict.parse("<a"))
