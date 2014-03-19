""" 
Simple Python example showing how to parse JSON-formatted Twitter messages+metadata
(i.e. data produced by the Twitter status tracking API)

This script simply creates Python lists containing the messages, locations and timezones
of all tweets in a single JSON file.

Author: Geert Barentsen - 4 April (#dotastro)
"""

import sys
import simplejson
import difflib
import tweepy

# Input argument is the filename of the JSON ascii file from the Twitter API
filename = "json.txt"

tweets_text = [] # We will store the text of every tweet in this list
tweets_location = [] # Location of every tweet (free text field - not always accurate or given)
tweets_timezone = [] # Timezone name of every tweet

# Loop over all lines
f = file(filename, "r")
lines = f.readlines()



# Show result
print tweets_text
print tweets_location
print tweets_timezone