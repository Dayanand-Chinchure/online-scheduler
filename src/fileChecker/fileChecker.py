import os,shutil,time,tarfile
import logging, ConfigParser, inspect, traceback, sys

funArgsDict = {}
def poorMansEnum(**es):
    return type('Enum', (), es)

errors = poorMansEnum(errSuccess=0, errIO=1, errCmd=2, errOther='other')

#process any cmds given by the user
#this is the only way to give commands to this process

def processCmd(cmdFilePath):
  cmds = ['pause', 'resume', 'stop', 'reconf', 'stat']
  try:
    cmdfile = open (cmdFilePath, 'r')
  except IOError:
    s = traceback.format_exc()
    serr = "Error text:\n%s\n" %(s)
    sys.stderr.write(serr)
    return (errors.errIO, '')
  #read the command
  cmdtxt = cmdfile.readline().rstrip()
  #process if valid
  return (errors.errSuccess, cmdtxt)

#useful function for logging
def lineno():
    return inspect.currentframe().f_back.f_lineno

#dummy cmd processing functions
def resumeFunc(): print 'printing resume...' 
def statFunc(): print 'printing stats...'
def pauseFunc(): print 'printing pause...'
def reconfFunc(): print 'printing reconf...'
def stopFunc(): 
 print 'printing stop...' 
 exit(0)

#infinitely looping function 
def processFiles():
    print 'test print ', funArgsDict ['watchDirPath'] 
    watchDirPath = funArgsDict['watchDirPath']
    delay = funArgsDict['delay']
    cmdFilePath = funArgsDict['cmdFilePath']
    state = 'resume'
    #dictionary of (cmd,function)
    dictCmdFuncs = {'resume' : resumeFunc,
                    'stat' : statFunc,
                    'pause' : pauseFunc,
                    'reconf' : reconfFunc,
                    'stop' : stopFunc
                    }
    while True:
        print 'watching directory: ', watchDirPath
        (errcode, cmd) = processCmd(cmdFilePath)
        if errcode != errors.errSuccess:
          print 'cmd file error'
          dictCmdFuncs['stop']()
        else:
          dictCmdFuncs[cmd]()
        print 'sleeping for ', delay , ' seconds'
        time.sleep(delay)
if __name__=='__main__':
  confsuccess = False
  try:
    config = ConfigParser.ConfigParser()
    config.read(sys.argv[1])
    funArgsDict ['watchDirPath'] = config.get('settings','watchDirPath')
    funArgsDict ['delay'] = float(config.get('settings','delay'))
    funArgsDict ['cmdFilePath'] = config.get('settings','cmdFilePath')
    confsuccess = True
  except Exception:
    s = traceback.format_exc()
    serr = "Error description:\n%s\n" %(s)
    sys.stderr.write(serr)
    confsuccess = False
  if confsuccess:
    print 'watching directory: ', funArgsDict ['watchDirPath']
    processFiles()

