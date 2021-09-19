# Hand Tracking

## [Youtube 1](https://www.youtube.com/watch?v=NZde8Xt78Iw)
- [MediaPipe](https://google.github.io/mediapipe/) (developed by Google)

### Hand Landmarks

### Opencv
```python
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

- あくまでも draw などは img を更新するイメージか
- 実際に更新を行うのは、cv2.imshow() の部分


### Requirements
- module
  - opencv-python
  - mediapipe
