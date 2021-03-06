'''
Write your own version of Filelog here!

The Filelog Class opens up a file and add log within. The
previous log, if any, should not be removed. Also, there
can be only one Filelog object at any time of this
program - that is, a second Filelog object will lead to
exact the same instance in the memory as the first one. 

At least three methods are required:
info(msg), warning(msg), and error(msg).
'''
from datetime import datetime

class FileLog():    
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(FileLog, self).__new__(self)
            
        self.log = open("Log.txt","a")
        self.now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        
        return self.instance
        
    def warning(self, msg):
        self.log.write(self.now+' WARNING:'+msg+'\n')
    
    def info(self, msg):
        self.log.write(self.now+' INFO:'+msg+'\n')
    
    def error(self, msg):
        self.log.write(self.now+' ERROR:'+msg+'\n')

'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''

def FileLogTest(filelogInstance = None):
    if filelogInstance == None:
        raise ValueError('Filelog Instance doesn\'t exist')

    log = filelogInstance()
    log.warning('One CS162 Filelog instance found with id ' + str(id(log)))
    log.info('Information provided')
    log.error('Error 404')
    
    log2 = filelogInstance()
    log2.warning('Another CS162 Filelog instance Found with id ' + str(id(log2)))

FileLogTest(filelogInstance = FileLog)




# Solution from class

class FileLog():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.file = "Log.txt"
            cls._instance.level = 5
        return cls._instance

    def generic(self, prefix, message, level):
        if level >= self.level:
            with open(self.file, "a") as f:
                f.write(prefix + message + "\n")

    def debug(self, message):
        self.generic("DEBUG: ", message, 4)

    def info(self, message):
        self.generic("INFO: ", message, 5)

    def warning(self, message):
        self.generic("WARNING: ", message, 6)

    def error(self, message):
        self.generic("ERROR: ", message, 7)
