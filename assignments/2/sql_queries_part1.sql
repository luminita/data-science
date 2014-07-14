#Part1
#——————
SELECT COUNT(*) FROM frequency 
	WHERE docid = "10398_txt_earn";

#138


SELECT COUNT(*) FROM 
	(SELECT term FROM frequency 
		WHERE docid = "10398_txt_earn" AND count = 1);
#110


SELECT COUNT(*) FROM 
	(SELECT term FROM frequency 
		WHERE docid = "10398_txt_earn" AND count = 1 
	UNION 
	SELECT term FROM frequency 
		WHERE docid = "925_txt_trade" AND count = 1);
#324


SELECT COUNT(*) FROM 
	(SELECT DISTINCT docid FROM frequency 
		WHERE term = 'parliament');
#15


SELECT COUNT(*) FROM 
	(SELECT * FROM 
		(SELECT docid, SUM(count) AS nterms FROM frequency 
			GROUP BY docid) 
	WHERE nterms > 300);
SELECT COUNT(*) FROM 
	(SELECT docid FROM frequency
		GROUP BY docid
		HAVING SUM(count) > 300);
#107



SELECT COUNT(*) FROM 
	(SELECT DISTINCT docid FROM frequency 
		WHERE docid in 
			(SELECT DISTINCT docid AS transaction_docids FROM frequency 
				WHERE term = "transactions") 
		AND term = "world");
#3