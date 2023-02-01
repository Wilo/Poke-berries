import matplotlib.pyplot as plt
import numpy as np
from requests import session


def fetch_data(url: str) -> dict:
    req = session()
    response = req.get(url)
    return response.json()


def graph_data(data: dict) -> None:
    frequency_growth_time = data.get("frequency_growth_time")
    frequency_growth_time = {
        int(key): val
        for key, val in sorted(
            frequency_growth_time.items(), key=lambda ele: int(ele[0])
        )
    }
    if frequency_growth_time:
        frequency_growth_time_keys = list(frequency_growth_time.keys())
        frequency_growth_time_values = list(frequency_growth_time.values())
        plt.bar(
            frequency_growth_time_keys,
            frequency_growth_time_values,
            edgecolor="black",
            color="deepskyblue",
        )
        plt.xlabel("Growth Time")
        plt.ylabel("Frequency")
        plt.rcParams.update({"font.size": 22})
        plt.savefig("histogram.png")
    else:
        print("We can't get the data")
        return


if __name__ == "__main__":
    url = "http://localhost:8000/api/allBerryStats/"
    result = fetch_data(url)
    graph_data(result)
