from src.fileloader import processfiles


def extractdata():
    processfiles('./data/raw/mongo/mongo_3_10_90', './data/clean/mongo/3_10_90_load.csv', 'load')
    processfiles('./data/raw/mongo/mongo_3_50_50', './data/clean/mongo/3_50_50_load.csv', 'load')
    processfiles('./data/raw/mongo/mongo_5_10_90', './data/clean/mongo/5_10_90_load.csv', 'load')
    processfiles('./data/raw/mongo/mongo_5_50_50', './data/clean/mongo/5_50_50_load.csv', 'load')

    processfiles('./data/raw/redis/redis_3_10_90', './data/clean/redis/3_10_90_load.csv', 'load')
    processfiles('./data/raw/redis/redis_3_50_50', './data/clean/redis/3_50_50_load.csv', 'load')
    processfiles('./data/raw/redis/redis_5_10_90', './data/clean/redis/5_10_90_load.csv', 'load')
    processfiles('./data/raw/redis/redis_5_50_50', './data/clean/redis/5_50_50_load.csv', 'load')


if __name__ == '__main__':
    extractdata()
