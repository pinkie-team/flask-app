from flask import Flask, request, jsonify
import datetime
import socket

app = Flask(__name__)


@app.route('/motion', methods=['POST'])
def detect_noise_by_motion():
    z = request.json['z']
    sensor = request.json['sensor']
    print(z, sensor)

    write_log_file(sensor, z, 'motion')
    return jsonify({'z': z, 'sensor': sensor})


@app.route('/sound', methods=['POST'])
def detect_noise_by_sound():
    volume = request.form['volume']
    sensor = request.form['sensor']
    crop = request.files['crop']

    print(request.form['volume'])
    print(request.form['sensor'])
    print(request.files['crop'])

    write_log_file(sensor, volume, 'sound')
    return jsonify({'volume': volume, 'sensor': sensor, 'filename': crop.filename})


@app.route('/effect/<effect_id>')
def effect_setting(effect_id):
    # 1: 波紋, 2: オノマトペ
    try:
        _ = int(effect_id)
    except ValueError:
        return jsonify('idは数字にする必要があります')

    processingHost = "127.0.0.1"  # Processingで立ち上げたサーバのIPアドレス
    processingPort = 10002  # Processingで設定したポート番号

    name = ''
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketClient.connect((processingHost, processingPort))

    if effect_id == '1':
        name = 'normal_hamon'
    elif effect_id == '2':
        name = 'onomatopoeia'

    socketClient.send(effect_id.encode('utf-8'))
    return jsonify({'id': effect_id, 'name': name})


def write_log_file(sensor, value, algorithm):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y/%m/%d %H:%M:%S")
    file_path = 'log/{}_{}.csv'.format(algorithm, sensor)

    file = open(file_path, 'a')

    if len(open(file_path).readlines()) == 0:
        file.write('{},{},{}'.format(now_str, sensor, value))

    file.close()


if __name__ == '__main__':
    app.run(debug=True)
