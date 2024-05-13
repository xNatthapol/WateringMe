import { fetchData } from "./utils.js";

async function updateWeather() {
  try {
    const weatherData = await fetchData(
      "http://127.0.0.1:8000/api/v1/weather/current",
    );
    document.getElementById("weatherIcon").src = weatherData.conic;
    console.log(weatherData.conic);
    document.getElementById("temperature").textContent =
      `Temperature: ${weatherData.temper} °C`;
    document.getElementById("humidity").textContent =
      `Humidity: ${weatherData.humid}%`;
    document.getElementById("condition").textContent =
      `Condition: ${weatherData.condi}`;
  } catch (error) {
    console.error("Failed to fetch weather data:", error);
  }
}

async function updateWatering() {
  try {
    const wateringData = await fetchData(
      "http://127.0.0.1:8000/api/v1/watering?soil_type=Loam",
    );
    document.getElementById("soilMoisture").textContent =
      `Soil Moisture: ${wateringData.sm.toFixed(2)}%`;
    document.getElementById("wateringSuggestion").textContent =
      `Suggestion: ${wateringData.suggest}`;
  } catch (error) {
    console.error("Failed to fetch watering data:", error);
  }
}

updateWeather();
updateWatering();
