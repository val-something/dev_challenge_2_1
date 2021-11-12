-- Create a service accoutn user to enable Django to use its own credentials. Be sure to change the password!
CREATE USER django_service_account WITH PASSWORD 'xxx';
GRANT CONNECT ON DATABASE sample_data TO django_service_account;
ALTER USER django_service_account CREATEDB;

-- Remove pre-existing tables if necessary
drop table sample_data_countries;
drop table sample_data_incidents;

-- Create three tables
create table sample_data_countries (
    -- Fill this out
);

create table sample_data_incidents (
    -- Fill this out
);

-- Give permissions to CRUD and use various foreign key/autoincrement features to the service account
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public to django_service_account;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON sample_data_countries TO django_service_account;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON sample_data_incidents TO django_service_account;

-- Insert sample data
insert into 
    sample_data_countries () 
values 
    ();

insert into
    sample_data_incidents ()
values
    ();

-- Select inserted data to double check everything
select * from sample_data_incidents;
