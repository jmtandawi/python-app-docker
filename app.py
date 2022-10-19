# libraries to be imported
from flask import Flask, render_template
from urllib.request import urlopen
import psutil, os, requests, json

app = Flask(__name__)

@app.route("/home")
def hello_world():
    # sample
    return 'Hello, world!'

@app.route("/process")
def list_processs():
    listPIDProcess = psutil.pids()
    stringPIDName = ""
    dictProcess = dict()
    # loop to create dictionary based on PID and CPU Utilization
    # limitations: too many PID can cause slowdown
    for i in listPIDProcess:
        process = psutil.Process(i)
        # process name to be added in /etc
        processName = process.name()
        stringPIDName += processName + "\n"
        processCPU = (process.cpu_percent(interval=1.0))
        addDictionary(dictProcess, process, processCPU)
    # write configuration file
    textfile = open('pid.conf', 'w')
    textfile.write(stringPIDName)
    textfile.close()
    # add newline and move to /etc
    os.system("sed 's/\\n/\/g' pid.conf")
    os.system("mv pid.conf /etc")
    # return html file to application
    return render_template('process.html', dictProcess=dictProcess)        
def addDictionary(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value) 

@app.route("/data")
def get_data():
    # create dictionary based on link:view_count key pair
    dictionaryView = dict()
    # parse website
    r = requests.get('https://api.stackexchange.com/2.2/search?intitle=grafana&site=stackoverflow')
    jsonRaw = json.loads(r.text)
    r.close()
    # get viewcount and url through parsing json file
    items = jsonRaw["items"]
    jsonLength = len(items)
    # loop through all of the json records based on json length
    for i in range(jsonLength-1):
        data = items[i]
        addDictionary(dictionaryView, data['link'], data['view_count'])
    # sort key-pair dictionary descending
    sortedView = dict(sorted(dictionaryView.items(), key=lambda item: item[1], reverse=True))
    # remove values that are not in top 10 of view count
    while(len(sortedView) != 10):
        sortedView.popitem()
    return render_template('data.html', sortedView=sortedView)   
def addDictionary(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)     



