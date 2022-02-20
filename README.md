## IL ASSIGNMENT SOLUTION

# Steps to run

* Clone this repository
* Create a virtual environment
* Install requirements
* Run django server and the api is excessible at `/filter-api/`
* For tests: `python manage.py test`

# Examples:

* `localhost/filter-api/?search_phrase=(date eq 2016-05-01) AND ((distance 
gt 20) OR (distance lt 10))`
* `localhost/filter-api/?search_phrase=distance lt 10`

# Main Source Files

* `parse_search_phrase` function is at `main/helpers.py` 
* Filter API is at `main/views.py`
