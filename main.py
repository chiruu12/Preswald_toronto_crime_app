from preswald import connect, get_df, table, text, plotly, checkbox, slider, alert
import pandas as pd
import plotly.graph_objects as go

connect()

main_df = get_df("major_crime_indicators")
neigh_map = get_df("neighbourhood_map")
mci_map = get_df("mci_map")
latlong_map = get_df("latlong_id_map")

main_df = main_df.merge(neigh_map, on="Neighbourhood_ID", how="left")

main_df = main_df.merge(mci_map, on="MCI_Category_ID", how="left")
main_df = main_df.merge(latlong_map, on="LatLong_ID", how="left")

main_df = main_df[["Year", "Neighbourhood", "MCI_Category", "Latitude", "Longitude"]]
text("## Toronto Crime Incidents Explorer (3D Map)")
text("Use the filters below to explore where, when, and what types of crimes are occurring in Toronto.")
available_years = sorted(main_df["Year"].unique())
available_mci = sorted(main_df["MCI_Category"].unique())

text("### Select MCI Categories")
assault = checkbox("Assault", default=True)
auto_theft = checkbox("Auto Theft", default=True)
break_enter = checkbox("Break and Enter", default=True)
robbery = checkbox("Robbery", default=True)
theft_over = checkbox("Theft Over", default=True)

selected_year = int(slider(
    label="Year",
    min_val=2014,
    max_val=2024,
    step=1,
    default=2014
))

selected_mcis = []
if assault: selected_mcis.append("Assault")
if auto_theft: selected_mcis.append("Auto Theft")
if break_enter: selected_mcis.append("Break and Enter")
if robbery: selected_mcis.append("Robbery")
if theft_over: selected_mcis.append("Theft Over")

filtered_df = main_df[
    (main_df["Year"] == selected_year) &
    (main_df["MCI_Category"].isin(selected_mcis))
]


if filtered_df.empty:
    alert("No data found for selected filters.")
else:
    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=filtered_df["Longitude"],
        lat=filtered_df["Latitude"],
        text=filtered_df["Neighbourhood"] + " - " + filtered_df["MCI_Category"],
        mode='markers',
        marker=dict(
            size=6,
            color=filtered_df["MCI_Category"].astype("category").cat.codes,
            colorscale='Turbo',
            colorbar_title="MCI Category",
            opacity=0.7
        )
    ))

    fig.update_layout(
        title=f"Toronto Crimes ({selected_year}) - Globe View",
        geo=dict(
            scope='north america',
            projection_type='orthographic',
            showland=True,
            landcolor='rgb(230, 230, 230)',
            showocean=True,
            oceancolor='rgb(200, 230, 255)',
            showcountries=True,
            lataxis=dict(range=[43.5, 44]),
            lonaxis=dict(range=[-80, -78.5])
        ),
        height=600
    )
    plotly(fig)
    table(filtered_df)