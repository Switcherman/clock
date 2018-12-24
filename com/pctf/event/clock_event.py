from com.pctf.entity.clock import Clock
import subprocess
import logging

logger = logging.getLogger('main')

def ring(clock):
    logger.info("clock rings, clock message is " + clock.__str__())
    r = subprocess.Popen(['mplayer', clock.sound, '-ss', clock.start, '-endpos', clock.last],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info(r.communicate()[0].decode("utf-8"))