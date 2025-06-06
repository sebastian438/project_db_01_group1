import pandas as pd
from dotenv import load_dotenv, dotenv_values
from os import makedirs
from io import StringIO

config = dotenv_values(".env")
makedirs('../SQLs/', exist_ok=True)

def sql_connection (): 
    conn = psycopg2.connect(
    host = config.host, port = config.port, dbname = config.dbname, user=config.username, password=config.pswd)
    print()


def write_sql(table_name, df):
    with open(f'../SQLs/{table_name}.sql', 'w') as fh:
        fh.write('\n'.join(df.sql.values))


fd = '../data/'
clase_1  = pd.read_csv(fd+ 'clase_1.csv', sep=';')
clase_2  = pd.read_csv(fd+ 'clase_2.csv', sep=';')
clase_3  = pd.read_csv(fd+ 'clase_3.csv', sep=';')
clase_4  = pd.read_csv(fd+ 'clase_4.csv', sep=';')
claustro = pd.read_csv(fd+'claustro.csv', sep=';')


df_DS = pd.concat([clase_1, clase_2])
df_FS = pd.concat([clase_3, clase_4])


df_alumno = pd.concat([ df_DS.iloc[:, :2], df_FS.iloc[:, :2] ])
df_alumno.reset_index(drop=True, inplace=True)
df_alumno['sql'] = "INSERT INTO Alumno(nombre, email) VALUES ('"\
                    + df_alumno.Nombre + "', '" + df_alumno.Email + "');"

write_sql('alumno', df_alumno)


df_profesor = pd.DataFrame(claustro.Nombre)
df_profesor['sql'] = "INSERT INTO Profesor(nombre) VALUES ('" + df_profesor.Nombre + "');"

write_sql('profesor', df_profesor)


df_vertical = pd.DataFrame(claustro.Vertical.unique(), columns=['Vertical'])
df_vertical['sql'] = "INSERT INTO Vertical(nombre) VALUES ('" + df_vertical.Vertical + "');"

write_sql('vertical', df_vertical)


df_proyecto = pd.DataFrame({'nombre': list(df_DS.columns[-5:]) + list(df_FS.columns[-5:]),
                            'id_vertical': [1]*5 + [2]*5})
df_proyecto['sql'] = "INSERT INTO Proyecto(nombre, id_vertical) VALUES ('"\
                    + df_proyecto.nombre + "', " + df_proyecto.id_vertical.astype(str)  + ");"

write_sql('proyecto', df_proyecto)


sql_lines = []

for i, row in enumerate(df_DS.itertuples()):
    for j, v in enumerate(row[-5:]):
        sql_lines += ['INSERT INTO Evaluacion(resultado, id_alumno, id_proyecto) VALUES ('+
              f"'{v}', {i+1}, {j+1});\n"]

for i, row in enumerate(df_FS.itertuples()):
    for j, v in enumerate(row[-5:]):
        sql_lines += ['INSERT INTO Evaluacion(resultado, id_alumno, id_proyecto) VALUES ('+
              f"'{v}', {i+1+df_DS.shape[0]}, {j+1+5});\n"]

with open('../SQLs/evaluacion.sql', 'w') as fh:
    fh.writelines(sql_lines)
