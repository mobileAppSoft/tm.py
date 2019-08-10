from datetime import datetime

DATETIME_TMP = '%Y-%m-%d %H:%M:%S.%f'


def formatTSP(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime(DATETIME_TMP)[:-3] if timestamp else datetime.utcnow().strftime(DATETIME_TMP)[:-3]
