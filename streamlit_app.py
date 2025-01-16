import cv2
from pyzbar.pyzbar import decode

# カメラの設定（0はデフォルトのカメラを意味します）
cap = cv2.VideoCapture(0)

while True:
    # フレームを取得
    ret, frame = cap.read()

    if not ret:
        print("カメラから画像を取得できませんでした")
        break

    # バーコードをデコード
    barcodes = decode(frame)

    # バーコードがあれば表示
    for barcode in barcodes:
        # バーコードのデータを取得
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type

        # バーコードのデータをコンソールに表示
        print(f"データ: {barcode_data} タイプ: {barcode_type}")

        # バーコードの位置を描画
        rect_points = barcode.polygon
        if len(rect_points) == 4:
            pts = [tuple(point) for point in rect_points]
            cv2.polylines(frame, [np.array(pts, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

        # バーコードのデータをテキストで表示
        cv2.putText(frame, f'{barcode_data} ({barcode_type})', (barcode.rect.left, barcode.rect.top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # フレームを画面に表示
    cv2.imshow("カメラの映像", frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラとウィンドウを解放
cap.release()
cv2.destroyAllWindows()
