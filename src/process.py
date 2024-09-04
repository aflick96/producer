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
    output_directory = os.path.join(current_directory, '../output')

    # create output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # generate new data set and timestamp of completion
    dataSet = [generateRandomString() for _ in range(10000)]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # output to csv
    df = pd.DataFrame(dataSet, columns=['data'])
    df.to_csv(os.path.join(output_directory, f'{timestamp}.csv'), index=False)

    # output timestamp to txt
    with open(os.path.join(output_directory, 'timestamp.txt'), 'w') as f:
        f.write(timestamp)

if __name__ == '__main__':
    generateDataSet()