#!/usr/bin/env python
"""A script to output the next event in an ics calendar to download.
"""
import os
import calendar
from icalevents.icalevents import events
import humanize


def events_from_urlfile(filename):
    'Read a list of urls from a file'
    event_list = []
    with open(filename) as urlfile:
        for url in urlfile:
            event_list += events(url.strip())
    return event_list


def pretty_formatting(event):
    """Represent the date in my own way.
    """
    raw_time = event.start.astimezone()
    week_day = calendar.day_name[raw_time.weekday()]
    month = calendar.month_name[raw_time.month]
    day = str(raw_time.day)
    hour = str(raw_time.hour)
    minute = str(raw_time.minute).zfill(2)
    time_left = '(' + humanize.naturaldelta(event.time_left()) + ')'
    return (f'{week_day}, {month} {day}, {hour}:{minute} -',
            f'{event.summary}', time_left)


if __name__ == '__main__':
    DIR_CONFIG = os.environ['XDG_CONFIG_HOME']
    EVENTS = events_from_urlfile(DIR_CONFIG + '/calendarlist')
    print(*pretty_formatting(sorted(EVENTS)[0]))
