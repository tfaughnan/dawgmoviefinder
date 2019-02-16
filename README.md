Dawg Movie Finder
===
A simple GroupMe bot for movie lovers.

What does it do?
---
*Dawg Movie Finder* supplies basic info about movies when called in a GroupMe group. There are currently two commands:
* ``!movie [title]`` returns info such as full title, year, synopsis, and IMDb link for a given search query "\[title]"
* ``!about`` returns a brief message of your choice. I recommend setting this to a description of this bot and its commands.

Its name comes from the blessed men and brothers of Alumni Hall, aka the dawgs, and our weekly movie nights. ΔΩΓ.

How do I use it?
---
1. Create an account with [The Movie Database](https://www.themoviedb.org/account/signup) and generate a TMDb API key.
2. Log in and register a new app on the [GroupMe website](https://dev.groupme.com/) and find your GroupMe API key, bot ID, and group ID.
3. Create a **config.py** file to store these four pieces of information, and add a personal message for the ``!about`` command. See [config.py.example](https://github.com/tfaughnan/dawgmoviefinder/blob/master/config.py.example) for specifics.
4. Run [dawgmoviefinder.py](https://github.com/tfaughnan/dawgmoviefinder/blob/master/dawgmoviefinder.py) with your new config.py file.
5. Interact with *Dawg Movie Finder* in your GroupMe group!
