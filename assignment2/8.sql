select v from (
SELECT a.docid as r, b.docid as c, SUM(a.count * b.count) as v
  FROM Frequency a, Frequency b
 WHERE a.docid in('10080_txt_crude', '17035_txt_earn') and
 b.docid in('10080_txt_crude', '17035_txt_earn') and
 a.term = b.term
 GROUP BY a.docid, b.docid
)
where
r = '10080_txt_crude' and c = '17035_txt_earn';
