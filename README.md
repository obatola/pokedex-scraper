# Web Scraping to information for Pokedex

## Steps to Run
1. run `python step1_scrape_for_all_pokemon_skeleton.py` to extract name and id of all pokemon from [pokemondb.net](https://pokemondb.net/pokedex/all). The data is extracted to `all_pokemon_stage1.json`.
```
    {
        [id-of-pokemon-1]: {
            [id]: string,
            [tinyImageURL]: string,
            [name]: string,
        },
        [id-of-pokemon-2]: {...},
        ...
        [id-of-pokemon-n]: {...},
    }
```
2. run `python step2_get_pokemon_detailed_info.py` to extract the rest of the information needed about each pokemon. The data is extracted to `all_pokemon_stage2.json`
3. run `python step3_get_pokemon_description.py` to extract pokemon description from the [official pokedex](https://www.pokemon.com/us/pokedex). The data is extracted to `all_pokemon_stage3.json`
4. run `step4_smooth_pokemon_data.py` to smooth the pokemon data. The data is extracted to `all_pokemon_stage4.json`