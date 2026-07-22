class movie:
    def __init__(self, moviename,directorname,rating):
        self.moviename=moviename
        self.directorname=directorname
        self.rating=rating
    def showmovie(self):
        print(f"{self.moviename}:{self.directorname}:{self.rating}")
s1=movie("hinanna","nil","5")
s2=movie("devara","nil","5")
s1.showmovie()
s2.showmovie()
                       
