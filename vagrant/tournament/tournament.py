#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

# make sure queries are returning things
# make sure python variables are inserted outside the query
# figure out how to execute two queries
# incorporate matches table


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        UPDATE Players
        SET Wins = 0, Matches = 0
        ''')
    c.execute('''
        DELETE FROM Matches
        ''')
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        DELETE FROM Players
        ''')
    c.execute('''
        DELETE FROM Matches
        ''')
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        SELECT count(*) from Players
        ''')
    count = c.fetchall()
    DB.close()
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        INSERT INTO Players(Name)
        VALUES(%s)''',  (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
        or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        SELECT *
        FROM Players
        ORDER BY wins DESC
        ''')
    rankings = c.fetchall()
    DB.close()
    return rankings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute('''
        UPDATE Players
        SET Wins = Wins+1, Matches = Matches+1
        WHERE ID = %s''' % (winner,))
    c.execute('''
        UPDATE Players
        SET Matches = Matches+1
        WHERE ID = %s''' % (loser,))
    c.execute('''
        INSERT INTO Matches
        VALUES(%s, %s)''', (winner, loser,))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    count = countPlayers()
    standings = playerStandings()
    i = 0
    n = 0
    upNext = []
    while i < count:
        pair = (standings[i][n], standings[i][n+1], standings[i+1][n], standings[i+1][n+1])
        upNext.append(pair)
        i += 2
    DB.close()
    return upNext



