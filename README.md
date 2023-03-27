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

