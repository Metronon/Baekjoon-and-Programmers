-- 코드를 작성해주세요
SELECT COUNT(INF.FISH_TYPE) AS FISH_COUNT
FROM FISH_INFO AS INF
INNER JOIN FISH_NAME_INFO AS NME
ON INF.FISH_TYPE = NME.FISH_TYPE
WHERE NME.FISH_NAME IN ("BASS", "SNAPPER");