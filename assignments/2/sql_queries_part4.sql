# PART 4
#————

CREATE VIEW full_frequency AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count

SELECT i, j, SUM(A.count*B.count) AS similarity_score FROM 
	(SELECT DISTINCT docid as i FROM full_frequency), 
	(SELECT DISTINCT docid as j from full_frequency), 
        full_frequency AS A, full_frequency AS B 
	WHERE A.docid = i AND B.docid = j AND A.term = B.term
              AND A.docid = ‘q’ 
	GROUP BY i, j ORDER BY similarity_score DESC LIMIT 10;