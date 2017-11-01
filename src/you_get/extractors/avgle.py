#!/usr/bin/env python

__all__ = ['avgle_download']

from ..common import *
import json
import time

def avgle_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    url = url + rstrip("/") + "/"
    content = get_content(url, headers=fake_headers)
    title = match1(content, r'<meta property="og:title" content="([^"]+)"')
    if (title == ''):
        title = match1(content, r'<meta property="og:description" content="([^"]+)"')
    m3u8_url = match1(content, r'<source src="([^"].*)"')
    m3u8 = get_content(m3u8_url, headers=fake_headers)
    video_id = match1(url, r'\/(\d+)\/')
    title = video_id + "-" + title
    video_url = re.findall(r'http.*', m3u8)
    print_info(site_info, title, 'ts', float('inf'))
    if not info_only:
        if player:
            launch_player(player, [m3u8_url])
        download_urls(video_url, title, 'ts', float('inf'), output_dir, merge=merge)

site_info = "avgle.com"
download = avgle_download
download_playlist = playlist_not_supported('avgle')

