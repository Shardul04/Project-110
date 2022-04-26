import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
print("population mean : ",population_mean)

def randomsetofmean(counter):
    data_set = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

def showfig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("sampling mean: ", mean)
    fig = ff.create_distplot([df],["sample reading time"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'MEAN'))
    fig.show()



def setup():
    meanlist = []
    for i in range(0,100):
        setofmeans = randomsetofmean(30)
        meanlist.append(setofmeans)
    showfig(meanlist)

setup()