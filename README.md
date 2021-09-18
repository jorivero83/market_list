# market_list
This is project to generate the market list based on a kitchen recipes list.


SQL Code
```
select 
    t1.name, t1.units, 
    sum(t1.size) as size 
from ingredientes as t1
inner join recetas as t2
on t1.receta_id = t2.id
WHERE 
    t2.id in (1, 5, 6)
    and t1.name not in ('agua')
GROUP by t1.name, t1.units
order by size desc
```

Results:
```

```
