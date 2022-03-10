from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selection_sort import selection_sort
load_dotenv()

spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())



# sort by release_date or name, duration_ms,popularity,explicit


def fetch_data(search_term):
    """Api request to fetch music"""
    results = spotify_client.search(q=search_term, limit=2)
    return transform_response(results["tracks"]["items"])


def transform_response(response):
  """Transform api response to our need"""
  prettified = map(lambda item : {
    "release_data":item["album"]["release_date"],"duration_ms":item["duration_ms"],
    "explicit":item["explicit"],"name":item["name"],"popularity":item["popularity"]
  },response)
  return list(prettified)




def main():
  """main application entry"""
  search_more = True
  while search_more:
    try:
      search_input = input("Music search\n=====\n\nPlease choose any of the options below\n\n1.Make search\n2.Quit app.\n\n")

      if int(search_input) == 2:
        search_more = False
      elif int(search_input )== 1:
        search_term = (input("\nPlease enter name of artist\n")).strip()
        data  = fetch_data(search_term)
        print(data)
      else:
        continue
    except KeyboardInterrupt:
      search_more = False
      print("Thank you for the trying the app out.")
    except Exception as error:
      print(error)
      search_more = False
      return None




if __name__ == "__main__":
  print(main())