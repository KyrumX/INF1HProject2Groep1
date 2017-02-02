import psycopg2
import random
import time
import pygame

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

def score(name, score, win, loss):
    connection = psycopg2.connect("dbname='project2' user='postgres' host='localhost' password='kaas123'")
    cursor = connection.cursor()
    cursor.execute("SELECT naamSpeler FROM score WHERE naamSpeler = '{}'".format(name))
    exists = cursor.fetchone()
    print(exists)
    if exists is None:
        cursor.execute("INSERT INTO score VALUES('{}',{},{},{})" . format(name, score, win, loss))
        connection.commit()
    else:
        x = cursor.execute("SELECT score FROM score WHERE naamSpeler = '{}'".format(name))
        cS = cursor.fetchall()
        y = cursor.execute("SELECT wins FROM score WHERE naamSpeler = '{}'".format(name))
        cW = cursor.fetchall()
        z = cursor.execute("SELECT losses FROM score WHERE naamSpeler = '{}'".format(name))
        cL = cursor.fetchall()
        connection.commit()
        cS2 = cS[0][0]
        cW2 = cW[0][0]
        cL2 = cL[0][0]
        nS = cS2 + score
        nW = cW2 + win
        nL = cL2 + loss
        cursor.execute("UPDATE score SET score='{}' WHERE naamSpeler = '{}'".format(nS, name))
        cursor.execute("UPDATE score SET wins ='{}' WHERE naamSpeler = '{}'".format(nW, name))
        cursor.execute("UPDATE score SET losses ='{}' WHERE naamSpeler = '{}'".format(nL, name))
        connection.commit()
    cursor.close()
    connection.close()

def highscoreRetrieve(screen):
    font = pygame.font.Font(None, 40)
    black = (0, 0, 0)
    white = (255, 255, 255)
    connection = psycopg2.connect("dbname='project2' user='postgres' host='localhost' password='kaas123'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM score ORDER BY score DESC LIMIT 10;")
    returns = cursor.fetchall()
    length = len(returns)
    print(length)
    x = 0
    y = 180
    for i in range(0, length):
        nameLabel = font.render(returns[x][0], True, white)
        screen.blit(nameLabel, (240, y))
        winLabel = font.render(str(returns[x][2]), True, white)
        screen.blit(winLabel, (615, y))
        loseLabel = font.render(str(returns[x][3]), True, white)
        screen.blit(loseLabel, (880, y))
        ratio = int((returns[x][2] / (returns[x][2] + returns[x][3])) * 100)
        ratioLabel = font.render(str(ratio) + "%", True, white)
        screen.blit(ratioLabel, (1150, y))
        scoreLabel = font.render(str(returns[x][1]), True, white)
        screen.blit(scoreLabel, (1420, y))
        x = x + 1
        y += 40



#highscore()
