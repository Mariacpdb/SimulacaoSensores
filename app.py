from flask import Flask, jsonify
import random
import time
import threading
import paho.mqtt.client as mqtt
import os

app = Flask(__name__)

# Dados simulados
simulated_data = {
    'temperature': None,
    'humidity': None,
    'forecast': None
}

# Função para prever chuva
def prever_chuva(temperatura, umidade):
    if temperatura < 20 and umidade > 70:
        return "Chuva prevista"
    else:
        return "Sem previsão de chuva"

# Função de simulação
def simular_clima():
    global simulated_data
    while True:
        temperatura = round(random.uniform(15, 35), 2)
        umidade = round(random.uniform(50, 100), 2)
        previsao = prever_chuva(temperatura, umidade)
        
        simulated_data = {
            'temperature': temperatura,
            'humidity': umidade,
            'forecast': previsao
        }
        
        # Publica os dados no MQTT
        client.publish("sensores/clima", str(simulated_data))
        print(f"Enviando dados: {simulated_data}")
        
        time.sleep(5)

# Callback para conexão MQTT
def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker MQTT com código {rc}")

# Endpoint da API Flask
@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify(simulated_data)

if __name__ == "__main__":
    # Configuração do cliente MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.hivemq.com", 1883, 60)

    client.loop_start()
    
    # Inicia a simulação em uma nova thread
    simulation_thread = threading.Thread(target=simular_clima)
    simulation_thread.daemon = True
    simulation_thread.start()
    
    # Executa o servidor Flask na porta especificada pela variável de ambiente PORT
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

   
