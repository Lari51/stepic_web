# gunicorn configuration file
# gunicorn -b 0.0.0.0:8080 --workers 5 hello:app $
CONFIG = {
  'mode': 'wsgi',
  'working_dir': '/home/box/web',
 # 'pythonpath'= '/home/box/web'
  'python': '/usr/bin/python3',
  'args': (
    '--bind=0.0.0.0:8080',
    '--workers=2',
    '--timeout=15',
    '--log-level=debug',
    'hello:app'
  )
}
