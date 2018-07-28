# camera_app.py
カメラからリアルタイムに画像を取得し、人の顔が検出されたら画面を切り替えるというプログラム。
アイディアはhttps://qiita.com/Hironsan/items/8ad9b11bcc0c618ec5e2を参考に。
dlibという機械学習のライブラリを用いて、顔の特徴点を取得する。
今回はライブラリにあらかじめ用意されている学習済みデータを利用。
以下のURL"http://dlib.net/files",から"shape_predictor_68_face_landmarks.dat.bz2"をDLして使う


