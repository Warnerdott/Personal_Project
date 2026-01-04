import pandas as pd 
from fn import get_req, save_anime_tbl, save_genres_tbl
import os

url = "https://api.jikan.moe/v4/top/anime"
file_path = 'raw_storage'
raw_json = 'top_anime.json'
anime_tbl = 'tbl_main.csv'
genres_tbl = 'tbl_genres.csv'

os.makedirs(file_path, exist_ok=True)

json_path = os.path.join(file_path, raw_json)
anime_tbl_path = os.path.join(file_path, anime_tbl)
genres_tbl_path = os.path.join(file_path, genres_tbl)

get_req(url, json_path)
save_anime_tbl(json_path, anime_tbl_path)
save_genres_tbl(json_path, genres_tbl_path)

