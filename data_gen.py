import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random, os

random.seed(42); np.random.seed(42)

ROADS = ["MG Road","Brigade Road","Outer Ring Road","Hosur Road",
         "Bannerghatta Road","Old Airport Road","Whitefield Road","Electronic City Road"]

ROAD_MULT = {"MG Road":1.3,"Brigade Road":1.25,"Outer Ring Road":1.4,"Hosur Road":1.1,
             "Bannerghatta Road":1.0,"Old Airport Road":0.95,"Whitefield Road":1.15,"Electronic City Road":1.2}

def generate_and_cache(days=30, path="traffic_data.csv"):
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=["Time"])
    records = []
    start = datetime(2024, 4, 1)
    for d in range(days):
        for h in range(24):
            for road in ROADS:
                ts = start + timedelta(days=d, hours=h)
                if 8<=h<=10 or 17<=h<=20:
                    vc = int(random.randint(180,350)*ROAD_MULT[road])
                    td = round(random.uniform(0.65,1.0),2)
                elif 11<=h<=16:
                    vc = int(random.randint(80,180)*ROAD_MULT[road])
                    td = round(random.uniform(0.35,0.65),2)
                elif 6<=h<=7 or 21<=h<=23:
                    vc = int(random.randint(40,100)*ROAD_MULT[road])
                    td = round(random.uniform(0.15,0.35),2)
                else:
                    vc = int(random.randint(5,40)*ROAD_MULT[road])
                    td = round(random.uniform(0.02,0.15),2)
                vc = max(1, vc + random.randint(-10,10))
                td = min(1.0, max(0.01, td))
                cl = "Low" if td<0.35 else "Moderate" if td<0.65 else "High" if td<0.85 else "Critical"
                records.append({
                    "Time": ts, "Date": ts.date(), "Hour": h,
                    "Day_of_Week": ts.strftime("%A"), "Road_Name": road,
                    "Vehicle_Count": vc, "Traffic_Density": td,
                    "Congestion_Level": cl,
                    "Avg_Speed_kmh": round(max(5, 60*(1-td)+random.uniform(-5,5)),1),
                    "Pollution_Index": round(vc*0.8+random.uniform(20,60),1),
                })
    df = pd.DataFrame(records)
    df.to_csv(path, index=False)
    return df
