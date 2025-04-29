import gradio as gr
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import easyocr

reader = easyocr.Reader(["en"], gpu=False)

parked_vehicles = dict()

def parking_lot_ocr(uploaded_img: str, ntd_per_sec: int=10):
    results = reader.readtext(uploaded_img, detail=0)
    entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
    entry_time_str = entry_time.strftime("%Y-%m-%d %H:%M:%S")
    car_plate = results[0]
    if car_plate not in parked_vehicles.keys():
        parked_vehicles[car_plate] = entry_time
        output_message =  f"""
        {car_plate} 歡迎光臨停車場！\n
        你的進場時間為 {entry_time_str}\n
        每秒鐘停車費為 {ntd_per_sec} 元
        """
    else:
        leaving_time = datetime.now(timezone.utc) + timedelta(hours=8)
        time_elapsed = leaving_time - parked_vehicles[car_plate]
        hr_elapsed = int(time_elapsed.total_seconds())
        charge_amount = hr_elapsed * ntd_per_sec
        output_message = f"""
        {car_plate} 再見！\n
        總停車時間為 {hr_elapsed} 秒鐘\n
        請支付 {charge_amount:,} 元
        """
    return output_message

demo = gr.Interface(
    fn=parking_lot_ocr,
    inputs=gr.Image(),
    outputs="text",
    title="小小停車場"
)

demo.launch()