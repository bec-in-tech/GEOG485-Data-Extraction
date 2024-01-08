#-------------------------------------------------------------------------------
# Name:        Data Extraction for all Player Positions in
#              Multiple Countries Using Selections
# Project:     Lesson 3 Project 3
# Author:      Rebecca Ubalde
# Created:     9/20/2023
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.overwriteOutput = True

try:
    # Define the workspace
    arcpy.env.workspace = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData2"

    # Define the variables
    countryFC = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData2\Countries_WGS84.shp"
    playerFC = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData2\nhlrosters.shp"
    positions = ["C", "RW", "LW", "G", "D"]
    targetCountries = ["Sweden", "Denmark"]
    countryField = "CNTRY_NAME"
    positionField = "primaryPos"

    # Loop through the target countries list
    for targetCountry in targetCountries:
        try:
            # Create a variable for the SQL query for the current target country
            # Make this line flexible for use
            countryQuery = f"{countryField} = '{targetCountry}'"

            # Create an output file for the current target country feature class
            countryOutputFile = f"{targetCountry}.shp"

            # Create a feature layer for the current target country
            arcpy.MakeFeatureLayer_management(countryFC, "CountryLyr", countryQuery)

            # Write the feature layer into a new feature class
            arcpy.CopyFeatures_management("CountryLyr", countryOutputFile)

            # Loop through the target positions list
            for position in positions:
                try:
                    # Create a SQL query to select players of the current position
                    # Make this line flexible for use
                    playerQuery = f"{positionField} = '{position}'"

                    # Create an output file variable for players in the current country and position
                    outputFile = f"{targetCountry} - {position}.shp"

                    # Create a feature layer for players of the target positions
                    arcpy.MakeFeatureLayer_management(playerFC, "PlayerPositionsLyr", playerQuery)

                    # Select players from the current country using the SelectLayerByLocation operation
                    arcpy.SelectLayerByLocation_management("PlayerPositionsLyr", "WITHIN", "CountryLyr")

                    # Write the selected players into a new feature class (shapefile)
                    arcpy.CopyFeatures_management("PlayerPositionsLyr", outputFile)

                except Exception as e:
                    print(f"Failed to process position {position} in {targetCountry}: {str(e)}")

                # Clean up feature layer
                finally:
                    arcpy.Delete_management("PlayerPositionsLyr")

        except Exception as e:
            print(f"Failed to process country {targetCountry}: {str(e)}")

        # Clean up feature layer
        finally:
            arcpy.Delete_management("CountryLyr")

    # Print a success message when the shapefiles are created.
    print("Shapefiles for all players from Sweden & Denmark have been created.")

except Exception as e:
    print(f"Failed to execute: {str(e)}")
