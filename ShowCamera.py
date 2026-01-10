import cv2

# ShowEdge.py
# カメラからフレームを取得してエッジを表示、Qキーで終了

def main():
    cap = cv2.VideoCapture(0)  # 0 はデフォルトカメラ
    if not cap.isOpened():
        print("カメラを開けませんでした。")
        return

    cv2.namedWindow("Press Q/q to close", cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("フレーム取得に失敗しました。")
                break

            # フレームを表示
            cv2.imshow("Press Q/q to close", frame)
            h, w = frame.shape[:2]
            cv2.resizeWindow("Press Q/q to close", w, h)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == ord('Q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()