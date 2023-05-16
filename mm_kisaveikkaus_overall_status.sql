CREATE OR REPLACE VIEW MM_KISAVEIKKAUS.MM_KISAVEIKKAUS_OVERALL_STATUS (id, match, home_team_goals_final, away_team_goals_final, KALLE_PTS, MIKA_PTS, ALEKSI_PTS, ANNA_PTS, ANNI_PTS, DIMA_PTS, OTSO_PTS, JUHANI_PTS, KAAREL_PTS, KIMMO_PTS, LARS_PTS, LIISA_PTS, RASMUS_PTS, TUOMAS_PTS) AS (

SELECT 

        final.id
      , final.match
      , final.home_team_goals_final
      , final.away_team_goals_final
      , kalle.points AS KALLE_PTS
      , mika.points AS MIKA_PTS
      , aleksi.points AS ALEKSI_PTS
      , anna.points AS ANNA_PTS
      , asm.points AS ANNI_PTS
      , dima.points AS DIMA_PTS
      , otso.points AS OTSO_PTS
      , juhani.points AS JUHANI_PTS
      , kaarel.points AS KAAREL_PTS
      , kimmo.points AS KIMMO_PTS
      , lars.points AS LARS_PTS
      , liisa.points AS LIISA_PTS
      , rasmus.points AS RASMUS_PTS
      , tuomas.points AS TUOMAS_PTS

 FROM MM_KISAVEIKKAUS.FINAL_MM_KISAVEIKKAUS_MATCHES_V final
 
    INNER JOIN MM_KISAVEIKKAUS.KALLE_MM_KISAVEIKKAUS_MATCHES_V kalle ON final.id = kalle.id
    INNER JOIN MM_KISAVEIKKAUS.MIKA_MM_KISAVEIKKAUS_MATCHES_V mika ON final.id = mika.id 
    INNER JOIN MM_KISAVEIKKAUS.ALEKSIOJA_MM_KISAVEIKKAUS_MATCHES_V aleksi ON final.id = aleksi.id 
    INNER JOIN MM_KISAVEIKKAUS.ANNA_MM_KISAVEIKKAUS_MATCHES_V anna ON final.id = anna.id 
    INNER JOIN MM_KISAVEIKKAUS.ASM_MM_KISAVEIKKAUS_MATCHES_V asm ON final.id = asm.id 
    INNER JOIN MM_KISAVEIKKAUS.DIMA_MM_KISAVEIKKAUS_MATCHES_V dima ON final.id = dima.id 
    INNER JOIN MM_KISAVEIKKAUS.OTSO_MM_KISAVEIKKAUS_MATCHES_V otso ON final.id = otso.id 
    INNER JOIN MM_KISAVEIKKAUS.JUHANI_MM_KISAVEIKKAUS_MATCHES_V juhani ON final.id = juhani.id 
    INNER JOIN MM_KISAVEIKKAUS.KAAREL_MM_KISAVEIKKAUS_MATCHES_V kaarel ON final.id = kaarel.id 
    INNER JOIN MM_KISAVEIKKAUS.KIMMO_MM_KISAVEIKKAUS_MATCHES_V kimmo ON final.id = kimmo.id 
    INNER JOIN MM_KISAVEIKKAUS.LARS_MM_KISAVEIKKAUS_MATCHES_V lars ON final.id = lars.id 
    INNER JOIN MM_KISAVEIKKAUS.LIISA_MM_KISAVEIKKAUS_MATCHES_V liisa ON final.id = liisa.id
    INNER JOIN MM_KISAVEIKKAUS.RASMUS_MM_KISAVEIKKAUS_MATCHES_V rasmus ON final.id = rasmus.id 
    INNER JOIN MM_KISAVEIKKAUS.TUOMAS_MM_KISAVEIKKAUS_MATCHES_V tuomas ON final.id = tuomas.id

    
ORDER BY ID ASC
) ;
