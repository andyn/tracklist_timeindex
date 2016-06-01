#!/usr/bin/env python3
# -*- enconding: utf-8 -*-

import re
from sys import stdin


RE_MMSS = re.compile("^(.*)([0-9]+):([0-9]+)(.*)$")
RE_HHMMSS = re.compile("^(.*)([0-9]+):([0-9]+):([0-9]+)(.*)$")


def main(args):
    lines = stdin.readlines()
    stripped_lines = [l.strip('\r\n') for l in lines]
    parse_tracklist(lines)


def parse_tracklist(lines):
    total_seconds = 0
    for line in lines:
        mangled, total_seconds = parse_trackline(line, total_seconds)
        print(mangled)


def parse_trackline(line, seconds_before_this_line):
    found_hours = RE_HHMMSS.search(line)
    found_minutes = RE_MMSS.search(line)

    # Minute timestamp matches if hour matches
    if found_hours:
        before, hours, minutes, seconds, after = found_hours.groups()

    # Hours not matched -> try minutes
    elif found_minutes:
        before, minutes, seconds, after = found_minutes.groups()
        hours = 0

    # Minutes not matched -> return the line as is
    else:
        return line, seconds_before_this_line

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    seconds_after_this_line = (hours * 3600
                             + minutes * 60
                             + seconds
                             + seconds_before_this_line)
    ts_hours = seconds_before_this_line // 3600
    ts_minutes = (seconds_before_this_line - ts_hours * 3600) // 60
    ts_seconds = (seconds_before_this_line - ts_hours * 3600
                                           - ts_minutes * 60)

    if ts_hours > 0:
        timestamp = "{:d}:{:02d}:{:02d}".format(ts_hours, ts_minutes, ts_seconds)
    else:
        timestamp = "{:d}:{:02d}".format(ts_minutes, ts_seconds)

    return "".join([before, timestamp, after]), seconds_after_this_line


if __name__ == "__main__":
    from sys import argv
    main(argv)
