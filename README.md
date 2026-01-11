![banner](https://github.com/EmikoHigashi/emikosh/blob/main/blob/banner.png)

# 📷 Simple Camera & Edge Detection for Kids
Two small Python programs that let kids play with their camera and learn how images work.
They can change numbers in the code and immediately see what happens.

## 1. ShowCamera.py
Shows the live camera image.
Press Q to quit.

✂️what kids can change⛏️
Flip the image
```bash
frame = cv2.flip(frame, 1)
```

Make the window smaller
```bash
cv2.resizeWindow("Press Q/q to close", 320, 240)
```

## 2. ShowEdge.py
Shows the camera image as edges (like a sketch).
Press Q to quit.

✂️what kids can change⛏️
Change the window name
```bash
cv2.namedWindow("My New Camera", cv2.WINDOW_NORMAL)
```

Change the blur size
```bash
blurred = cv2.GaussianBlur(gray, (3, 3), 1.0)
```

Make edges stronger or weaker
```bash
edges = cv2.Canny(blurred, 30, 120)
```

# ⭐How to Download⭐
Click the **“Code”** button and select **“Download ZIP”** to download all files as a ZIP archive.

### Requirements
- Python
- OpenCV 
```bash
pip install opencv-python
```


# 🌍
# 📷 子ども向け：かんたんなカメラ表示 & エッジ表示
カメラの画像をそのまま見たり、線だけの画像にしたりできる小さなプログラムです。
数字を変えるとすぐに結果が変わるので、遊びながら学べます。

## 1. ShowCamera.py
カメラの画像をそのまま表示します。
Qキーで終了。

### ✂️子どもが遊べるポイント ⛏️
- 左右反転してみる
- ウィンドウの大きさを変える

## 2. ShowEdge.py
カメラ画像を 線だけの絵（エッジ） にして表示します。
Qキーで終了。

### ✂️子どもが遊べるポイント ⛏️
- ウィンドウの名前を変える
- ぼかしの強さを変える
- 線の強さを変える

## 必要なもの
- Python
- OpenCV
```bash
pip install opencv-python
```



