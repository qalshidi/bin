#!/usr/bin/env python
"""A script to output the next event in an ics calendar to download.
"""
import os
from icalevents.icalevents import events


def events_from_urlfile(filename):
    'Read a list of urls from a file'
    event_list = []
    with open(filename) as urlfile:
        for url in urlfile:
            event_list += events(url.strip())
    return event_list


if __name__ == '__main__':
    DIR_CONFIG = os.environ['XDG_CONFIG_HOME']
    EVENTS = events_from_urlfile(DIR_CONFIG + '/calendarlist')
    print(sorted(EVENTS)[0])
