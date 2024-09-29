import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generate_graph(data, days, email):
    current_time = datetime.now()
    filtered_data = []
    
    for entry in data:
        glucose_time = datetime.strptime(entry[2], '%Y-%m-%d %H:%M:%S')
        if current_time - glucose_time <= timedelta(days=days):
            filtered_data.append((glucose_time, entry[1]))
    
    if not filtered_data:
        print(f"No data found for the last {days} days.")
        return
    
    # Sort data by timestamp
    filtered_data.sort(key=lambda x: x[0])
    
    times = [entry[0] for entry in filtered_data]
    glucose_levels = [entry[1] for entry in filtered_data]

    # Plot the graph
    plt.figure(figsize=(10, 6))
    plt.plot(times, glucose_levels, marker='o', linestyle='-', color='b')
    plt.title(f"Blood Glucose Levels Over the Last {days} Days for {email}")
    plt.xlabel("Date")
    plt.ylabel("Blood Glucose Level (mg/dL)")
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Save the graph
    graph_file = f'graphs/{email}_glucose_graph_{days}_days.png'
    plt.savefig(graph_file)
    plt.close()
    print(f"Graph saved as {graph_file}")
