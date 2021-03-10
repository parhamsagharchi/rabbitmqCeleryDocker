import logging
import json

from imdb import IMDb

logging.basicConfig(
    filename='history.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d:%(process)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


def scrapper(id):
    id = str(id.rstrip())

    TITLE = None
    MOVIE_DATA = {}

    INSTANCE = IMDb()
    MOVIE_INFO = INSTANCE.get_movie(id.replace('tt', ''))

    MOVIE_DATA.update(
        {
            "_id": {
                "imdb": id
            }
        }
    )

    try:
        TITLE = MOVIE_INFO['title']
    except Exception as e:
        logging.error(
            'Error: {}, Problem: Title, ID: {}'.format(e, id)
        )
    finally:
        MOVIE_DATA.update(
            {
                "title": TITLE
            }
        )

    with open(f'data/info/{id}.json', 'w') as WriteFile1:
        json.dump(MOVIE_DATA, WriteFile1)
    WriteFile1.close()

    with open(f'data/main.json', 'a') as WriteFile2:
        WriteFile2.write(json.dumps(MOVIE_DATA))
        WriteFile2.write('\n')
    WriteFile2.close()
