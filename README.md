# GEOG485: NHL Player Extraction Tool

<b>Project Description:
<br>NHL Player Extraction Tool</b>

The NHL Player Extraction Tool is a Python script designed for data analysts working with NHL rosters. The tool assists in extracting player information based on country and playing position, while also converting height and weight measurements to metric units. This project aims to facilitate the team's preparation for the league draft by providing the team general manager with detailed insights into players born in a specific country and playing specific forward positions.

<b>Key features: </b>

1. Flexible Configuration: Users can easily customize the country and list of positions by editing a couple of lines of code at the top of the script. This flexibility allows the tool to be adapted for different scenarios and requirements.

2. Country-Based Extraction: The script processes a shapefile containing world country boundaries and another shapefile containing NHL player rosters. Users can specify the target country (e.g., Sweden) to extract player information based on their birth country.

3. Position-Specific Shapefiles: The tool generates separate shapefiles for each of the three forward positions (center, right wing, and left wing) within the specified country. This enables the team to focus on specific player positions during the draft preparation.

4. Metric Unit Conversion: The script enhances the extracted player information by adding two new numeric fields to the attribute table of the new shapefiles. These fields, "height_cm" and "weight_kg," store height in centimeters and weight in kilograms, respectively. The conversion is based on the provided imperial units (feet & inches and pounds).

5. Error Handling: The script incorporates error handling mechanisms to ensure robust execution. In case of any issues during the extraction process, informative error messages are printed, allowing users to identify and address potential problems.

6. Batch Processing for Multiple Countries: An extended version of the script is available for batch processing multiple countries simultaneously. Users can specify a list of target countries, and the tool will generate shapefiles for all players from each country based on their playing positions.

7. Usage: Users need to set the appropriate file paths for the country shapefile (Countries_WGS84.shp) and the NHL player roster shapefile (nhlrosters.shp). Additionally, the target country and list of positions can be easily adjusted by modifying the relevant variables at the beginning of the script. Execute the script to generate separate shapefiles for each forward position within the specified country, including height and weight in metric units.

![image](https://github.com/bec-in-tech/GEOG485-Data-Extraction/assets/120440399/cf50147f-9885-4003-8e3c-6fd1a5afb6fc)
