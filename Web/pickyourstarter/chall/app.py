from flask import Flask, render_template, render_template_string

app = Flask(__name__)
app.static_folder = 'static'

starter_pokemon = {
    "charmander" : {
        "name": "Charmander",
        "type": "Fire",
        "abilities": ["Blaze", "Solar Power"],
        "height": "0.6m",
        "weight": "8.5 kg",
        "description": "Charmander is a Fire-type Pokémon known for its burning tail flame.",
        "picture": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png"
    },
    "bulbasaur" : {
        "name": "Bulbasaur",
        "type": "Grass/Poison",
        "abilities": ["Overgrow", "Chlorophyll"],
        "height": "0.7m",
        "weight": "6.9 kg",
        "description": "Bulbasaur is a dual-type Grass/Poison Pokémon known for the plant bulb on its back.",
        "picture": "https://archives.bulbagarden.net/media/upload/f/fb/0001Bulbasaur.png"
    },
    "squirtle" : {
        "name": "Squirtle",
        "type": "Water",
        "abilities": ["Torrent", "Rain Dish"],
        "height": "0.5m",
        "weight": "9.0 kg",
        "description": "Squirtle is a Water-type Pokémon known for its water cannons on its back.",
        "picture": "https://static.pokemonpets.com/images/monsters-images-800-800/7-Squirtle.webp"
    },
}

def blacklist(string):
    block = ["config", "update", "builtins", "\"", "'", "`", "|", " ", "[", "]", "+", "-"]
    
    for item in block:
        if item in string:
            return True
    return False


@app.route('/')
def index():
    render = render_template('index.html')
    return render_template_string(render)


@app.route('/<pokemon>')
def detail(pokemon):
    pokemon = pokemon.lower()
    try:
        render = render_template('pokemon_name.html', data=starter_pokemon[pokemon])
        return render_template_string(render)
    except:
        if blacklist(pokemon):
            return render_template('error.html')
            
        render = render_template('404.html', pokemon=pokemon)
        return render_template_string(render)

if __name__ == '__main__':
    app.run(debug=True)
