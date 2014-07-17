# PART 2 
#————
SELECT i, j, SUM(A.value*B.value) FROM 
	(SELECT DISTINCT row_num as i FROM A), 
	(SELECT DISTINCT col_num as j from B), A, B 
	WHERE A.row_num = i AND B.col_num = j AND A.col_num = B.row_num 
	GROUP BY i, j;