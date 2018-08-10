from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def detect_noise():
    z = request.args.get('z')
    sensor = request.args.get('sensor')
    print(z, sensor)

    return jsonify({'z': z, 'sensor': sensor})


if __name__ == '__main__':
    app.run(debug=True)
