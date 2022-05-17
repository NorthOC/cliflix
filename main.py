import src.tpb_scraper as scrape
import src.streamer as stream
import src.search_or_top as sot
import subprocess

# clear console
subprocess.run("clear")

query = sot.search_or_top()
# parse data from apibay as a dictionary
parsed_json = scrape.parse_me_matey(query)

# transform data from dictionary to array
parsed_array = scrape.info_to_arr(parsed_json)

# select a movie
info_hash = stream.select_movie(parsed_array)

# select a media player
selected_player = stream.select_player()

# stream how much you want :)
stream.stream_me_matey(info_hash, selected_player)
