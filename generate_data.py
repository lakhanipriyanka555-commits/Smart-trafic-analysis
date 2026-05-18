import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

roads = [
    "MG Road", "Brigade Road", "Outer Ring Road", "Hosur Road",
    "Bannerghatta Road", "Old Airport Road", "Whitefield Road", "Electronic City Road"
]

def generate_traffic_data(days=30):
    records = []
    start_time = datetime(2024, 4, 1, 0, 0, 0)

    for day in range(days):
        for hour in range(24):
            for road in roads:
                current_time = start_time + timedelta(days=day, hours=hour)

                # Simulate peak hours
                if 8 <= hour <= 10 or 17 <= hour <= 20:
                    base_count = random.randint(180, 350)
                    density_factor = random.uniform(0.7, 1.0)
                elif 11 <= hour <= 16:
                    base_count = random.randint(80, 180)
                    density_factor = random.uniform(0.4, 0.7)
                elif 21 <= hour <= 23 or 6 <= hour <= 7:
                    base_count = random.randint(40, 100)
                    density_factor = random.uniform(0.2, 0.45)
                else:
                    base_count = random.randint(5, 40)
                    density_factor = random.uniform(0.05, 0.2)

                # Road-specific multipliers
                road_multipliers = {
                    "MG Road": 1.3,
                    "Brigade Road": 1.25,
                    "Outer Ring Road": 1.4,
                    "Hosur Road": 1.1,
                    "Bannerghatta Road": 1.0,
                    "Old Airport Road": 0.95,
                    "Whitefield Road": 1.15,
                    "Electronic City Road": 1.2
                }

                vehicle_count = int(base_count * road_multipliers[road] + random.randint(-15, 15))
                vehicle_count = max(1, vehicle_count)

                traffic_density = round(density_factor + random.uniform(-0.05, 0.05), 2)
                traffic_density = max(0.01, min(1.0, traffic_density))

                if traffic_density < 0.35:
                    congestion_level = "Low"
                elif traffic_density < 0.65:
                    congestion_level = "Moderate"
                elif traffic_density < 0.85:
                    congestion_level = "High"
                else:
                    congestion_level = "Critical"

                # Pollution estimation (index 0-500 AQI scale proxy)
                pollution_index = round(vehicle_count * 0.8 + random.uniform(20, 60), 1)

                # Speed estimation (km/h)
                avg_speed = round(60 * (1 - traffic_density) + random.uniform(-5, 5), 1)
                avg_speed = max(5, avg_speed)

                records.append({
                    "Time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "Date": current_time.strftime("%Y-%m-%d"),
                    "Hour": hour,
                    "Day_of_Week": current_time.strftime("%A"),
                    "Road_Name": road,
                    "Vehicle_Count": vehicle_count,
                    "Traffic_Density": traffic_density,
                    "Congestion_Level": congestion_level,
                    "Avg_Speed_kmh": avg_speed,
                    "Pollution_Index": pollution_index,
                })

    df = pd.DataFrame(records)
    df.to_csv("traffic_data.csv", index=False)
    print(f"✅ Dataset generated: {len(df)} records saved to traffic_data.csv")
    return df

if __name__ == "__main__":
    df = generate_traffic_data(days=30)
    print(df.head())
    print(df.describe())
