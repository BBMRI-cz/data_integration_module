import datetime
import logging
import os
from pyexpat import ExpatError

import xmltodict

from database.biobank_record import BiobankRecord

log = logging.getLogger(__name__)


def isValidFileType(dir_entry):
    return dir_entry.is_file() and dir_entry.name.endswith(".xml")


class FileParser:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        log.info("Initializing FileParser with directory: {dir}".format(dir=dir_path))

    def foundValidFiles(self) -> bool:
        count = 0
        for path in os.scandir(self.dir_path):
            if isValidFileType(path):
                count += 1
        log.info("Found {numOfFiles} valid files in {directory}"
                 .format(numOfFiles=count, directory=self.dir_path))
        return count > 0

    def parseXMLFilesInDir(self) -> [BiobankRecord]:
        for dirEntry in os.scandir(self.dir_path):
            if isValidFileType(dirEntry):
                fileCreationTimestamp = datetime.datetime.fromtimestamp(os.path.getctime(dirEntry))
                with open(dirEntry) as xml_file:
                    log.debug("Parsing file: {fileName}".format(fileName=dirEntry.name))
                    try:
                        yield BiobankRecord(
                            xmltodict.parse(xml_file.read()),
                            fileCreationTimestamp
                        )
                    except ExpatError:
                        log.warning("File: {fileName} is empty or has wrong format".format(fileName=dirEntry.name))
