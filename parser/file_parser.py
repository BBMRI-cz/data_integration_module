import logging
import os

log = logging.getLogger(__name__)


class FileParser:
    dir_path = "/Users/radot/Projects/data_integration_module/dummy_files"

    def foundValidFiles(self) -> bool:
        count = 0
        for path in os.scandir(self.dir_path):
            if path.is_file():
                count += 1
        log.info("Found {numOfFiles} valid files in {directory}".format(numOfFiles=count, directory=self.dir_path))
        return count > 0
