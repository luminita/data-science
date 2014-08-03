# PART 3 
#————
SELECT i, j, SUM(A.count*B.count) FROM 
	(SELECT DISTINCT docid as i FROM frequency), 
	(SELECT DISTINCT docid as j from frequency), frequency AS A, frequency AS B 
	WHERE A.docid = i AND B.docid = j AND i < j AND A.term = B.term 
	GROUP BY i, j;