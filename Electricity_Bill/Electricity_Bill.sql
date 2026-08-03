-- create database electricity_bill;
-- show databases;
-- use electricity_bill;

--  create table consumers(
--  	consumer_no varchar(20) primary key,
--      consumer_name varchar(100) not null,
--      address varchar(200) not null,
--      mobile varchar(10),
--      email varchar(100),
--      division varchar(100),
--      sanctioned_load decimal(5,2),
--      meter_no varchar(50),
--      connection_date date
--      );
     
-- describe consumers;

--  create table bills(
--  	bill_no varchar(30) primary key,
--      consumer_no varchar(20) not null,
--      bill_month varchar(20) not null,
--      bill_date date not null,
--      due_date date not null,
--      units decimal(10,2) not null,
--      previous_due decimal (10,2) not null,
--      current_bill decimal (10,2) not null,
--      payable_amount decimal(10,2) not null,
--      
--      foreign key(consumer_no) references consumers(consumer_no)
--      );

-- alter table consumers
-- modify mobile varchar(10) not null,
-- modify email varchar(100) not null,
-- modify division varchar(100) not null,
-- modify sanctioned_load decimal(5,2) not null,
-- modify meter_no varchar(50) not null,
-- modify connection_date date not null;

-- describe consumers;

-- insert into consumers
-- (consumer_no, consumer_name, address, mobile, email, division, sanctioned_load, meter_no, connection_date)
-- values
-- ('C1001','Anjali Gajara','H.No. 1-10-45, Ashok Nagar, RTC X Roads, Hyderabad – 500020','7452156985','anjali90@gmail.com','Himayatnagar',4.0,'MTR45892173','2021-03-14'),
-- ('C1002','Archana Singh','Flat No. 203, Sai Residency, Kukatpally Housing Board Colony, Hyderabad – 500072','7854123695','archana23@gmail.com','Kukatpally',4.0,'MTR52613984','2018-10-12'),
-- ('C1003','Akshay Guru','H.No. 6-3-120/8, Banjara Hills, Road No. 2, Hyderabad – 500034','7605241685','akshayguru14@gmail.com','Banjara Hills',4.0,'MTR78546091','2020-05-30'),
-- ('C1004','Shivam Kumar','H.No. 8-3-168/1, Srinagar Colony, Hyderabad – 500073','8567941236','shivam@gmail.com','Erragadda',4.0,'MTR76218450','2019-12-19'),
-- ('C1005','Nirali Bhanushali','Flat No. 502, Royal Heights, Chandanagar, Hyderabad – 500050','9327498512','nbhanushali@gmail.com','Serilingampally',4.0,'MTR39567128','2024-02-04');

describe bills;