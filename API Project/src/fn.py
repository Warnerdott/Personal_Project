import requests
import json
import pandas as pd

def get_req(url, json_path):

    response = requests.get(url)
    data = response.json()

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)

    print(f"Download successfully - {json_path}")

def save_anime_tbl(json_path, anime_tbl_path):

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.json_normalize(data["data"], sep="_")

    need_columns = ['rank','title', 'title_english', 'title_japanese', 'type', 'favorites',
                    'source', 'episodes', 'status', 'duration', 'synopsis', 'members',
                    'score', 'scored_by', 'popularity', 'year', 'rating', 'genres']
    df = df[need_columns]

    df["genres"] = df["genres"].apply(
        lambda x: " ".join(str(g["mal_id"]) for g in x) if isinstance(x, list) else ""
    )

    df.to_csv(anime_tbl_path, index=False, encoding="utf-8-sig")

    print(fr'tbl_main saved at {anime_tbl_path}')

def save_genres_tbl(json_path, genres_tbl_path):

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    genres_list = []

    for anime in data["data"]:
        for genre in anime.get("genres", []):
            genres_list.append({
                "mal_id": genre.get("mal_id", ""),
                "type": genre.get("type", ""),
                "name": genre.get("name", "")
            })

    df_genres = pd.DataFrame(genres_list)
    df_genres = df_genres.drop_duplicates().reset_index(drop=True)
    df_genres.to_csv(genres_tbl_path, index=False, encoding="utf-8-sig")

    print(f"tbl_genres saved at {genres_tbl_path}")