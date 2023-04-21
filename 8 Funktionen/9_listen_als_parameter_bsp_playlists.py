tracks = [
  {"band" : "Queen", "name" : "Another one bites the dust"},
  {"band" : "Aerosmith", "name" : "Crazy"},
  {"band" : "Ozzy Osbourne", "name" : "Crazy Train"},
  {"band" : "Queen", "name" : "We will rock you"},
]

def get_tracks_by_band(band_name, track_list):
  tracks_found = []

  for track in track_list:
    if track["band"] == band_name:
        tracks_found.append(track)

  return tracks_found 
my_tracks = get_tracks_by_band("Queen", tracks)
print(my_tracks)