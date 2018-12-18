import json
class Clock(object):

    def __init__(self, cron, name='alarm', sound='default', enabled=True, start='0', last='30'):
        self.cron = cron
        self.name = name
        self.sound = sound
        self.enabled = enabled
        self.start = start
        self.last = last

    def __str__(self):
        return 'clock: %s, cron: %s, sound: %s, enabled: %s, start: %s, last: %s' % (self.name, self.cron, self.sound, self.enabled, self.start, self.last)

def clock_to_json(clock):
    return json.dumps(clock, default=lambda obj: obj.__dict__)

def dict_to_clock(d):
    return Clock(d['cron'], d['name'], d['sound'], d['enabled'],d['start'], d['last'])

def from_json_to_clock(str):
    return json.loads(str, object_hook=dict_to_clock)
