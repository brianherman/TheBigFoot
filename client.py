from urllib import request, parse
from .serialization import dict_to_xml, xml_to_dict

# encoding: utf-8

#from https://stackoverflow.com/questions/18175489/sending-soap-request-using-python-requests
def call(url="", headers = {'content-type': 'text/xml'}, encoding="utf-8", document={}, modify_request=None):
    doctype = f"<?xml version="1.0" encoding="{encoding}"?>"
    header =  f"<SOAP-ENV:Header/>"
    envelope = f"""<SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/" 
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
                <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
            </SOAP-ENV:Envelope>"""

    if modify_request: body = modify_request(body)
    data = parse.urlencode(<your data dict>).encode()
    request =  request.Request(url, data=data) # this will make the method "POST"
    response = request.urlopen(request)

    return xml_to_dict(response)
