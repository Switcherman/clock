import subprocess

child1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

child2 = subprocess.Popen(['grep', 'test'], stdin=child1.stdout, stdout=subprocess.PIPE)

print(child2.stdout.read().decode('utf-8'))