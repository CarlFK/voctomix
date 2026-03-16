#!/usr/bin/env python3
import logging

from configparser import NoOptionError
from gi.repository import Gst

from voctocore.lib.config import Config
from voctocore.lib.sources.avsource import AVSource


class TestSource(AVSource):
    def __init__(self, name, has_audio=True, has_video=True,
                 force_num_streams=None):
        super().__init__('TestSource', name, has_audio, has_video,
                         force_num_streams)

        self.name = name
        self.video_source = Config.getGstVideoPipe(name)
        self.audio_source = Config.getGstAudioPipe(name)
        self.build_pipeline()

    def port(self):
        return "GST AV"

    def num_connections(self):
        return 1

    def __str__(self):
        return 'GstSource[{name}]'.format(
            name=self.name,
        )

    def build_audioport(self):
        return """{audio_source}
                      name=gstaudiosrc-{name}
                      """.format(
            audio_source=self.audio_source,
            name=self.name,
        )

    def build_videoport(self):

        return """{video_source}
                      name=gstvideosrc-{name}
                ! queue max-size-time=4000000000
                ! videoconvert
                ! videorate
                ! videoscale
                ! queue max-size-time=4000000000
                      """.format(
            video_source=self.video_source,
            name=self.name,
        )
 
