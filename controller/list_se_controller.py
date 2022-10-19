from flask import Blueprint,Response, request
import json

from service.list_se_service import ListSEService
from util.util_encoder import UtilEncoder

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/listse')
def get_list():  # put application's code here
    #return list_se_service.list.head

    return Response(status=200,
                    response=json.dumps(list_se_service.list.head
                                        , cls=UtilEncoder), mimetype="application/json")

@app_list_se.route('/listse',methods=['POST'])
def add_kid():
    data = request.json
    return Response(status=200,response=json.dumps({"kid adicionado":
                    list_se_service.add_kid(data)}),
                    mimetype="application/json")
@app_list_se.route('/listse',methods=['POST'])
def add_to_start():
    data = request.json
    return Response(status=200,response=json.dumps({"kid adicionado al inicio":
                    list_se_service.add_to_start(data)}),
                    mimetype="application/json")
@app_list_se.route('/listse',methods=['GET'])
def invert():
    data = request.json
    return Response(status=200,response=json.dumps({"message":
                    list_se_service.invert(data)}),
                    mimetype="application/json")
@app_list_se.route('/listse/byposition', methods=['POST'])
def save_by_position():
    data = request.json
    kidByPositionDTO = KidByPositionDTO(data['position'],data['kid'])
    return  Response(status=200,response=json.dumps({"message":
                    list_se_service.add_by_position(kidByPositionDTO)}),
                    mimetype="application/json")

@app_list_se.route('/listse/mixbygender')
def mix_by_gender():
    return Response(status=200, response=json.dumps({"message":
                 list_se_service.mix_by_gender()}),
                    mimetype="application/json")