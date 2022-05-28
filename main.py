from os import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name= name
        self.age= age
        self.tracks= tracks
        self.score= score

    def change_name(self, name):
        self.name= name
        print("your name is ", self.name)
    def change_age(self, age):
        self.age= age
        print("your age is ", self.age)
    def add_track(self,tracks):
        self.tracks.append(tracks)
        print("your track is ", self.tracks)
    def get_score(self,score):
        self.score= score
        print("your score is ", self.score)

Bob = Student("Bob",26,[],20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(23.67)
