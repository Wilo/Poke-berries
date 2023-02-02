# Table of Contents
1. [POKEAPI STATISTICS API](#pokeapi-statistics-api)
2. [API Instalation Instructions](/pokeapi/README.md)
3. [API Histogram Instructions](/graph/README.md)


# POKEAPI STATISTICS API

*Goal:*  Create a Poke-berries statistics API.


### General rules:

- Commit your changes to a public repository in GitHub.

- Add a README.md with instructions to run the code.


Support the following endpoints

```http
   GET /allBerryStats
```
```json
Response: {

    "berries_names": [...],

    "min_growth_time": "" // time, int

    "median_growth_time": "", // time, float

    "max_growth_time": "" // time, int

    "variance_growth_time": "" // time, float

    "mean_growth_time": "", // time, float

    "frequency_growth_time": "", // time, {growth_time: frequency, ...}

}
```


This endpoint should consume an external API to get the proper info, here

is the documentation page: https://pokeapi.co/docs/v2#berries

## TODO List.

- [X] The data must be human-readable.

- [X] Use environment variables for configuration.

- [X] The response must include the content-type header (application/json)

- [ ] Functions must be tested with pytest.


For extra points:

- [ ] Upload and deploy the solution to a free cloud service for example Heroku.

- [ ] Use a containering system like docker

- [X] Use a Python library (example: Matplotlib) to create a Histogram graph and display the image in a plain html. [Link](graph/README.md)

# Documentation Endpoint (Swagger)

```http
   http://localhost:8000
```
![Swagger Page](/assets/swagger.png "Swagger page")

# Get AllBerries Stats (API View and POSTMAN)

```http
   http://localhost:8000/api/allBerryStats/
```
#### Response json as Api View

![Api View Page](/assets/api-view.png "Api View page")

#### Response using Postman [Link to the collection](Postman%20Collection/PokeAPI%20Challenge.postman_collection.json)

![Postman](/assets/Postman.png "Postman")


# Histogram Berries stats.

![Histogram Stats Page](/assets/histogram.png "Histogram Stats Page")





## Authors

- [@Wilo](https://github.com/Wilo)