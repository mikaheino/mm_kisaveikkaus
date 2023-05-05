CREATE SCHEMA MM_KISAVEIKKAUS ; 

CREATE OR REPLACE TABLE MM_KISAVEIKKAUS.MM_KISAVEIKKAUS_SCHEDULE (
  id integer NOT NULL,
  match_day date NOT NULL,
  match varchar(40) NOT NULL,
  home_team_goals integer,
  away_team_goals integer
); 

CREATE OR REPLACE TABLE MM_KISAVEIKKAUS._MM_KISAVEIKKAUS (
  id integer NOT NULL,
  match_day date NOT NULL,
  match varchar(40) NOT NULL,
  home_team_goals integer,
  away_team_goals integer
); 
