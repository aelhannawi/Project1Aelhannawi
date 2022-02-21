import api_data


def test_gettop250():
    top250_results = api_data.get_top_250_data()
    assert len(top250_results) == 250
def test_getMostPopular():
    mostPopular_results = api_data.get_most_popular_data()
    assert len(mostPopular_results) ==250

def test_getMostPopular_movies():
        mostPopular_movies_results = api_data.get_popular_movies()
        assert len(mostPopular_movies_results) == 250

def test_getTop250_movies():
     top250_movies_results = api_data.get_top250_movies()
     assert len(top250_movies_results) == 250
