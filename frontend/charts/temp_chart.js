import {
  fetchData,
  getCurrentDateFormatted,
  calculateOptimalDtick,
  calculateAxisPadding,
} from "./utils.js";

async function createTempChart() {
  try {
    const currentDate = getCurrentDateFormatted();

    // Fetch historical temperature data
    const historicalData = await fetchData(
      `http://127.0.0.1:8000/api/v1/weather/day/${currentDate}`,
    );

    // Determine the last timestamp from historical data
    const lastHistoricalDataTime = new Date(
      historicalData[historicalData.length - 1].ts,
    );
    lastHistoricalDataTime.setHours(lastHistoricalDataTime.getHours() + 1); // Set to next hour

    // Fetch forecast temperature data
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
        temper: historicalData[historicalData.length - 1].temper, // last historical temperature
      });
    }

    // Prepare filtered forecast data for plotting
    const forecastTrace = {
      x: filteredForecastData.map((data) => data.ts),
      y: filteredForecastData.map((data) => data.temper),
      type: "scatter",
      mode: "lines+markers",
      name: "Forecast Temperature",
      line: { color: "red" },
    };

    // Prepare historical data for plotting
    const historicalTrace = {
      x: historicalData.map((data) => data.ts),
      y: historicalData.map((data) => data.temper),
      type: "scatter",
      mode: "lines+markers",
      name: "Historical Temperature",
      line: { color: "blue" },
    };

    // Calculate min and max for Y-axis
    const allTemps = historicalData
      .concat(filteredForecastData)
      .map((data) => data.temper);
    const minValue = Math.min(...allTemps);
    const maxValue = Math.max(...allTemps);
    const optimalDtick = calculateOptimalDtick(minValue, maxValue);
    const { adjustedMin, adjustedMax } = calculateAxisPadding(
      minValue,
      maxValue,
    );

    // Plot layout configuration
    var layout = {
      title: "Temperature Visualization",
      xaxis: {
        title: "Timestamp",
        type: "date",
      },
      yaxis: {
        title: "Temperature (°C)",
        dtick: optimalDtick,
        range: [adjustedMin, adjustedMax],
      },
      autosize: true,
    };

    // Render the plot
    Plotly.newPlot("tempChart", [forecastTrace, historicalTrace], layout);
  } catch (error) {
    console.error("Error fetching or plotting data:", error);
  }
}

createTempChart();
