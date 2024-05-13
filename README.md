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

-

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

Move into `app/` directory

```bash
cd app/
```

Run application

```bash
fastapi dev main.py
```

## Requirements

- Python version 3.10 - 3.12
- all requirements is stored in `backend/requirements.txt`
