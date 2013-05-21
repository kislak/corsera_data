select count(*) 
from  
Frequency f join Frequency ff 
on f.docid=ff.docid and f.term='transactions' and ff.term='world';
