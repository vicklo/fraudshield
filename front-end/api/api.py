import pickle
from flask import Flask
from flask_cors import CORS, cross_origin
import pandas as pd
from flask import request

with open('../../logisticRegression.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def transformdata(insured_hobbies,incident_type,collision_type,incident_severity,auto_model,authorities_contacted):
    data = {
          "insured_hobbies_" + insured_hobbies: [1],
          "incident_type_" + incident_type: [1],
          "collision_type_" + collision_type: [1],
          "incident_severity_" + incident_severity: [1],
          "auto_model_" + auto_model: [1],
          "authorities_contacted_" + authorities_contacted: [1],
     }
    df = pd.DataFrame(columns=['insured_hobbies_base-jumping', 'insured_hobbies_basketball',
       'insured_hobbies_board-games', 'insured_hobbies_bungie-jumping',
       'insured_hobbies_camping', 'insured_hobbies_chess',
       'insured_hobbies_cross-fit', 'insured_hobbies_dancing',
       'insured_hobbies_exercise', 'insured_hobbies_golf',
       'insured_hobbies_hiking', 'insured_hobbies_kayaking',
       'insured_hobbies_movies', 'insured_hobbies_paintball',
       'insured_hobbies_polo', 'insured_hobbies_reading',
       'insured_hobbies_skydiving', 'insured_hobbies_sleeping',
       'insured_hobbies_video-games', 'insured_hobbies_yachting',
       'incident_type_Multi-vehicle Collision', 'incident_type_Parked Car',
       'incident_type_Single Vehicle Collision', 'incident_type_Vehicle Theft',
       'collision_type_?', 'collision_type_Front Collision',
       'collision_type_Rear Collision', 'collision_type_Side Collision',
       'incident_severity_Major Damage', 'incident_severity_Minor Damage',
       'incident_severity_Total Loss', 'incident_severity_Trivial Damage',
       'auto_model_93', 'auto_model_95', 'auto_model_3 Series',
       'auto_model_92x', 'auto_model_A3', 'auto_model_A5', 'auto_model_Accord',
       'auto_model_C300', 'auto_model_CRV', 'auto_model_Camry',
       'auto_model_Civic', 'auto_model_Corolla', 'auto_model_E400',
       'auto_model_Escape', 'auto_model_F150', 'auto_model_Forrestor',
       'auto_model_Fusion', 'auto_model_Grand Cherokee',
       'auto_model_Highlander', 'auto_model_Impreza', 'auto_model_Jetta',
       'auto_model_Legacy', 'auto_model_M5', 'auto_model_MDX',
       'auto_model_ML350', 'auto_model_Malibu', 'auto_model_Maxima',
       'auto_model_Neon', 'auto_model_Passat', 'auto_model_Pathfinder',
       'auto_model_RAM', 'auto_model_RSX', 'auto_model_Silverado',
       'auto_model_TL', 'auto_model_Tahoe', 'auto_model_Ultima',
       'auto_model_Wrangler', 'auto_model_X5', 'auto_model_X6',
       'authorities_contacted_Ambulance', 'authorities_contacted_Fire',
       'authorities_contacted_None', 'authorities_contacted_Other',
       'authorities_contacted_Police'], data=data)
    df = df.fillna(0)
    usedFeaturesInModel = ['insured_hobbies_camping','incident_severity_Trivial Damage' ,'auto_model_Wrangler','insured_hobbies_sleeping',
 'insured_hobbies_dancing', 'insured_hobbies_kayaking', 'auto_model_CRV',
 'incident_severity_Minor Damage', 'incident_severity_Total Loss',
 'insured_hobbies_golf', 'auto_model_Malibu', 'auto_model_Camry',
 'insured_hobbies_exercise', 'insured_hobbies_bungie-jumping',
 'auto_model_Grand Cherokee', 'insured_hobbies_yachting', 'auto_model_X6',
 'auto_model_Civic', 'incident_severity_Major Damage',
 'insured_hobbies_cross-fit','insured_hobbies_chess']
    return df[usedFeaturesInModel]
     

@app.route("/")
@cross_origin()
def helloWorld():
      return "Hello, cross-origin-world!"


@app.route("/checkfraud",methods=["post"])
def CheckFraud():
    insured_hobbies = request.form.get('insured_hobbies')
    incident_type = request.form.get('incident_type')
    collision_type = request.form.get('collision_type')
    incident_severity = request.form.get('incident_severity')
    auto_model = request.form.get('auto_model')
    authorities_contacted = request.form.get('authorities_contacted')

    transformedData = transformdata(insured_hobbies,incident_type,collision_type,incident_severity,auto_model,authorities_contacted)
    pred = model.predict(transformedData)
    print(pred[0])
    return {'Prediction' : str(pred[0])}

Flask.run(app)
