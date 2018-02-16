import os
import MySQLdb

class element_model(object):
    def __init__(self):
        self.file = []
        self.model = []
        self.period = []
        self.project = []
        self.member = []

def create_model(modelo, cursor):
    insert_query = 'INSERT INTO modelos_tb (name) VALUES (%i)' %(modelo)
    cursor.execute(insert_query)
    cursor.fetchall()

def create_member(membro, cursor):
    insert_query = 'INSERT INTO membros_tb (name) VALUES (%i)' %(membro)
    cursor.execute(insert_query)
    cursor.fetchall()

def create_period(periodo, cursor):
    insert_query = 'INSERT INTO periodos_tb (name) VALUES (%i)' %(periodo)
    cursor.execute(insert_query)
    cursor.fetchall()

def create_project(projeto, cursor):
    insert_query = 'INSERT INTO projetos_tb (name) VALUES (%i)' %(projeto)
    cursor.execute(insert_query)
    cursor.fetchall()

def _push_model_data(nome, modelo, membro, periodo, projeto):
    try:
        db = MySQLdb.connect("localhost","root","&i1hm","pacmen_db" )
        cursor = db.cursor()

        query_model   = 'SELECT id FROM modelos_tb  WHERE name=%s' %(modelo)
        cursor.execute(query_model)
        id_model = cursor.fetchall()        
        if id_model == '':
            create_model(modelo,cursor)
            query_model   = 'SELECT id FROM modelos_tb  WHERE name=%s' %(modelo)
            cursor.execute(query_model)
            id_model = cursor.fetchall() 
        
        query_member  = 'SELECT id FROM membros_tb  WHERE name=%s' %(membro)
        cursor.execute(query_member)
        id_member = cursor.fetchall()
        if id_member == '':
            create_member(membro,cursor)
            query_member   = 'SELECT id FROM membros_tb  WHERE name=%s' %(membro)
            cursor.execute(query_member)
            id_member = cursor.fetchall() 
        
        query_period  = 'SELECT id FROM periodos_tb WHERE name=%s' %(periodo)
        cursor.execute(query_period)
        id_period = cursor.fetchall()
        if id_period == '':
            create_period(periodo,cursor)
            query_period   = 'SELECT id FROM periodos_tb  WHERE name=%s' %(periodo)
            cursor.execute(query_period)
            id_period = cursor.fetchall() 
        
        query_project = 'SELECT id FROM projetos_tb WHERE name=%s' %(projeto)
        cursor.execute(query_project)
        id_project = cursor.fetchall()
        if id_project == '':
            create_project(projeto,cursor)
            query_project   = 'SELECT id FROM projetos_tb  WHERE name=%s' %(projeto)
            cursor.execute(query_project)
            id_project = cursor.fetchall() 

        verify_query = 'SELECT id FROM dados_tb WHERE nome=%s' %(nome)
        cursor.execute(verify_query)
        is_in = cursor.fetchall()
        if is_in == '':
            insert_query = 'INSERT INTO dados_tb (tipo, nome, membro, modelo, projeto) VALUES (%i, %s, %i, %i, %i)' %(id_period, nome, id_member, id_model, id_project)
            cursor.execute(insert_query,cursor)
            cursor.fetchall()
            db.close()
            return (True)
        else:
            db.close()
            return (False)
    except:
        return ('Erro')

files = [val for sublist in [[os.path.join(i[0], j)\
                 for j in i[2]] for i in os.walk('./')] for val in sublist]

out = element_model()
for file_path in files:
     file    = file_path.split('/')[-1]
     model   = file_path.split('/')[-2]
     period  = file_path.split('/')[-3]
     member  = file_path.split('/')[-4]
     project = file_path.split('/')[-5]

     out.file.append(file)
     out.modelo.append(model)
     out.periodo.append(period)
     out.membro.append(member)
     out.projeto.append(project)

num_new_files = 0
for i in range(0, len(out.file)):
    # inserted = _push_model_data(out.file[i], out.modelo[i], out.membro[i],\
    #                                          out.periodo[i], out.projeto[i])
    inserted == True 
    print(out.file[i], out.modelo[i], out.membro[i],\
                                              out.periodo[i], out.projeto[i])
    if inserted == True:
           num_new_files += 1
    elif inserted == 'Erro':
        print("Erro ao inserir o arquivo: %s" %(out.file[i].split('/')[-1]))

print("Total de arquivos: $s" %(len(out.file)))
print("Novos:" %(num_new_files))
