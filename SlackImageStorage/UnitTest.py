from dbHandler import DBHandler
from fileHandler import FileHandler
import unittest

class TestHander(unittest.TestCase):
    dbHandler = None;
    fileHandler = None;
    
    def setUp(self):
        self.dbHandler = DBHandler()
        self.fileHandler = FileHandler(5)

    def testFileHanderSave(self,url = 'aa'):
        path = '/tmp/license.txt'
        import os
        if not os.path.isfile(path):
           os.mknod(path)
        fileId,physicalName = self.fileHandler.save(path,url)
        return fileId,physicalName
    
    def testGetFileByPhysicalName(self):
        fileId,physicalName = self.testFileHanderSave()
        fileObj = self.fileHandler.getFileByDiskName(physicalName)
        
    
    def testGetFiletypeByURL(self):
        url = 'http://www.abc.com'
        self.testFileHanderSave(url)
        print 'file type is :' + self.fileHandler.getTypeByUrl(url)
        
    def testGetFileByID(self):
        fileId,physicalName = self.testFileHanderSave()
        opendFile = self.fileHandler.getFileByID(fileId)
         
    def testGetFiletypeByID(self):
        fileId,physicalName = self.testFileHanderSave()
        print self.fileHandler.getTypeByID(fileId)

    def testGetTotalFileCount(self):
        num = self.fileHandler.getTotalFileCount()
        print "file count : " + str(num)

    def testExecute(self):
        sql = 'select * from files'
        rows = self.dbHandler.excute(sql)


    

if __name__ == '__main__':
    unittest.main()
