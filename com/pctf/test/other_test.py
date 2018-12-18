from com.pctf.entity.clock import clock_to_json, Clock, from_json_to_clock, dict_to_clock
import com.pctf.entity.clock
import json
c1 = Clock('*/5 * * * * * *', name='clock1', sound='/Users/lucifer/Music/无损音乐/宇多田光 - Automatic.ape')

clockStr = clock_to_json(c1)

print(clockStr)

c2 = from_json_to_clock(clockStr)

print(c2)

import os
print(os.path.join(os.path.abspath(os.path.join(os.getcwd(), '../../../')), 'clockconfiguration.json'))
configuration = os.path.join(os.path.abspath(os.path.join(os.getcwd(), '../../../')), 'clockconfiguration.json')
with open(configuration) as in_stream:
    config_array = json.loads(in_stream.read())
    for config in config_array:
        print(dict_to_clock(config))