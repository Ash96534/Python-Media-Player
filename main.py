#!/usr/bin/env python3
"""Python Media Player - Local desktop media player with torrent streaming support."""

import vlc
import libtorrent as lt
import time


class MediaPlayer:
    def __init__(self):
        self.player = vlc.MediaPlayer()
        self.session = lt.session()

    def play_local(self, path):
        self.player.set_media(path)
        self.player.play()

    def stream_torrent(self, magnet_link):
        params = {
            "save_path": "./downloads",
            "storage_mode": lt.storage_mode_t.storage_mode_sparse,
        }
        handle = lt.add_magnet_uri(self.session, magnet_link, params)
        self.session.start_download()

        while not handle.is_seed():
            s = handle.status()
            print(f"Progress: {s.progress * 100:.2f}%")
            time.sleep(1)

        print("Download complete!")


if __name__ == "__main__":
    player = MediaPlayer()
    # Example usage
    # player.play_local("video.mp4")
