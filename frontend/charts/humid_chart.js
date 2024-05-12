import {
  fetchData,
  getCurrentDateFormatted,
  calculateOptimalDtick,
  calculateAxisPadding,
} from "./utils.js";

async function createHumidChart() {
  try {
    const currentDate = getCurrentDateFormatted();

    // Fetch historical humidity data
    const historicalData = await fetchData(
      `http://127.0.0.1:8000/api/v1/weather/day/${currentDate}`,
    );

    // Determine the last timestamp from historical data
    const lastHistoricalDataTime = new Date(
      historicalData[historicalData.length - 1].ts,
    );
    lastHistoricalDataTime.setHours(lastHistoricalDataTime.getHours() + 1); // Set to next hour

    // Fetch forecast humidity data
    const forecastData = await fetchData(
      "http://127.0.0.1:8000/api/v1/weather/forecast",
    );

    // Filter forecast data to start from the hour after the last historical data timestamp
    const filteredForecastData = forecastData.filter(
      (data) => new Date(data.ts) >= lastHistoricalDataTime,
    );

    // Add last historical point to forecast data for continuity
    if (historicalData.length > 0 && filteredForecastData.length > 0) {
      filteredForecastData.unshift({
        ts: historicalData[historicalData.length - 1].ts, // last historical timestamp
        humid: historicalData[historicalData.length - 1].humid, // last historical humidity
      });
    }

    // Prepare filtered forecast data for plotting
    const forecastTrace = {
      x: filteredForecastData.map((data) => data.ts),
      y: filteredForecastData.map((data) => data.humid),
      type: "scatter",
      mode: "lines+markers",
      name: "Forecast Humidity",
      line: { color: "red" },
    };

    // Prepare historical data for plotting
    const historicalTrace = {
      x: historicalData.map((data) => data.ts),
      y: historicalData.map((data) => data.humid),
      type: "scatter",
      mode: "lines+markers",
      name: "Historical Humidity",
      line: { color: "blue" },
    };

    // Calculate min and max for Y-axis
    const allTemps = historicalData
      .concat(filteredForecastData)
      .map((data) => data.humid);
    const minValue = Math.min(...allTemps);
    const maxValue = Math.max(...allTemps);
    const optimalDtick = calculateOptimalDtick(minValue, maxValue);
    const { adjustedMin, adjustedMax } = calculateAxisPadding(
      minValue,
      maxValue,
    );

    // Plot layout configuration
    var layout = {
      title: "Humidity Visualization",
      xaxis: {
        title: "Timestamp",
        type: "date",
      },
      yaxis: {
        title: "Humidity (%)",
        dtick: optimalDtick,
        range: [adjustedMin, adjustedMax],
      },
      autosize: true,
    };

    // Render the plot
    Plotly.newPlot("humidChart", [forecastTrace, historicalTrace], layout);
  } catch (error) {
    console.error("Error fetching or plotting data:", error);
  }
}

createHumidChart();
