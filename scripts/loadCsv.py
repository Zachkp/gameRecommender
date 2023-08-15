import csv

videoGameList = []


def loadCsv(file):
    videoGameList.clear()
    with open(file, 'r') as videoGames:
        gameData = csv.reader(videoGames, delimiter=',', quotechar='"')
        # next(gameData) # NOT SURE IF I NEED THIS
        for game in gameData:
            url = game[0]
            typeOfPkg = game[1]
            name = game[2]
            description = game[3]
            recentReviews = game[4]
            allReviews = game[5]
            releaseDate = game[6]
            developer = game[7]
            publisher = game[8]
            popularTags = game[9]

            thisGame = VideoGames(url, typeOfPkg, name, description, recentReviews, allReviews, releaseDate, developer,
                                  publisher, popularTags)
            videoGameList.append(thisGame)


class VideoGames:
    def __init__(self, url, typeOfPkg, name, desSnippet, recentReviews, allReviews,
                 releaseDate, developer, publisher, popularTags):
        self.url = url
        self.types = typeOfPkg
        self.name = name
        self.desSnippet = desSnippet
        self.recentReviews = recentReviews
        self.allReviews = allReviews
        self.releaseDate = releaseDate
        self.developer = developer
        self.publisher = publisher
        self.popularTags = popularTags


def returnAll():
    for game in videoGameList:
        print(game)

