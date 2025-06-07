#  GPS Toll-Based System

This project simulates a GPS-based toll calculation system using Python. It combines data structures, pathfinding algorithms, GUI elements, and real-time animation to offer an engaging and educational demonstration of how tolls can be dynamically computed based on shortest routes between cities.

##  Features

*  **Shortest Path Calculation** using **Dijkstra’s Algorithm**.
*  **Dynamic Toll Calculation** based on distance traveled.
*  **Interactive GUI** built with **Tkinter** for user input and result display.
*  **Vehicle Animation** using **Pygame**, simulating travel across cities.
*  **Graph Visualization** using **NetworkX** and **Matplotlib**, with path highlights.

##  Tech Stack

* **Python**
* **NetworkX** – for graph representation and shortest path algorithms.
* **Pygame** – for animated vehicle movement.
* **Tkinter** – for GUI-based input/output.
* **Matplotlib** – to visualize the city graph.

##  Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ashutosh-Shukla-036/gps-toll-system.git
   cd gps-toll-system
   ```

2. **Install dependencies:**

   ```bash
   pip install networkx pygame matplotlib
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

## Usage

1. Enter the **Start Point** and **End Point** from the list of available cities (e.g., Mumbai, Delhi, Bangalore, etc.).
2. Click **"Calculate Toll"** to:

   * Find the shortest path.
   * Display the toll amount based on route distance.
   * Trigger vehicle animation across the map.
3. Optionally, click **"Show Graph"** to visualize the graph with highlighted path and edge weights.

## Testing

Unit tests for the pathfinding and toll logic are included:

```bash
python test_main.py
```

## Example Cities

Cities include: Mumbai, Delhi, Bangalore, Hyderabad, Ahmedabad, Chennai, Kolkata, Pune, Jaipur, Lucknow, and more.

##  Demo Video

Watch the working demo of the project here:  
📽️ [Click to Watch Video](https://drive.google.com/file/d/1mAAxkoQ-tZHMG64wLXAQi7HK-cdnajlt/view?usp=sharing)


## Contribution
Feel free to fork the repository, raise issues, or suggest improvements.
