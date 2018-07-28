# camera_app.py
カメラからリアルタイムに画像を取得し、人の顔が検出されたら画面を切り替えるというプログラム。
アイディアはhttps://qiita.com/Hironsan/items/8ad9b11bcc0c618ec5e2 を参考に。
dlibという機械学習のライブラリを用いて、顔の特徴点を取得する。
今回はライブラリにあらかじめ用意されている学習済みデータを利用。
以下のURLから"shape_predictor_68_face_landmarks.dat.bz2"をDLして使う

http://dlib.net/files

画面の切り替えについては、適当に用意したデスクトップ画像を表示することで表現。
テスト用にテキストエディタのスクリーンショットを用意した。
プログラムについては以下を参考に

https://qiita.com/ufoo68/items/b1379b40ae6e63ed3c79

https://www.kunihikokaneko.com/dblab/dlib/trydlib.html






