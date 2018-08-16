from flask import Flask, request, jsonify
import os
import datetime
import socket

app = Flask(__name__)


@app.route('/', methods=['GET'])
def detect_noise():
    z = request.args.get('z')
    sensor = request.args.get('sensor')
    print(z, sensor)

    write_log_file(sensor, z)
    return jsonify({'z': z, 'sensor': sensor})


@app.route('/effect/<effect_id>')
def effect_setting(effect_id):
    # 1: 波紋, 2: オノマトペ
    try:
        _ = int(effect_id)
    except ValueError:
        return jsonify('idは数値する必要があります')

    processingHost = "127.0.0.1"  # Processingで立ち上げたサーバのIPアドレス
    processingPort = 10002  # Processingで設定したポート番号

    name = ''
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((processingHost, processingPort))

    if effect_id == 1:
        name = 'normal_hamon'
    elif effect_id == 2:
        name = 'onomatopoeia'

    socketClient.send(effect_id.encode('utf-8'))
    return jsonify({'id': effect_id, 'name': name})


def write_log_file(sensor, z):
    os.makedirs('log', exist_ok=True)

    now = datetime.datetime.now()
    now_str = now.strftime("%Y/%m/%d %H:%M:%S")
    file_path = 'log/{}.csv'.format(sensor)

    file = open(file_path, 'a')

    if len(open(file_path).readlines()) == 0:
        file.write('{},{},{}'.format(now_str, sensor, z))

    file.close()


if __name__ == '__main__':
    app.run(debug=True)
