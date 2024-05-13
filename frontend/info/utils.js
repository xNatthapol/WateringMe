// Fetch data from url
export async function fetchData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}

// Get Current date
export function getCurrentDateFormatted() {
  const today = new Date();
  const year = today.getFullYear();
  const month = (today.getMonth() + 1).toString().padStart(2, "0");
  const day = today.getDate().toString().padStart(2, "0");
  return `${year}-${month}-${day}`;
}

// Calculate Optimal dtick
export function calculateOptimalDtick(minValue, maxValue) {
  const range = maxValue - minValue;
  if (range <= 10) {
    return 1;
  } else if (range <= 20) {
    return 2;
  } else if (range <= 40) {
    return 5;
  } else if (range <= 60) {
    return 7;
  } else {
    return 10;
  }
}

// Calculate Axis Padding
export function calculateAxisPadding(minValue, maxValue) {
  const range = maxValue - minValue;
  let padding;

  if (range <= 10) {
    padding = 1;
  } else if (range <= 20) {
    padding = 2;
  } else if (range <= 40) {
    padding = 5;
  } else if (range <= 60) {
    padding = 7;
  } else {
    padding = 10;
  }

  return {
    adjustedMin: minValue - padding,
    adjustedMax: maxValue + padding,
  };
}
