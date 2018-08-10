from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)


@app.route('/')
def detect_noise():
    z = request.args.get('z')
    sensor = request.args.get('sensor')
    print(z, sensor)

    write_log_file(sensor, z)
    return jsonify({'z': z, 'sensor': sensor})


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
