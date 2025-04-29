import easyocr
# import cv2
# import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timezone
from datetime import timedelta

reader = easyocr.Reader(["en"], gpu=False)

parked_vehicles = dict()

def parking_lot_ocr(img_path: str, ntd_per_sec: int=10):
    results = reader.readtext(img_path, detail=0)
    entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
    entry_time_str = entry_time.strftime("%Y-%m-%d %H:%M:%S")
    car_plate = results[0]
    if car_plate not in parked_vehicles.keys():
        parked_vehicles[car_plate] = entry_time
        print(f" {car_plate} 歡迎光臨停車場！")
        print(f"你的進場時間為 {entry_time_str}")
        print(f"每分鐘停車費為 {ntd_per_sec} 元")
    else:
        leaving_time = datetime.now(timezone.utc) + timedelta(hours=8)
        time_elapsed = leaving_time - parked_vehicles[car_plate]
        hr_elapsed = int(time_elapsed.total_seconds())
        charge_amount = hr_elapsed * ntd_per_sec
        print(f"{car_plate} 再見！")
        print(f"總停車時間為 {hr_elapsed} 秒鐘")
        print(f"請支付 {charge_amount:,} 元")
        parked_vehicles.pop(car_plate, None)

parking_lot_ocr("data/car_plate_1.jpg")
print(parked_vehicles)
parking_lot_ocr("data/car_plate_1.jpg")



# results = reader.readtext(img_path, detail=0)
# entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
# # results = reader.readtext(img_path, detail=0)
# leaving_time = datetime.now(timezone.utc) + timedelta(hours=8)
# time_elapsed = leaving_time - entry_time
# print(entry_time)
# print(leaving_time)
# print(time_elapsed)
# print(int(time_elapsed.total_seconds()))

# reader = easyocr.Reader(["en"], gpu=False)

# img_path = "data/car_plate_1.jpg"
# results = reader.readtext(img_path, detail=0)
# # print(results)
# # print(results[0][0])
# x_points = []
# y_points = []
# for xi, yi in results[0][0]:
#     x_points.append(xi)
#     y_points.append(yi)
# left_top = (min(x_points), min(y_points))
# right_bottom = (max(x_points), max(y_points))
# print(left_top, right_bottom)
# img = cv2.imread(img_path)
# cv2.rectangle(img, left_top, right_bottom, (0, 255, 0), 5)
# plt.imshow(img)
# plt.show()


