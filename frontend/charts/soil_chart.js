import { fetchData, getCurrentDateFormatted } from "./utils.js";

async function createChart() {
  try {
    const currentDate = getCurrentDateFormatted();

    // Fetch historical soil moisture data
    const historicalData = await fetchData(
      `http://127.0.0.1:8000/api/v1/soil/day/${currentDate}`,
    );
    // Fetch forecast soil moisture data
    const forecastData = await fetchData(
      "http://127.0.0.1:8000/api/v1/soil/forecast",
    );

    // Add last historical point to forecast data for continuity
    if (historicalData.length > 0 && forecastData.length > 0) {
      forecastData.unshift({
        ts: historicalData[historicalData.length - 1].ts, // last historical timestamp
        sm: historicalData[historicalData.length - 1].sm, // last historical soil moisture
      });
    }

    // Prepare forecast data for plotting
    const forecastTrace = {
      x: forecastData.map((data) => data.ts),
      y: forecastData.map((data) => data.sm),
      type: "scatter",
      mode: "lines+markers",
      name: "Forecast Soil Moisture",
      line: { color: "green" },
    };

    // Prepare historical data for plotting
    const historicalTrace = {
      x: historicalData.map((data) => data.ts),
      y: historicalData.map((data) => data.sm),
      type: "scatter",
      mode: "lines+markers",
      name: "Historical Soil Moisture",
      line: { color: "black" },
    };

    // Calculate min and max for Y-axis
    const allValues = historicalData
      .concat(forecastData)
      .map((data) => data.sm);
    const minValue = Math.min(...allValues);
    const maxValue = Math.max(...allValues);

    // Plot layout configuration
    var layout = {
      title: "Soil Moisture Visualization",
      xaxis: {
        title: "Timestamp",
        type: "date",
      },
      yaxis: {
        title: "Soil Moisture (%)",
        dtick: 1.0,
        range: [minValue - 3, maxValue + 3],
      },
      autosize: true,
    };

    // Render the plot
    Plotly.newPlot("chart", [forecastTrace, historicalTrace], layout);
  } catch (error) {
    console.error("Error fetching or plotting data:", error);
  }
}

createChart();
