import api_data
import dataBaseStuff


def report_results(data_to_write: list):
    with open("Output.txt", mode='a') as outputFile:  # open the output file for appending
        for show in data_to_write:
            print(show, file=outputFile)  # write each data item to file
            print("\n", file=outputFile)
            print("===================================================================", file=outputFile)


def main():
    connection, db_cursor = dataBaseStuff.open_db("project1db.sqlite")
    dataBaseStuff.create_top250_table(db_cursor)
    dataBaseStuff.create_top250_movies_table(db_cursor)
    dataBaseStuff.create_ratings_table(db_cursor)
    dataBaseStuff.create_mostPopular_TV_table(db_cursor)
    dataBaseStuff.create_UpDown_ranking_table(db_cursor)

    top_show_data = api_data.get_top_250_data()
    most_popular_TV_data = api_data.get_most_popular_TV_data()
    top250_movies_data = api_data.get_top250_movies()
    most_popular_movies_data = api_data.get_popular_movies()
    updown_ranking_data= api_data.get_UpDown_ranking_data()

    top_show_data_for_db = api_data.prepare_top_250_data(top_show_data)
    most_popularTV_data_for_db = api_data.prepare_most_popular_TV(most_popular_TV_data)
    top250_movies_data_for_db = api_data.prepare_top250_movies(top250_movies_data)
    most_popular_movies_data_for_db = api_data.prepare_most_popular_movies(most_popular_movies_data)
    updown_ranking_data_for_db = api_data.prepare_UpDown_ranking_data(updown_ranking_data)

    dataBaseStuff.put_top_250_in_database(top_show_data_for_db, db_cursor)
    dataBaseStuff.put_most_PopularTV_in_database(most_popularTV_data_for_db, db_cursor)
    dataBaseStuff.put_top_movies_in_database(top250_movies_data_for_db, db_cursor)
    dataBaseStuff.put_most_Popular_movies_in_database(most_popular_movies_data_for_db, db_cursor)
    dataBaseStuff.put_UpDown_ranking_in_database(updown_ranking_data_for_db, db_cursor)

    dataBaseStuff.put_in_wheel_of_time(db_cursor)
    ratings_data = api_data.get_ratings(top_show_data)
    db_ready_ratings_data = api_data.prepare_ratings_for_db(ratings_data)
    dataBaseStuff.put_ratings_into_db(db_ready_ratings_data, db_cursor)
    dataBaseStuff.close_db(connection)


if __name__ == '__main__':
    main()
