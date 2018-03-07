python_library(
  name='nomnom-lib',
  dependencies=[
    '3rdparty/python:flask',
    '3rdparty/python:pyyaml',
  ],
  sources=globs('*.py'),
)

python_binary(
  name='nomnom-app',
  dependencies=[':nomnom-lib'],
  entry_point='nomnom.app',
)
