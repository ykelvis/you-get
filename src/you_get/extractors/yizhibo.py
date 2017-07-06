#!/usr/bin/env python

__all__ = ['yizhibo_download']

from ..common import *
import json
import time

def yizhibo_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    content = get_content(url)
    title = match1(content, r'<h1>.*：(.*)<\/h1>')
    if (title == ''):
        title = match1(content, r'nickname:\"(.*)\",')
    m3u8_url = match1(content, r'play_url:"(.*)",')
    m3u8 = get_content(m3u8_url)
    base_url = "/".join(m3u8_url.split("/")[:7])+"/"
    part_url = re.findall(r'([0-9]+\.ts)', m3u8)
    real_url = []
    for i in part_url:
        url = base_url + i
        real_url.append(url)
    print_info(site_info, title, 'ts', float('inf'))
    if not info_only:
        if player:
            launch_player(player, [m3u8_url])
        download_urls(real_url, title, 'ts', float('inf'), output_dir, merge = merge)

site_info = "yizhibo.com"
download = yizhibo_download
download_playlist = playlist_not_supported('yizhibo')
