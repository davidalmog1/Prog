import json
from uuid import uuid4
from pprint import pprint


class Agron:

    def __init__(self):
        f = open("db.json","r")
        self.people = json.loads(f.read())
        f.close()

    def _create_uid(self):
        tid = str(uuid4()).split('-')
        tuid = tid[0] + tid[-1]
        if tuid in self.people:
            return self._create_uid()
        else:
            return tuid

    def add(self):
        uid = self._create_uid()
        self.people[uid] ={
            "Uid":uid,
            "name": input("\nEnter First Name: "),
            "last name": input("\nEnter Last Name: "),
            "phone": input("\nEnter phone number: "),
            "family": [],
        }
    
    def delete(self):
        uid = input("\nEnter Uid: ")
        if uid in self.people:
            self.people.pop(uid)
        else:
            print("\nPerson not exists !")       
    
    def edit(self):
        uid = input("\nEnter Uid: ")
        if uid in self.people:
            edit = input("\nSelect filed: ")
            if edit in ["name","last name","phone","Uid","family"]:
                changeTo = input("\nEnter new value: ")
                self.people[uid][edit] = changeTo
            else:
                print("\nWrong input !")
        else:
            print("\nUid Not found")
    
    def search(self):
        uid = input("\nEnter Uid: ")
        if uid in self.people:
            print(self.people[uid])
        else:
            print("\nUid Not found")
        
    def exit(self,select):
        if select == 'yes':
            f = open("db.json","w")
            f.write(json.dumps(self.people))
            f.close()
        print("\nCloas the program & save the data\n")























msg = '''
\nWelcome to Agron!
please Chose option:
1) Add
2) Search
3) Delete
4) Edit
5) Print All
6) Save & Exit
7) Exit(w/o Save)
\n
'''
