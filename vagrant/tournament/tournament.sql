-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

create database tournament;

\c tournament;

create table Players(
	ID serial primary key,
	Name text not null,
	Wins integer DEFAULT 0,
	Matches integer DEFAULT 0
);

create table Matches(
	Winner integer,
	Loser integer,
	PRIMARY KEY (Winner, Loser)
);