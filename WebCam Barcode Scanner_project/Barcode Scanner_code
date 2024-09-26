import cv2  # OpenCVライブラリをインポート。画像処理を行うために使用。
from pyzbar import pyzbar  # Pyzbarライブラリをインポート。バーコードのデコード（読み取り）を行うために使用。

# カメラキャプチャを開始 
cap = cv2.VideoCapture(0)

# カメラが正常に動作している間、無限ループを実行
while cap.isOpened():
    # フレーム（画像）をキャプチャ
    ret, frame = cap.read()

    # もしフレームが取得できなければ、ループを終了
    if not ret:
        break

    # フレーム内のバーコードを検出
    barcodes = pyzbar.decode(frame)

    # 検出されたバーコードごとに処理を実行
    for barcode in barcodes:
        # バーコードの位置（x, y, 幅w, 高さh）を取得
        (x, y, w, h) = barcode.rect
        # バーコードの位置に矩形を描画 (緑色, 枠線の太さ2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # バーコードのデータをUTF-8形式でデコードして文字列に変換
        barcode_value = barcode.data.decode('utf-8')

        # バーコードの値をコンソールに出力
        print("Barcode Value:", barcode_value)

        # フレーム内のバーコードの上に値を表示（緑色のテキスト）
        cv2.putText(frame, barcode_value, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # カメラのフレームをウィンドウに表示
    cv2.imshow("Barcode Scanner", frame)

    # 'Esc'キーが押されたらループを終了（キーコード27はEsc）
    if cv2.waitKey(1) & 0xFF == 27:
        break

# カメラとウィンドウを解放して終了
cap.release()
cv2.destroyAllWindows()

