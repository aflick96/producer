import random
import string
import pandas as pd
import datetime
import os

def generateRandomString(length = 10):
    # generate random alphanumerical characters of length
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generateDataSet():
    #define out directory
    current_directory = os.path.dirname(__file__)

    print(current_directory)

    output_directory = os.path.join(current_directory, '../output')

    print(output_directory)

    # create output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # generate new data set and timestamp of completion
    dataSet = [generateRandomString() for _ in range(10000)]
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # output timestamp to txt
    with open(os.path.join(output_directory, 'timestamp.txt'), 'w') as f:
        f.write(timestamp)

    # output to csv
    df = pd.DataFrame(dataSet, columns=['data'])
    df.to_csv(os.path.join(output_directory, 'db_data.csv'), index=False)


if __name__ == '__main__':
    generateDataSet()