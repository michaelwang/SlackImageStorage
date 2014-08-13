from dbHandler import DBHandler
from fileHandler import FileHandler
import unittest

class TestHander(unittest.TestCase):
    dbHandler = None;
    fileHandler = None;
    
    def setUp(self):
        self.dbHandler = DBHandler()
        self.fileHandler = FileHandler(5)

    def testFileHanderSave(self):
        path = '/home/michael/license.txt'
        import os
        if not os.path.isfile(path):
           os.mknod(path)
        self.fileHandler.save(path,'aa')

    def testGetTotalFileCount(self):
        num = self.fileHandler.getTotalFileCount()
        print "file count : " + str(num)
    
    def testExecute(self):
        sql = 'select * from files'
        rows = self.dbHandler.excute(sql)

if __name__ == '__main__':
    unittest.main()
