#!/usr/bin/env python3
import logging

from gi.repository import Gst

from voctocore.lib.config import Config
from voctocore.lib.sources.avsource import AVSource


class GstAVSource(AVSource):
    def __init__(self, name, has_audio=True, has_video=True,
                 force_num_streams=None):
        super().__init__('GstAVSource', name, has_audio, has_video,
                         force_num_streams)

        self.name = name
        self.audio_source = Config.getGstAudioPipe(name)
        self.video_source = Config.getGstVideoPipe(name)
        self.build_pipeline()

    def num_connections(self):
        return 1

    def port(self):
        if self.internal_audio_channels():
            audio_hint=self.audio_source.split()[0]
        else:
            audio_hint="(None)"
        if self.has_video:
            video_hint=self.video_source.split()[0]
        else:
            video_hint="(None)"

        return f"(AV:{audio_hint}+{video_hint})"

    def __str__(self):
        return f'GSTSource[{self.name}] ({self.port()})'

    def build_audioport(self):
        return self.audio_source

    def build_videoport(self):
        return self.video_source
