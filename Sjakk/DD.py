def show_movies(db):
    for key in db:
        info = db[key]
        if len(key) > 20:
            title = key[:21]
        else:
            title = key
        year = str(info[0])
        genre = info[1]
        if len(genre) > 10:
            genre = genre[:11]
        age = str(info[2])
        country = info[3]
        if len(country) > 15:
            country = country[:16]
        score = str(info[4]) + "%"
        print(year.ljust(0) + title.ljust(5) + genre.ljust(46) + country.ljust(57) + "Age:".rjust(16)+ age.rjust(12)+ "Score:".rjust(5)+ score.rjust(0))


db={"Ostepop":(2007,'Sci-Fi',2,"Norway",100,"Doodle your way into chilness")}

show_movies(db)