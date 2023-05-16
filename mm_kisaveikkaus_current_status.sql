CREATE OR REPLACE VIEW MM_KISAVEIKKAUS.MM_KISAVEIKKAUS_CURRENT_STATUS (player, points) AS 

SELECT 'Mika', points FROM MM_KISAVEIKKAUS.MIKAHEINO_MM_KISAVEIKKAUS_V 
UNION
SELECT 'Aleksi', points FROM MM_KISAVEIKKAUS.ALEKSIOJA_MM_KISAVEIKKAUS_V
UNION
SELECT 'Anna', points FROM MM_KISAVEIKKAUS.ANNA_MM_KISAVEIKKAUS_V
UNION 
SELECT 'Anni', points FROM MM_KISAVEIKKAUS.ASM_MM_KISAVEIKKAUS_V
UNION
SELECT 'Dima', points FROM MM_KISAVEIKKAUS.DIMA_MM_KISAVEIKKAUS_V
UNION 
SELECT 'Otso', points FROM MM_KISAVEIKKAUS.OTSO_MM_KISAVEIKKAUS_V
UNION
SELECT 'Juhani', points FROM MM_KISAVEIKKAUS.JUHANI_MM_KISAVEIKKAUS_V
UNION
SELECT 'Kaarel', points FROM MM_KISAVEIKKAUS.KAAREL_MM_KISAVEIKKAUS_V
UNION
SELECT 'Kalle', points FROM MM_KISAVEIKKAUS.KALLE_MM_KISAVEIKKAUS_V
UNION
SELECT 'Kimmo', points FROM MM_KISAVEIKKAUS.KIMMO_MM_KISAVEIKKAUS_V
UNION
SELECT 'Lars', points FROM MM_KISAVEIKKAUS.LARS_MM_KISAVEIKKAUS_V
UNION
SELECT 'Liisa', points FROM MM_KISAVEIKKAUS.LIISA_MM_KISAVEIKKAUS_V
UNION
SELECT 'Rasmus', points FROM MM_KISAVEIKKAUS.RASMUS_MM_KISAVEIKKAUS_V
UNION
SELECT 'Tuomas', points FROM MM_KISAVEIKKAUS.TUOMAS_MM_KISAVEIKKAUS_V

ORDER BY points DESC
;