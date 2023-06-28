import numpy as np
import pandas as pd

## Section 4.2 ##
Chapter = 4
Section = 2 
print("\n<Section {0}.{1}>\n".format(Chapter, Section))

# pandas_datareader 패키지의 DataReader 을 사용하면 일부 인터넷 사이트의 자료를 바로 pandas로 읽어들일 수 있다. 
# pandas_datareader 패키지는 판다스와 별도로 설치해야 한다. 다음은 pandas_datareader 패키지가 제공하는 인터넷 사이트의 예이다. 
# 일부 인터넷 사이트는 유료이므로 별도의 가입절차를 거쳐야 한다.
# 
# FRED
# Fama/French
# World Bank
# OECD
# Eurostat
# EDGAR Index
# TSP Fund Data
# Oanda currency historical rate
# Nasdaq Trader Symbol Definitions
# 
# 자세한 내용은 다음 웹사이트를 참조한다.
# https://pandas-datareader.readthedocs.io/en/latest/index.html