--select * from places;

--select count(*) from places;

--select count(*) from information_schema.columns where table_name = 'places';

/*
select count(*)
from places 
where id is null;
*/

/*
select place_code
from places 
group by place_code
having count(*) > 1;
*/

/*
select postcode
from places
where length(postcode) > 4;
*/

/*
select address
from places 
where holding_number is null and super_sub_area is null and sub_area is null;
*/

/*
select count(distinct city) as distinct_city_count
from places;
*/



--                                      FIELD VALIDIATION 


--        postcode field 

/*
select postcode
from places
where length(postcode) > 4;
*/

/*
select count(*) as invalid_count
from places 
where not (postcode ~ '^[0-9]+$');
*/

--       city field 

/*
select distinct city as dis_city
from places 
*/

/*
select count(*) as cnt 
from places 
where city is null;
*/

--      type, sub_type field 

/*
select count(place_code) 
from places 
where type = sub_type;
*/

--      private_public_flag field 

/*
select distinct private_public_flag
from places 
*/

--      popularity_ranking field 
/*
select count(*) as invalid_count
from places
where (popularity_ranking::text ~ '^[a-zA-Z]+$');
*/

--      location field

/*
select place_code, location 
from places 
where location is null;
*/

--      district, union field 

/*
select district, "union"  
from places
where district = "union" ;
*/

/*
select place_code  
from places
where district = "union" ;
*/

--                     special character check 
/*
SELECT holding_number, place_code 
FROM places
WHERE holding_number ~ '[?@!#$%^*()è:=|ã~]';
*/

/*
select business_name , place_code
from places 
where business_name ~ '[?!#$%^*è=ã~]';
*/

/*
select place_name, place_code 
from places 
where place_name ~ '[?!#$%^*è=ã~]';
*/

select address , place_code
from places 
where address ~ '[?!$%^*è=ã~]';


--                    area, sub_area, super_sub_area field 

/*
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND 
table_name = 'places';
/*

/*
select count(*) as invalid_count
from places 
where (area ~ '^[0-9]+$');
*/

/*
select count(*) as invalid_count
from places 
where (sub_area ~ '^[0-9]+$');
*/

/*
select area, sub_area, super_sub_area
from places 
where area = sub_area and area = super_sub_area;
*/

--          road_name_number, super_sub_area field

/*
select place_code 
from places 
where road_name_number = super_sub_area 
*/

--         holding_number field 

/*
select holding_number, place_code 
from places 
where not holding_number ~ '\d' and holding_number !~ '^\d+$';
*/

/*
select holding_number, place_code 
from places 
where holding_number !~ '[0-9]'
*/

--      road_name_number field

/*
select holding_number, road_name_number 
from places 
where road_name_number !~[0-9] and road_name_number = holding_number;
*/

/*
select road_name_number 
from places 
where road_name_number !~ '[0-9]' and road_name_number not similar to '%Road%' and road_name_number not similar to '%Street%';
*/

/*
select place_code 
from places 
where road_name_number is null and holding_number is not null;
*/

/*
select place_code 
from places
where area = road_name_number 
*/

/*
select holding_number, road_name_number, place_code 
from places 
where road_name_number is not null and holding_number is null;
*/

/*
select place_code 
from places 
where road_name_number is not null and holding_number is null;
*/

--      sub_type 

/*
select count(*) 
from places 
where sub_type is null;
*/

--      sub_area , super_sub_area

/*
select place_code 
from places 
where sub_area = super_sub_area 
*/

/*
select business_name 
from places 
where business_name ~ '^[0-9]'
*/

/*
select  "union" 
from places 
where ("union" ~ '^[0-9]+$');
*/

/*
select  area  
from places 
where (area ~ '[0-9]+$');
*/

--                                   CHECK

/*
select count(data_source)
from places 
where data_source is not null;
*/

/*
select place_code 
from places
where ("union" ~ '^[0-9]')
*/


/*
select place_code 
from places 
--where (super_sub_area ~ '[0-9]+$')
where super_sub_area = area 
*/

/*
select city, holding_number, place_code 
from places 
where city = 'Dhaka' and holding_number is null;
*/

--select substring('abc', 1,2); -- substring('string', pos where start, pos till the index)


/*
with expanded as (
     select p.id,
     p.place_code, 
     unnest(string_to_array(p.sub_type, ',')) as single_value
     from places as p
),
value_counts as (
     select id, single_value, count(*) as count 
     from expanded 
     group by id, single_value
),
repeated_values as (
     select id
     from value_counts
     where count > 1
     group by id 
),
result as (
     select p.place_code, p.sub_type 
     from places as p
     join repeated_values r on p.id = r.id 
)
--select count(place_code)
select place_code, sub_type 
from result;
*/
     
     
/*
with expanded as (
     select p.id,
     p.place_code, 
     unnest(string_to_array(p.type, ',')) as single_value
     from places as p
),
value_counts as (
     select id, single_value, count(*) as count 
     from expanded 
     group by id, single_value
),
repeated_values as (
     select id
     from value_counts
     where count > 1
     group by id 
),
result as (
     select p.place_code, p.type 
     from places as p
     join repeated_values r on p.id = r.id 
)
select count(place_code)
--select place_code, type 
from result;
*/

/*
select place_code 
from places 
where city='Dhaka' and holding_number is null and road_name_number is not null;
*/

/* 
select type 
from places 
where (type ~ '^[az]');
*/
     

--                                   START

/*
(
    SELECT * 
    FROM places 
    WHERE district = 'Dhaka' 
    LIMIT 10
)
UNION ALL
(
    SELECT * 
    FROM places 
    WHERE district = 'Chattogram' 
    LIMIT 10
)
*/


--              todo: each sub_district -> 5 data 

/*
SELECT COUNT(DISTINCT sub_district) AS distinct_sub_district_count
FROM places;
*/

/*
with places as (
     select *,
     ROW_NUMBER() over (partition by sub_district) as cnt
     from places 
)
select address, holding_number, road_name_number, postcode, super_sub_area, sub_area, area, city, district, sub_district , "union", business_name, place_name
from places
where cnt <= 5;
*/


/*
select count(distinct area)
from places 
where city='Dhaka'
*/


/*
(
    with places as (
        select *,
               ROW_NUMBER() over (partition by sub_district) as cnt
        from places
    )
    select address, holding_number, road_name_number, postcode, super_sub_area, sub_area, area, city, district, sub_district, "union", business_name, place_name
    from places
    where cnt <= 5
)
union all
(
    with places as (
        select *,
               ROW_NUMBER() over (partition by area) as rn
        from places
        where city = 'Dhaka'
    )
    select address, holding_number, road_name_number, postcode, super_sub_area, sub_area, area, city, district, sub_district, "union", business_name, place_name
    from places
    where rn <= 10
);
*/
