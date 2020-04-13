"""

EDA of MTA data to determine best spots for 

"""

import pandas as pd

mta_test = pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_190330.txt")
mta_test.head()