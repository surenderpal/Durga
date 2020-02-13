class SportsNews:
    def sportsInfo(self):
        print('Sports information 1')
        print('Sports information 2')
        print('Sports information 3')
        print('Sports information 4')
class MovieNews:
    def movieInfo(self):
        print('Movies information 1')
        print('Movies information 2')
        print('Movies information 3')
        print('Movies information 4') 
class PoliticsNews:
    def politicsInfo(self):
        print('Politics information 1')
        print('Politics information 2')
        print('Politics information 3')
        print('Politics information 4')
class DurgaNews:
    def __init__(self,sports,movies,politics):
        print('\nWelcome to the Durga News channels:---\n')
        self.sports=sports
        self.movies=movies
        self.politics=politics
    def getTotalInfo(self):
        print('Welcome to Durga News:---')
        self.sports.sportsInfo()
        self.movies.movieInfo()
        self.politics.politicsInfo()
sp=SportsNews()
mv=MovieNews()
pol=PoliticsNews() 
d=DurgaNews(sp,mv,pol)
d.getTotalInfo()








# class DurgaNews:
#     def __init__(self):
#         # print('Welcome to Durga news')
#         self.sports=SportsNews()
#         self.movie=MovieNews()
#         self.politics=PoliticsNews()
#     def getTotalInfo(self):
#         print('\nWelcome to Durga News:\n')
#         self.sports.sportsInfo()
#         print()
#         self.movie.movieInfo()
#         print()
#         self.politics.politicsInfo() 
#         print()
#         print('End of news channel....')
# d=DurgaNews()
# d.getTotalInfo()

