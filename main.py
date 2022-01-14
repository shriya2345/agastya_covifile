from flask import Flask,request,jsonify
# from data import data
import csv

app = Flask(__name__)

#add code to open csv file and convert data to list

with open('covid-variants.csv', encoding='utf8') as file:
    data = csv.reader(file)
    listData = list(data)
    # print(listData)
    covidVar = listData[1:]  #this is to pop header

@app.route("/")
def index():
    return jsonify({
        "data":covidVar,
        "message":"Successful"
    }),200

@app.route("/variant", methods=['POST']) #added post request method
def variant():
    name = request.args.get('variant')
    v_data = next(item for item in covidVar if item[2]== name) #looking for variant name in list
    return jsonify({
        "data":v_data,
        "message":"Successful"
    }),200

if __name__ == "__main__":
    app.run()