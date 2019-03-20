import argparse
import yaml

from setupy.setupy import setupy

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--setting', dest='settings', nargs='*')
parser.add_argument('--include-setting', dest='literal_settings', nargs='*')

args = parser.parse_args()

# Depending on how the arguments are passed, there may
# be one or more blank settings in this list of literal
# settings.  Strip those out.
literal_settings = filter(lambda x: x.strip() != "", args.literal_settings)

print(setupy(settings=args.settings, literal_settings=literal_settings))
