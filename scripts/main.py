import loadCsv
import loadCsvWithPandas


def main():
    # loadCsv.loadCsv('C:\\Users\\Zach\\PycharmProjects\\pythonProject3\\files\\steam_games.csv')
    # loadCsv.returnAll()
    print(loadCsvWithPandas.recommender("Factorio", loadCsvWithPandas.cos_similarity, loadCsvWithPandas.df2))


if __name__ == '__main__':
    main()
