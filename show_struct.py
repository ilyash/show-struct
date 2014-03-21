#!/usr/bin/env python
# vim: ts=4 sw=4 et

import argparse
import collections
import json
import sys

class Outliner(object):

    def __init__(self):
        self.paths = {}
        self.values_for_path = collections.defaultdict(dict)

    def _outline(self, data, path):
        p = ''.join(path)
        self.paths[p] = True
        if isinstance(data, dict):
            if not data:
                self.values_for_path[p]['(Empty hash)'] = True
            for k, v in data.iteritems():
                self._outline(v, path + ['.' + k])
            return
        if isinstance(data, list):
            for v in data:
                self._outline(v, path + ['[]'])
            self.values_for_path[p]['(Array of {0} elements)'.format(len(data))] = True
            return
        # scalar assumed
        self.values_for_path[p][data] = True

    def outline(self, data):
        self._outline(data, [])
        del self.paths['']

        ret = []
        for path in sorted(self.paths):
            ret.append({
                'path': path,
                'values': sorted(self.values_for_path[path].keys())
            })
        return ret


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Show structure of give JSON file')
    parser.add_argument('file', metavar='FILE',help="The filename to read. Use '-' to read stdin")
    args = parser.parse_args()

    if args.file == "-":
        data = json.loads(sys.stdin.read())
    else:
        with open(args.file) as f:
            data = json.loads(f.read())

    outline = Outliner().outline(data)
    for path in outline:
        l = len(path['values'])
        if l == 0:
            print(path['path'])
            continue
        if l == 1:
            print("{0} -- {1}".format(path['path'], path['values'][0]))
            continue
        print("{0} -- {1} .. {2} ({3} unique values)".format(path['path'], path['values'][0], path['values'][-1], l))
