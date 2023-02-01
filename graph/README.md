
# Poke Api Statistics API Histogram

This is a script who makes a histogram with the result of our API Endpoint `allBerryStats`.


## API Reference

#### Get all items

```http
  GET /api/allBerryStats
```

#### Response
```json
{
  "berries_names": [
    "cheri",
    "chesto",
    "pecha",
    "rawst",
    "aspear",
    "starf",
    "enigma",
    "micle",
    "custap",
    "jaboca",
    "rowap"
  ],
  "min_growth_time": 2,
  "median_growth_time": 12.859375,
  "max_growth_time": 24,
  "variance_growth_time": 61.495849609375,
  "mean_growth_time": 12.859375,
  "frequency_growth_time": {
    "2": 5,
    "3": 5,
    "4": 3,
    "5": 5,
    "6": 4,
    "8": 7,
    "12": 1,
    "15": 5,
    "18": 17,
    "24": 12
  }
}
```


## Demo

1. Make a `virtual environment` with the following command.
    
    > `python -m venv env`

2. Activate our `env` using `source env/bin/activate`.
3. Install the requirements `pip install -r requirements.txt`
4. run script code `python graph.py`.
5. open `index.html` a see the histogram.

> *Note:*
> You must replace the API endpoint `http://localhost:8000/api/allBerryStats/` for your own domain or make you sure the local server is running.

## Authors

- [@Wilo](https://github.com/Wilo)


## License

[MIT](https://choosealicense.com/licenses/mit/)

