SELECT gd.year as "year",
	gd.avg_temp as "global_temp",
    cd.avg_temp as "wash_temp"
from global_data as gd
	JOIN city_data as cd
    ON cd.year = gd.year
 WHERE cd.city = 'Washington' AND cd.avg_temp IS NOT Null AND gd.avg_temp IS NOT NULL
