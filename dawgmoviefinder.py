import time
import requests
from config import *


# checks most recent message in GroupMe group for command
def read_messages():
    group_messages = requests.get('https://api.groupme.com/v3/groups/{0}/messages?token={1}'.format(GROUP_ID, GM_KEY)).json()
    last_message = group_messages['response']['messages'][0]['text']
    if last_message[0:6].lower() == '!movie':
        send_message(search(last_message[7:]))
    if last_message[0:6].lower() == '!about':
        send_message(ABOUT)


# bot sends a message to GroupMe group
def send_message(message):
    post_body = {"bot_id": BOT_ID,
                 "text": message}
    r = requests.post('https://api.groupme.com/v3/bots/post', post_body)
    return r


# searches for user's requested movie on TMDb
def search(query):
    query = query.strip()
    if query[:-5:-1].isdigit():
        results = requests.get('https://api.themoviedb.org/3/search/movie?api_key={0}&query={1}&primary_release_year={2}'.format(TMDB_KEY, query[:-5], query[:-5:-1][::-1])).json()['results']
    else:
        results = requests.get('https://api.themoviedb.org/3/search/movie?api_key={0}&query={1}'.format(TMDB_KEY, query)).json()['results']

    if not results:
        return 'No movie found called \"{0}\"'.format(query)

    tmdb_id = str(results[0]['id'])
    movie = requests.get('https://api.themoviedb.org/3/movie/{0}?api_key={1}&append_to_response=credits,videos'.format(tmdb_id, TMDB_KEY)).json()

    title = movie['title']
    year = movie['release_date'][0:4]

    for person in movie['credits']['crew']:
        if person['job'] == 'Director':
            director = person['name']
            break

    actor0 = movie['credits']['cast'][0]['name']
    actor1 = movie['credits']['cast'][1]['name']

    overview = movie['overview']
    imdb_url = 'https://www.imdb.com/title/{0}'.format(movie['imdb_id'])

    if not movie['videos']['results']:
        trailer_url = ''
    else:
        trailer_url = '\nhttps://youtube.com/watch?v={0}'.format(movie['videos']['results'][0]['key'])
        for video in movie['videos']['results']:
            if video['type'] == 'Trailer':
                trailer_url = '\nhttps://youtube.com/watch?v={0}'.format(video['key'])
                break

    return '{0} ({1})\ndir. {2}\nstarring {3}, {4}\n-----\n\"{5}\"\n-----\n{6}{7}'.format(title, year, director, actor0, actor1, overview, imdb_url, trailer_url)


# ================================================

while True:
    read_messages()
    time.sleep(1)
