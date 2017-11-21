bind = '0.0.0.0:5000'
worders = (os.sysconf('SC_NPROCESSORS_ONLN') * 2) + 1
loglevel = 'error'
command = '/usr/local/lib/python2.7/dist-packages/gunicorn'
pythonpath = '/home/bezoar-developer-shantam/My-Projects/delbot'