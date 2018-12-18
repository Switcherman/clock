from com.pctf.entity.clock import Clock
import subprocess
def ring(clock):
    print("clock rings, clock message is " + clock.__str__())
    r = subprocess.Popen(['mplayer', clock.sound, '-ss', clock.start, '-endpos', clock.last],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(r.communicate()[0].decode("utf-8"))