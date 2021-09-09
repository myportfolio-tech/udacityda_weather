CREATE TABLE "city_data" (
"year" SMALLINT, 
"city" VARCHAR(100),
"country" VARCHAR(100),
"avg_temp"  FLOAT
);


COPY "city_data" ("year", "city", "country", "avg_temp")
FROM 'C:\Repos\Udacity_DA\project1\data\city_data.csv'
DELIMITER ','
CSV HEADER;



CREATE TABLE "city_list" (
"city" VARCHAR(100),
"country" VARCHAR(100)
);


COPY "city_list" ("city", "country")
FROM 'C:\Repos\Udacity_DA\project1\data\city_list.csv'
DELIMITER ','
CSV HEADER;


CREATE TABLE "global_data" (
"year" SMALLINT,
"avg_temp"  FLOAT
);


COPY "city_list" ("city", "country")
FROM 'C:\Repos\Udacity_DA\project1\data\global_data.csv'
DELIMITER ','
CSV HEADER;