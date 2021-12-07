import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("C:/Users/Administrator/Desktop/Python 2/classes/110/data.csv")
data = df["temp"].tolist()
populationMean = statistics.mean(data)
dev = statistics.stdev(data)
print("population mean:", populationMean)
print("standard derivation:", dev)




#mean and stdv of 100 data points
#dataset = []
#for i in range (0,100):
    #randomindex = random.randint(0,len(data))
    #value = data[randomindex]
    #dataset.append(value)

#mean = statistics.mean(dataset)
#stdv = statistics.stdev(dataset)
#print("sample mean:", mean)
#print("standard derivation of sample:", stdv)

def randomMean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def showFig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines", name = mean))



    fig.show()

def setup ():
    meanlist = []
    for i in range(0,1000):
        setOfmeans = randomMean(100)
        meanlist.append(setOfmeans)

    showFig(meanlist)
    mean = statistics.mean(meanlist)
    print("mean of sampling distribution:",mean)

setup()

def stdev ():
    meanlist = []
    for i in range (0,1000):
        setOfMeans = randomMean(100)
        meanlist.append(setOfMeans)

    standardDev = statistics.stdev(meanlist)
    print("Standard Derivation:" , standardDev)

stdev()
