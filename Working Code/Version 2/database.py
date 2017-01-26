import psycopg2
import random

# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname='project2' user='postgres' host='localhost' password='kaas123'")
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
    results = results[0][0]
    return results


# Uploads a score into the hiscore table
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
        print("Je bent ingelogd!")


def interact_with_database2(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=sjors user=sjors")
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

    # !/usr/bin/python
    # import the desired package



def get_questions(questionCat):
    # Open database connection
    db = psycopg2.connect("dbname='project2' user='postgres' host='localhost' password='kaas123'")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    gesloten = "MC"
    cursor.execute("SELECT Question_ID FROM qna WHERE question_catagory = '{}' AND question_type = '{}'" .format(questionCat, gesloten))


    # OR use fetchall() method to fetch multiple rows and store the result in a list variable.
    data = cursor.fetchall()

    return data

    # disconnect from server
    db.close()


def get_questions2(questionCat):
    # Open database connection
    db = psycopg2.connect("dbname='project2' user='postgres' host='localhost' password='kaas123'")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    open = "OPEN"
    cursor.execute("SELECT Question_ID FROM qna WHERE question_catagory = '{}' AND question_type = '{}'" .format(questionCat, open))


    # OR use fetchall() method to fetch multiple rows and store the result in a list variable.
    data = cursor.fetchall()

    return data

    # disconnect from server
    db.close()


