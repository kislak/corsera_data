select v from(
SELECT a.row_num as r, b.col_num as c, SUM(a.value * b.value) as v
  FROM a, b
 WHERE a.col_num = b.row_num
 GROUP BY a.row_num, b.col_num
)
where r = 2 and c = 3;
