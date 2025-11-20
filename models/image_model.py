from nudenet import NudeDetector

detector = NudeDetector()

NSFW_CLASSES = [
    "FEMALE_GENITALIA_COVERED","BUTTOCKS_EXPOSED","FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED","MALE_BREAST_EXPOSED","ANUS_EXPOSED",
    "FEET_EXPOSED","BELLY_COVERED","FEET_COVERED","ARMPITS_COVERED",
    "ARMPITS_EXPOSED","BELLY_EXPOSED","MALE_GENITALIA_EXPOSED","ANUS_COVERED",
    "FEMALE_BREAST_COVERED","BUTTOCKS_COVERED"
]

def check_image(image_path):
    detections = detector.detect(image_path)

    if len(detections) == 0:
        return {"Image": image_path, "Status": "SAFE", "Reason": "No explicit content detected."}

    for item in detections:
        if item["class"] in NSFW_CLASSES and item["score"] > 0.45:
            return {"Image": image_path, "Status": "NSFW",
                    "Reason": f"Explicit content detected: {item['class']}",
                    "Score": round(item["score"],4)}

    return {"Image": image_path, "Status": "SAFE", "Reason": "Only non-sexual body parts detected."}
