# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
from collections import defaultdict


def get_autocomplete_handler(engine='PrefixMap'):
    if engine == 'PrefixMap':
        return PrefixMap()
    return Brute()


def santitize(addr_str):
    # https://github.com/moskytw/zipcodetw/blob/dev/zipcodetw/util.py
    pass


class Brute:
    def __init__(self):
        self.roads = []
        with io.open('twaddr/data/roads.txt', 'rt') as f:
            for line in f:
                self.roads.append(line.replace('\n', ''))

    def query(self, prefix_str, limit=10):
        matched = []
        for road in self.roads:
            if road.startswith(prefix_str):
                matched.append(road)
            if len(matched) >= limit:
                return matched
        return matched


class PrefixMap:
    def __init__(self):
        self.prefix_map = defaultdict(list)
        with io.open('twaddr/data/roads.txt', 'rt') as f:
            for line in f:
                self.prefix_map[line[0]].append(line.replace('\n', ''))

    def query(self, prefix_str, limit=10):
        return [road for road in self.prefix_map[prefix_str[0]] if road.startswith(prefix_str)][:10]
