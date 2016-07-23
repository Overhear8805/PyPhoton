# PyPhoton
A simple backend for Photon, built with Django. Images are stored as plain files and metadata is stored in a bundled SQLite database. 

## Run locally on Linux
PyPhoton comes with everything that is needed to run it. If you wish to run PyPhoton in a more stable environment, checkout the [installation instructions](#Installation-(Apache-with-WSGI)). 

1. Make sure that Python 3 and pip is installed.
2. `git clone https://github.com/simon1573/PyPhoton.git && cd PyPhoton`
3. In `PyPhoton/photon/views.py`, edit `MEDIA_DIR` to your prefrerred directory. (TODO: Move this setting to `mysite/settings.py`)
4. `sudo pip install -r requrements.txt`
5. `python manage.py makemigrations photon`
6. `python manage.py migrate photon`
7. Finally, to start the server and make it listen to all interfaces at port 4123: `python manage.py runserver 0.0.0.0:4123`
8. ~~Download the Android application and follow the setup instructions.~~

## Installation (Apache with WSGI)
todo
