# Toronto Crime Incidents Explorer (3D Map)

An interactive visualization app built with Preswald to explore Toronto crime data over time and geography.

## 🔍 Objective

To provide an intuitive and interactive way to explore major crime incidents across Toronto using 3D maps. The application helps understand when, where, and what type of crimes have occurred over the years.

## 🛠️ Data Preprocessing

We used the Toronto Major Crime Indicators dataset available [here]([https://open.toronto.ca/dataset/major-crime-indicators/](https://www.kaggle.com/datasets/mohammadbadi/crimes-in-toronto?select=major-crime-indicators.csv)). The raw dataset was merged with supporting datasets including:
- Neighbourhood ID mappings
- MCI category mappings
- Latitude/Longitude mappings

After merging, we reduced the size of the dataset by filtering down to essential columns:
- `Year`
- `Neighbourhood`
- `MCI_Category`
- `Latitude`
- `Longitude`

This reduced memory load and optimized the dataset for deployment.

## 🗺️ Interactive Mapping

To further reduce rendering load and enhance interactivity, we opted to visualize crime incidents using Plotly's 3D map capabilities. This allowed:
- Efficient filtering based on crime type and year
- Visual clarity with color-coded markers
- Better performance than loading full tabular datasets

## 🚀 Deployment

The app is will be deployed using **Preswald**, which allows rapid cloud or local deployment of interactive Python apps.

## 📌 Features

- Year slider (2014–2024)
- Category checkboxes for common crime types
- Interactive 3D map with neighborhood info
- Responsive filtering and table view

## 🧩 Tech Stack

- Python
- Pandas
- Plotly 
- Preswald CLI

