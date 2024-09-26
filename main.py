# pip install ultralytics

from ultralytics import YOLO

# modelos
model_detect = YOLO('yolov8n.pt')
model_segment = YOLO('yolov8n-seg.pt')
model_keypoints = YOLO('yolov8n-pose.pt')

# é possível passar links de vídeos também
results = model_keypoints.track(source="C:/Users/maria/CODIGOS/YOLO/rastreamentoObjetos/36510-411342239_small.mp4", save=True)
