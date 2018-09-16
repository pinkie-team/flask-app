# flask-app

#### エンドポイント
127.0.0.1で立ち上げた場合
```
URL: /motion
Method: POST
Request: {'z': '0.357678', 'sensor': '1'}
```

```
URL: /sound
Method: POST
Request: {'volume': '-0.83631164', 'sensor': '1', 'crop': crop.m4a}
※volumeは0に近いほど大きい音。
※multipartFormDataを使用すること。
```

```
URL: /effect/<effect_id>
Method: GET
ex.) http://127.0.0.1/effect/1
```
