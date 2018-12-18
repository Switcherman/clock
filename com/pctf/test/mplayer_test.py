#!/usr/bin/env python
#coding: utf-8

import subprocess
import time
filePath = '/Users/lucifer/Music/无损音乐/周杰伦-止战之殇.ape'

r = subprocess.Popen(['mplayer', filePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

command = input('command: ')

if 'q' == command:
    r.terminate()
    time.sleep(10)