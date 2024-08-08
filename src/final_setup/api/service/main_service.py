import json
import plotly
from sqlalchemy.orm import Session
from typing import List, Optional
from ..repository.main_repository import MainRepository
from shapely.geometry import shape
import geopandas as gpd
import pandas as pd
from shapely import wkt
import plotly.express as px

class MainService:
    
    @staticmethod
    async def get_chloropleth_map(db: Session):
        lga_data=  await MainRepository.get_lga(db)
        accident_data = await MainRepository.get_accident_data(db)
        
        lga_df = pd.DataFrame(lga_data)
        
        lga_df['geometry'] = lga_df['geometry'].apply(wkt.loads)
 
        lga_gdf = gpd.GeoDataFrame(lga_df, geometry='geometry')

        accident_df = pd.DataFrame(accident_data,columns=['accident_no','lga_name'])
        
        # Reducing the size of the geometry object
        lga_gdf['geometry'] = lga_gdf['geometry'].apply(lambda geom: shape(geom).simplify(0.01))

        # Converting the datafame to json
        geojson_data = json.loads(lga_gdf.to_json())
        
        # Computing the total accidents
        grouped_LGA_df = accident_df.groupby("lga_name")['accident_no'].agg('count') \
            .rename('accident_count').reset_index() \
            .sort_values('accident_count', ascending = True).reset_index()
        
        # Creating the choropleth map
        fig = px.choropleth_mapbox(
            grouped_LGA_df,
            geojson=geojson_data,
            locations='lga_name',
            featureidkey="properties.lga_name",
            color='accident_count',
            color_continuous_scale=px.colors.sequential.Darkmint,
            range_color=[grouped_LGA_df['accident_count'].min(), grouped_LGA_df['accident_count'].max()],
            center={"lat": -37.8136, "lon": 144.9631},
            mapbox_style="open-street-map",
            zoom=7.0,
            # title="Geospatial Distribution of Bicycle Accidents in Melbourne",
            labels={'accident_count': 'Number of Accidents',
                    'lga_name': 'LGA Name'},
            hover_name=grouped_LGA_df['lga_name'].apply(lambda x: x.capitalize()),
            hover_data= {'lga_name': False},
            height= 650
        )
        
        gdpGraph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        return gdpGraph
    
    @staticmethod
    async def get_lga(db: Session):
        lga_data=  await MainRepository.get_lga(db)
        return lga_data