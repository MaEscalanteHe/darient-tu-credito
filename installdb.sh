sudo -u postgres dropdb tucredito >> /dev/null
sudo -u postgres dropuser tucredito >> /dev/null
sudo -u postgres createuser tucredito
sudo -u postgres createdb tucredito
sudo -u postgres psql << EOF
alter user tucredito with encrypted password 'tucredito_password123';
alter role tucredito set client_encoding to 'utf8';
alter role tucredito set default_transaction_isolation to 'read committed';
alter role tucredito set timezone to 'utc';
alter role tucredito createdb;
grant all privileges on database tucredito to tucredito ;\q
EOF