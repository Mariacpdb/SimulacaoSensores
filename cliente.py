import paho.mqtt.client as mqtt
import json


def menssagem_ativada (client, userdata, message):
    dados = json.loads(message.payload.decode())
    print(f'Dados recebidos: {dados}')
    
   
    if dados['temperatura'] > 45:
        print("Alerta: Temperatura elevada!")


broker = 'localhost'
port = 1883
topic = 'sensores/energiasolar'


client = mqtt.Client()
client.on_message = menssagem_ativada
client.connect(broker, port)
client.subscribe(topic)


client.loop_forever()
