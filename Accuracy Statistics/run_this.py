import json
from collections import defaultdict, Counter

# Read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Calculate the distribution of all y-axis values when x=spe in a line named Y
def calculate_y_values_at_x_spe(json_data):
    y_values_at_x_spe = []
    #i=0
    for line_data in json_data:
        if line_data.get("name", "") == "Y":
            #i=i+1
            #print(i)
            x_values = line_data.get("x", [])
            y_values = line_data.get("y", [])
            for x, y in zip(x_values, y_values):
                if x == 10000:
                # 1.1 - 50
                # 1.2 - 5000
                # 1.3 - 5000
                # 2.1 - 200
                # 2.2 - 5000
                # 2.3 - 5000
                # 3.1 - 500
                # 3.2 - 10000
                # 3.3 - 10000
                # 3.4 - 10000
                    y_values_at_x_spe.append(y)
    return y_values_at_x_spe

# Calculate the frequency of elements in a list
def calculate_frequency(data_list):
    counter = Counter(data_list)
    total_count = len(data_list)
    frequency = {key: count / total_count for key, count in counter.items()}
    return frequency

# main
def main():
    json_file_path = "3.3-multi-NOO-CRN-with-clock-synchronization.json"  # Please replace with your JSON file path
    # 1.1-max-max-without-clock.json
    # 1.2-max-max-with-clock.json
    # 1.3-max-max-with-clock.json
    # 2.1-CRD-CRC-without-clock.json
    # 2.2-CRD-CRC-with-clock.json
    # 2.3-CRD-CRC-with-clock.json
    # 3.1-multi-NOO-CRN-without-clock.json
    # 3.2-multi-NOO-CRN-without-synchronization.json
    # 3.3-multi-NOO-CRN-with-clock-synchronization.json
    # 3.4-multi-NOO-CRN-with-clock-synchronization.json

    data = read_json_file(json_file_path)
    y_values_at_x_spe = calculate_y_values_at_x_spe(data)

    # Print statistical results
    print("The distribution of values for all y-axis values when x=spe in a line named Y:")
    print(y_values_at_x_spe)

    print("Frequency of y values for all x=spe:")
    frequency = calculate_frequency(y_values_at_x_spe)
    print(frequency)

if __name__ == "__main__":
    main()


