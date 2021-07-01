import os

def read_db():
    db_path = "./util/db.csv"
    projects = []
    with open(db_path) as f:
        lines = f.readlines()
        for line in  lines:
            array = line.split(",")
            projects.append(array)
    
    return projects

def write_project(title,description,cover,githubLink,liveLink):
    line = "{},{},{},{},{}".format(title,description,cover,githubLink,liveLink)
    db_path = "./util/db.csv"
    with open(db_path, 'a') as f:
        f.write(f'\n{line}')
    return None
