import glob
import os
import json

class PersonInfo(object):
    def __init__(self, FirstName, LastName, NetID, GitHubID, TeamName):
        self.fn=FirstName
        self.ln=LastName
        self.netid=NetID
        self.gitid=GitHubID
        self.tn=TeamName
        

def main():
    check_for_everyone()
    filesInDir = collect_all_csv_filenames()
    create_master_file(filesInDir)
    check_for_team_names()
    create_JSON_files(filesInDir)   


def check_for_everyone():
    ePath=glob.glob("everyone.csv")
    if ePath!=None:
        os.remove("everyone.csv")

def collect_all_csv_filenames():
    filesInDir=glob.glob("*.csv")
    return filesInDir

def create_master_file(filesInDir):
    f = open("everyone.csv",'w')
    for file in filesInDir:
        myInput=open(file,'r')
        line=myInput.readline()
        while len(line)>0:
            f.write(line)
            if line[len(line)-1]!='\n':
                f.write('\n')
            line=myInput.readline()
        myInput.close()
    f.close()

def create_JSON_files(filesInDir):
    for file in filesInDir:
        myInput=open(file,'r')
        line=myInput.readline()
        if line[0]=='#':
            line=myInput.readline()
        entries=line.split(',')
        # json_out=PersonInfo(entries[0],entries[1],entries[2],entries[3],entries[4])
        json_out=[entries[0],entries[1],entries[2],entries[3],entries[4]]
        filename=file.split('.')[0]
        myOut=open(filename+".json",'w')
        json.dump(json_out,myOut)
        myOut.close()
        myInput.close()
        

def check_for_team_names():
    noTeams=0
    with open('everyone.csv') as f:
        for line in f:
            if (',' in line) and (line[0]!='#'):
                entries=line.split(",")
                teamName=entries[4].strip()
                noTeams+=1
                print('Team Number: {}  Team Name: {}'.format(noTeams,teamName))
                if ' ' in teamName:
                    print("A team name with a space found {}".format(entries[2]))
        


if __name__ == "__main__":
    main()
