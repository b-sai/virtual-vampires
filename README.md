# virtual-vampires
duolingo, but much worse 

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# Backend running instructions

install: 

`pip install -r requirements.txt`

setup: 

`python manage.py migrate`
`python manage.py makemigrations`


run: 

`python manage.py runserver`

### Testing
To run tests for sentence generators, run `python -m  backend_scripts.test_converters.test_all` from the root directory. To run tests for a specific language, run `python -m unittest backend_scripts.test_converters.test_english` (for example).

#### Django APIs:

- `rand_elem/` - returns a random `{'en': 'jump', 'sp': 'saltar'}`

- `en_sent/` - returns a random english sentence that is grammatically right and is generated using features: `{'en': I do believe}`

- `en_es_verbs/` - API1: Provide a sentence with a verb in its present tense. Provides a verb that is correct and a list of incorrect verbs. 
```
{
'sentence': 'he ____',
'verb': 'jump',
'correct': 'jumped' ,
'wrong': ['will run', 'eats', 'laughs']
}
```

- `en_es_sent/` - API2: Provide a random sentence with a list of its correct spanish translation. `{"en": "I will jump", "sp": ["yo", "voluntad", "saltar"]}`

- swahili versions of the previous apis - `rand_swa_elem/`, `en_swa_sent/`, `en_swa_verbs/`
