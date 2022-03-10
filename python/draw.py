import pandas as pd
from plotnine import *

import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
from plotnine import *
from plotnine.data import mpg
import matplotlib.pyplot as plt

df = pd.read_csv('res-100.dat', sep="\s+", skiprows=1, usecols=[0, 1, 2, 3, 4], names=['m', 'p', '1', '2', '3'])
df = pd.melt(df, id_vars='p', value_vars=['1', '2', '3'], value_name="Nombre d'opérations", var_name="Stratégie")


(ggplot(mpg)
 + aes(x='class')
 + geom_bar(size=20)
 + coord_flip()  # flipping the x- and y-axes
 + labs(title='Number of Vehicles per Class', x='Vehicle Class', y='Number of Vehicles')  # customizing labels
 )

ggplot(df) + aes(x="p", y="Nombre d'opérations", group='Stratégie') + geom_line(aes(color='Stratégie'), size=1,
                                                                                alpha=0.5)