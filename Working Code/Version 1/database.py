import psycopg2
# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname='ijiivzmk' user='ijiivzmk' host='horton.elephantsql.com' password='3kI0M6nYddinHSJL_ZlzzidbKFMTJwkO' port=5432")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()
    return results


# Uploads a score into the highscore table
def upload_score(name, score):
    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                           .format(score, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY score")[0][1]
    return result

def login():
    usr = input('Voer je gebruikersnaam in') # momenteel via console
    pw = input('Voer je wachtwoord in')

    find = interact_with_database("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(usr, pw))

    if interact_with_database("SELECT * FROM users WHERE username = '{}'".format(usr)) == []:
        print("De ingevoerde gebruikersnaam bestaat niet")
    elif interact_with_database("SELECT * FROM users WHERE username = '{}'".format(usr)) != [] and find == []:
        print("De ingevoerde wachtwoord is verkeerd")
    else:
        print("U bent ingelogd")

