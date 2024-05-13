# WateringMe

## Member

Natthapol Sermsaran 6510545527 Software engineering, Kasetsart University<br/>
Natthadit Lertpisanwut 6510545403 Software engineering, Kasetsart University

## Overview

WateringMe is home plant monitoring application designed to promote the way
gardener water by analyzing past and current data of soil moisture and weather
condition. Through data visualization, it presents historical and real-time
data trends. Using multiple linear regression, it forecasts soil moisture for
the next hour from many factors such as humidity, temperature and precipitation
, while also computing Potential Evapotranspiration (PET) to estimate water
loss from soil, mm/day.

## Features

### API:

- Hourly current soil moisture level
- All predicted soil moisture level in the rest of the current day
- Soil moisture level at specified date and hour
- Soil moisture level at the specified hour
- Hourly current weather data
- All forecast weather data at the current day
- Weather data at specified date and hour
- Weather data at the specified date
- Potential Evapotranspiration (PET) at the current day
- Watering suggestion

### Data visualization

Our visualized application provides the current temperature, 
humidity and soil moisture data. It also displays a line graph
to represent historical and forecast data.

<img width="1440" alt="image" src="https://github.com/xNatthapol/WateringMe/assets/115071646/02738fa7-3089-45ba-a913-c91bb6e87b1a">

## Tools & Libraries

- Python version 3.10 - 3.12
- FastAPI
- Plotly
- all requirements is stored in `backend/requirements.txt`

## Installation

### Clone the repository

```bash
git clone https://github.com/xNatthapol/WateringMe.git
```

Move into the project repository and `/backend` directory

```bash
cd WateringMe/backend
```

### Create a Virtual Environment

```bash
python -m venv venv
```

> If python cannot work well, use `python3` instead

Activate the Virtual Environment

- MacOS or Linux

```bash
source venv/bin/activate
```

- Window

```cmd
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env` file and copy the content from `.env.example` file

- MacOS or Linux

```bash
 cp .env.example .env
```

- Windows

```cmd
copy .env.example .env
```

### Run the tests

```bash
python -m unittest
```

> If python cannot work well, use `python3` instead
> If `python -m unittest` not work you can try to add `discover -s tests`

```bash
python -m unittest discover -s tests
```

### Run the application

#### Run the backend application

Move into `app/` directory

```bash
cd app/
```

Run backend application on localhost port 8000

```bash
fastapi dev main.py
```

#### Run the frontend application

Assume you are in `app/` directory

```bash
cd ../../frontend
```

Run frontend application on localhost port 3000

```bash
python -m http.server 3000
```

And go to `http://127.0.0.1:3000/dashboard.html`
