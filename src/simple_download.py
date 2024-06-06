#!/usr/bin/env python
import argparse
import spotipy
import spotify_dl
import subprocess
import os
import jellyfish


from spotipy.oauth2 import SpotifyClientCredentials

def gen_queries(track, artist):
    return [f'track:{track} artist:{artist}',
     f'{track}',
     f'{artist}',
     f'track:{track}',
     f'artist:{artist}']

def gen_tokenized_queries(track,artist):
    tokens = artist.split()
    result = []
    for token in tokens:
        result += gen_queries(track, token)
    result += gen_queries(track,artist)
    return result

def jaro_metric(lhs, rhs):
    return jellyfish.jaro_similarity(lhs,rhs) >= 0.9

def substr(lhs,rhs):
    return lhs in rhs or rhs in lhs

def get_most_matched(items, target_track, target_artist):
    tracks = items['tracks']['items']
    for track in tracks:
        artist = track['artists'][0]['name'].lower()
        track_name = track['name'].lower()
        target_artist = target_artist.lower()
        target_track = target_track.lower()

        metrics = [jaro_metric, substr]
        track_matched = any( metric(track_name, target_track) for metric in metrics)
        if track_matched:
            #for token in target_artist.split():
            #    artist_matched = any(metric(artist, target_artist) for metric in metrics)
            #    if artist_matched:
            link  = track['external_urls']['spotify']
            album_name = track['album']['name']
            return [album_name, link]
    return None

def simple_download():
    parser = argparse.ArgumentParser(prog='simple_download', description='simple download from spotify with title name and artist name.')
    parser.add_argument('--artist',  action='store',type=str,default='',help='artist name of the music to download')
    parser.add_argument('--title',  action='store',type=str,default='',help='title name of the music to download')

    args = parser.parse_args()


    client_id='b00a0d09652b4e1083850f6222ac8df3'
    client_secret='f1a5696d83554e27a280b1e09b1429ce'

    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        ),language='ko'
    )
    title = args.title
    artist = args.artist
    queries = gen_tokenized_queries(title, artist)
    for query in queries:
        items = sp.search(query, limit=20)
        res = get_most_matched(items, title,artist)
        if res is not None:
            break
    if res is None:
        raise Exception(f'cannot find track with {title} and {artist}')

    env = os.environ.copy()
    env['SPOTIPY_CLIENT_ID'] = f'{client_id}'
    env['SPOTIPY_CLIENT_SECRET']=f'{client_secret}'

    album_name = res[0]
    link = res[1]
    download_location = f'/music/{album_name}'
    cmd = ['spotify_dl']
    args = ['-l',f'{link}','-o', f'{download_location}']
    subprocess.run(cmd+args, env=env)


if __name__ == "__main__":
    simple_download()
