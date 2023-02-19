# Web Scraping to information for Pokedex

## Steps to Run
1. run `python step1_scrape_for_all_pokemon_skeleton.py` to extract name and id of all pokemon from [pokemondb.net](https://pokemondb.net/pokedex/all). The data is extracted to `all_pokemon_stage1.json`.
```typescript
    {
        ['id-of-pokemon-1']: {
            id: string,
            tinyImageURL: string,
            name: string,
        },
        ['id-of-pokemon-2']: {...},
        ...
        ['id-of-pokemon-n']: {...},
    }
```
2. run `python step2_get_pokemon_detailed_info.py` to extract the rest of the information needed about each pokemon. The data is extracted to `all_pokemon_stage2.json`
```typescript
    {
        ['id-of-pokemon-1']: {
            id: string,
            name: string,
            tinyImageURL: string,
            imageUrl: string,
            type: string,
            species: string,
            height: string,
            weight: string,
            catchRate: string,
            baseExperience: string,
            growthRate: string,
            hp: string,
            attack: string,
            defense: string,
            specialAttack: string,
            specialDefense: string,
            speed: string,
            total: string,
            evolutions: string,
        },
        ['id-of-pokemon-2']: {...},
        ...
        ['id-of-pokemon-n']: {...},
    }
```
3. run `python step3_get_pokemon_description.py` to extract pokemon description from the [official pokedex](https://www.pokemon.com/us/pokedex). The data is extracted to `all_pokemon_stage3.json`
```typescript
    {
        ['id-of-pokemon-1']: {
            ...
            descriptions: string[],
        },
        ['id-of-pokemon-2']: {...},
        ...
        ['id-of-pokemon-n']: {...},
    }
```
4. run `step4_smooth_pokemon_data.py` to smooth the pokemon data. The data is extracted to `all_pokemon_stage4.json`
```typescript
    {
        ['id-of-pokemon-1']: {
            id: string,
            name: string,
            tinyImageURL: string,
            imageUrl: string,
            type: string,
            species: string,
            catchRate: number,
            baseExperience: number,
            growthRate: string,
            hp: number,
            attack: number,
            defense: number,
            specialAttack: number,
            specialDefense: number,
            speed: number,
            evolutions: string,
            descriptions: string,
            weightKg: number,
            heightM: number,
            baseStatTotal: string
        },
        ['id-of-pokemon-2']: {...},
        ...
        ['id-of-pokemon-n']: {...},
    }
```

if there's problems with importing
- run `source scraper-env/bin/activate` to activate the virtual environment
- install requests, `pip3 install requests`
- install BeautifulSoup 4, `pip3 install bs4`

run `deactivate` to exit the python virtual environment