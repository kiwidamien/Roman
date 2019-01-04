import pkg_resources
import pandas as pd


def load_emperors():
    """Return a dataframe about the 69 different Roman Emperors.

    Contains the following fields:
        index          68 non-null int64
        name           68 non-null object
        name.full      68 non-null object
        birth          63 non-null object
        death          68 non-null object
        birth.cty      51 non-null object
        birth.prv      68 non-null object
        rise           68 non-null object
        reign.start    68 non-null object
        reign.end      68 non-null object
        cause          68 non-null object
        killer         68 non-null object
        dynasty        68 non-null object
        era            68 non-null object
        notes          46 non-null object
        verif.who      11 non-null object

    """
    # This is a stream-like object. If you want the actual info, call
    # stream.read()

    stream = pkg_resources.resource_stream(__name__, 'data/emperors.csv')
    return pd.read_csv(stream, encoding='latin-1')


def causes_of_death():
    """Return a count of the ways Roman Emperors died."""
    return load_emperors()['killer'].value_counts()
