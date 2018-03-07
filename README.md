# nomnom

a tool for randomly grouping participants

## Development

To set up your developent environment, create a virtual environment for NomNom.  From the nomnom directory,

```
mkvirtualenv -a . -r 3rdparty/python/requirements.txt nomnom
```

Once you have done this, you can work on NomNom with the command

```
workon nomnom
```

which will put you in the virtual environment and bring you back to this directory.

To run the NomNom app in development mode,

```
env FLASK_DEBUG=1 FLASK_APP=src/python/nomnom/app.py flask run
```
