CREATE EXTERNAL TABLE IF NOT EXISTS Stock_Exchange_Daily(
symbol STRING,
full_name STRING,
quantity BIGINT,
volume BIGINT,
value BIGINT,
yesterday_qnt BIGINT,
first_order_value INT,
last_order_value INT,
last_order_value_change FLOAT,
last_order_value_change_percent FLOAT,
close_price INT,
close_price_change FLOAT,
close_price_change_percent FLOAT,
min_price INT,
max_price INT,
EPS FLOAT,
PE FLOAT,
buy_quantity INT,
buy_volume INT,
buy_price INT,
sell_volume INT,
sell_price INT,
sell_quantity INT,
fa_date STRING,
en_date DATE,
fa_year STRING
) 
COMMENT 'Daily Trades Of Iranian Stocks - Aggregated By TSETMC'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE LOCATION '/data/data_lake/stock'
TBLPROPERTIES ('skip.header.line.count'='1');



CREATE EXTERNAL TABLE IF NOT EXISTS Stock_Exchange_Daily_Partitioned(
symbol STRING,
full_name STRING,
quantity BIGINT,
volume BIGINT,
value BIGINT,
yesterday_qnt BIGINT,
first_order_value INT,
last_order_value INT,
last_order_value_change FLOAT,
last_order_value_change_percent FLOAT,
close_price INT,
close_price_change FLOAT,
close_price_change_percent FLOAT,
min_price INT,
max_price INT,
EPS INT,
PE FLOAT,
buy_quantity INT,
buy_volume INT,
buy_price INT,
sell_volume INT,
sell_price INT,
sell_quantity INT,
fa_date STRING,
en_date DATE
) 
COMMENT 'Daily Trades Of Iranian Stocks - Aggregated By TSETMC'
PARTITIONED BY (fa_year STRING)
STORED AS TEXTFILE LOCATION '/data_lake/stock'
TBLPROPERTIES ('skip.header.line.count'='1');