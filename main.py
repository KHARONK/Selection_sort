from dotenv import load_dotenv
from pprint import pformat
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from selection_sort import selection_sort
load_dotenv()
spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# sort by release_date or name, duration_ms,popularity,explicit

TEMP_DB = {}

def fetch_data(search_term):
    """Api request to fetch music"""
    # limitations to music search
    results = spotify_client.search(q=search_term, limit=3)
    return transform_response(results["tracks"]["items"])


def transform_response(response):
    """Transform api response to our need"""
    prettified = map(lambda item: {
      "release_date": item["album"]["release_date"], "duration_ms": item["duration_ms"],
      "explicit": item["explicit"], "name": item["name"], "popularity": item["popularity"]
    }, response)
    return list(prettified)

def main():
    # Documentation
    """main application entry"""
    data = None
    sorted = None
    search_more = True
    while search_more:
      try:
        search_input = input(
          "Music search\n=====\n\nPlease choose any of the options below\n\n1.Make search\n2.Quit app.\n\n")
        # If User decides to quit then no search
        if int(search_input) == 2:
          search_more = False
          # If User decide to search then data will be fetched
        elif int(search_input) == 1:
          search_term = (input("\nPlease enter name of artist\n")).strip()
          if TEMP_DB.get(search_term) is not None:
            data = TEMP_DB[search_term]
          else:
              #If data not in dictionary search from API
            data = fetch_data(search_term)
            TEMP_DB[search_term] = data
          print("\n\n")
         #Option to sort data
          search_input = (input("\nDo you want to sort your data\n1.Yes\n2.No\n")).strip()
        #If not the print unsorted data
          if int(search_input) == 2:
            print("\n")
            print("Unsorted data\n\n {}".format(data))
          else:
            sort_key = (input(
              "\nChoose how you want to sort\n\n1.Release date\n2.Duration\n3.name\n4.popularity\n5.Explicit\n\n")).strip()
            #Sorting conditions for User
            if int(sort_key) == 1:
              sorted = selection_sort(data, "release_date")
            elif int(sort_key) == 2:
              sorted = selection_sort(data, "duration_ms")
            elif int(sort_key) == 3:
              sorted = selection_sort(data, "name")
            elif int(sort_key) == 4:
              sorted = selection_sort(data, "popularity")
            elif int(sort_key) == 5:
              sorted = selection_sort(data, "explicit")
            else:
              print("no or wrong key entered. Data wont be sorted\n")
            if sorted is not None:
              print(pformat(sorted))
            else:
              print(pformat(data))

        else:
          continue
          # Control C to quit
      except KeyboardInterrupt:
        search_more = False
        print("Thank you for the trying the app out.")
      except Exception as error:
        print(error)
        search_more = False
        return None



if __name__ == "__main__":
   print(main())