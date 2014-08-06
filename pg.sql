create database filesCenter;
create sequence files_seq start with 1 increment by 2  maxvalue 10000000 ;  
create table files( id bigint NOT NULL DEFAULT nextval('files_seq'), 
                    logical_name varchar(100), 
                    physical_name varchar(100),
                    file_type varchar(50),
                    from_url varchar(200),
                    saved_position varchar(10));

