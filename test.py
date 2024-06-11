import trackintel as ti

database_name = 'trackintel-tests'
conn_string = 'postgresql://test:1234@localhost:5432/' + database_name

pfs = ti.read_positionfixes_csv('examples/data/posmo_trajectory_2.csv', sep=';')
pfs.to_postgis('positionfixes', conn_string, if_exists='append')