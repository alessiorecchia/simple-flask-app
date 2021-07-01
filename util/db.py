import os

from uuid import uuid4

import pandas as pd
 
def read_db():
    db_path = "./util/db.csv"
    projects = []
    with open(db_path) as f:
        lines = f.readlines()
        for line in  lines:
            if(len(line)!=0):
                array = line.split(",")
                projects.append(array)
    projects.pop(0)
    return projects

def write_project(title,description,cover,githubLink,liveLink):
    line = "{},{},{},{},{},{}".format(uuid4(),title,description,cover,githubLink,liveLink)
    db_path = "./util/db.csv"
    with open(db_path, 'r+') as f:
        lines = f.readlines()
        if(len(lines)==0):
            f.write("id,title,description,cover,githubLink,liveLink")
            f.write(f'{line}')
        else:
            f.write(f'\n{line}')
    return None


def find_project_by_id(id):
    projects = read_db()
    found = None
    for  project in projects:
        project_id = project[0]
        if(project_id==id):
            return project
    return found

def find_project_by_id_and_delete(id):
    db_path = "./util/db.csv"
    df = pd.read_csv(db_path,index_col=0) 
    for k, el in enumerate(df.id):
        if el == id:
            print(k,df.id[k])
            df = df.drop(k)
    df.to_csv(db_path)  
    return None
    