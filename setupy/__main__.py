import argparse
import yaml

from setupy.setupy import setupy

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--setting', dest='settings', nargs='*')

args = parser.parse_args()

settings = [yaml.load(s) for s in args.settings]

print(setupy(settings=settings))
