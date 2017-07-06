#!/usr/bin/env python

__all__ = ['meipai_download']

from ..common import *
import json
import time

def meipai_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'}
    content = get_content(url, headers=headers)
    title = match1(content, r'<meta content="(.*)" property="og:title">')
    if (title == ''):
        title = match1(content, r'<meta content="(.*)" property="og:og:description">')
    vid_url = [match1(content, r'style="display: block;" src="(.*)"><\/video>')]
    print_info(site_info, title, 'ts', float('inf'))
    if not info_only:
        if player:
            launch_player(player, [m3u8_url])
        download_urls(vid_url, title, 'ts', float('inf'), output_dir, merge = merge)

site_info = "meipai.com"
download = meipai_download
download_playlist = playlist_not_supported('meipai')

