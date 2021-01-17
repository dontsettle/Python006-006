
INNER JOIN 
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 并取出id 对应的name.
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 取出id对应的name外还取出Table1表所有的id和name.
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id
WHERE Table2.id NULL;
结果：根据Table1和Table2共同的id 取出Table1表id不对应的name，其它值都显示为空.
 RIGHT JOIN
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 取出id对应的name外还取出Table2表所有的id和name.
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id
WHERE Table1.id NULL;
结果：根据Table1和Table2共同的id 取出Table2表id不对应的name，其它值都显示为空.