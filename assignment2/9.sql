select max(v) from(

select c, v from (
SELECT a.docid as r, b.docid as c, SUM(a.count * b.count) as v
  FROM Frequency1 a, Frequency1 b
 WHERE a.docid in('q') and
 a.term = b.term
 GROUP BY a.docid, b.docid
)
where
r = 'q'
order by v

);
