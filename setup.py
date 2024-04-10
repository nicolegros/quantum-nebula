from src.fileloader import processfiles


def extractdata():
    # Mongo
    processfiles('./data/raw/mongo/mongo_3_10_90', './data/clean/mongo/load_3_10_90.csv', 'load')
    processfiles('./data/raw/mongo/mongo_3_50_50', './data/clean/mongo/load_3_50_50.csv', 'load')
    processfiles('./data/raw/mongo/mongo_5_10_90', './data/clean/mongo/load_5_10_90.csv', 'load')
    processfiles('./data/raw/mongo/mongo_5_50_50', './data/clean/mongo/load_5_50_50.csv', 'load')

    processfiles('./data/raw/mongo/mongo_3_10_90', './data/clean/mongo/run_3_10_90.csv', 'run')
    processfiles('./data/raw/mongo/mongo_3_50_50', './data/clean/mongo/run_3_50_50.csv', 'run')
    processfiles('./data/raw/mongo/mongo_5_10_90', './data/clean/mongo/run_5_10_90.csv', 'run')
    processfiles('./data/raw/mongo/mongo_5_50_50', './data/clean/mongo/run_5_50_50.csv', 'run')

    # Redis
    processfiles('./data/raw/redis/redis_3_10_90', './data/clean/redis/load_3_10_90.csv', 'load')
    processfiles('./data/raw/redis/redis_3_50_50', './data/clean/redis/load_3_50_50.csv', 'load')
    processfiles('./data/raw/redis/redis_5_10_90', './data/clean/redis/load_5_10_90.csv', 'load')
    processfiles('./data/raw/redis/redis_5_50_50', './data/clean/redis/load_5_50_50.csv', 'load')

    processfiles('./data/raw/redis/redis_3_10_90', './data/clean/redis/run_3_10_90.csv', 'run')
    processfiles('./data/raw/redis/redis_3_50_50', './data/clean/redis/run_3_50_50.csv', 'run')
    processfiles('./data/raw/redis/redis_5_10_90', './data/clean/redis/run_5_10_90.csv', 'run')
    processfiles('./data/raw/redis/redis_5_50_50', './data/clean/redis/run_5_50_50.csv', 'run')


if __name__ == '__main__':
    extractdata()
