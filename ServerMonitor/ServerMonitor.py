#!/usr/bin/env python
import logging
import time

def setupLogger():
    logger = logging.getLogger('MockServer')
    hdlr = logging.FileHandler('log/MockServer.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger

def main():
    i=0
    log=setupLogger()
    while(1):
        time.sleep(1)
        logMsg=""
        if i == 0:
            logMsg="Mock Server 1.0 Started"
        elif i == 1:
            logMsg="Initializing Mock Server"
        elif i == 10:
            logMsg="Mock Server Initialized"
        elif i == 11:
            logMsg="Mock Server Running"
        elif i == 25:
            logMsg="Fatal run-time error.  Shutting down"
        log.info(logMsg)

        i = i + 1

if __name__ == "__main__":
    main()




