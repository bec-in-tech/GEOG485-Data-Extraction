#-------------------------------------------------------------------------------
# Name:        Data Extraction Using Selections and Cursors
# Project:     Lesson 3 Project 3
# Author:      Rebecca Ubalde
# Created:     9/20/2023
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.overwriteOutput = True

try:
    # Define the workspace
    arcpy.env.workspace = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData"

    # Define the variables
    countryFC = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData\Countries_WGS84.shp"
    playerFC = r"C:\PSU\Geog485_FA23\Lesson3Project\ProjectData\nhlrosters.shp"
    positions = ["C", "RW", "LW"]
    targetCountry = "Sweden"
    countryField = "CNTRY_NAME"
    positionField = "primaryPos"

    # Create a variable for the SQL query for Sweden
    # Make this line flexible for use
    countryQuery = f"{countryField} = '{targetCountry}'"

    # Create an output file for the Sweden feature class
    countryOutputFile = "Sweden.shp"

    # Create a feature layer for the target country (Sweden)
    arcpy.MakeFeatureLayer_management(countryFC, "SwedenLyr", countryQuery)

    # Write the feature layer into a new feature class
    arcpy.CopyFeatures_management("SwedenLyr", countryOutputFile)

    # Loop through the target positions list
    for position in positions:
        try:
            # Create a SQL query to select players of the current position
            # Make this line flexible for use
            playerQuery = f"{positionField} = '{position}'"

            # Create an output file variable for players in the current country and position
            outputFile = f"{position}.shp"

            # Create a feature layer for players of the target positions
            arcpy.MakeFeatureLayer_management(playerFC, "PlayerPositionsLyr", playerQuery)

            # Select players from the current country using the SelectLayerByLocation operation
            arcpy.SelectLayerByLocation_management("PlayerPositionsLyr", "WITHIN", "SwedenLyr")

            # Write the selected players into a new feature class (shapefile)
            arcpy.CopyFeatures_management("PlayerPositionsLyr", outputFile)

            # Add new fields "height_cm" and "weight_kg" to each new output shapefiles
            arcpy.AddField_management(outputFile, "height_cm", "DOUBLE")
            arcpy.AddField_management(outputFile, "weight_kg", "DOUBLE")

            # Calculate the "height_cm" and "weight_kg" field using string slicing
            # then convert to metric units using Update Cursor
            with arcpy.da.UpdateCursor(outputFile, ["height", "height_cm", "weight", "weight_kg"]) as cursor:
                for row in cursor:

                    # Get the height string from tuple
                    heightString = row[0]

                    # Remove the double quotes found at the end of the height string
                    heightString = heightString.replace('"', '')

                    # Use the string slicing notation to split the string into feet and inches
                    # " ' " will be used as the delimiter for the split
                    ftString, inString = heightString.split("'")

                    # Convert feet and inches to integers
                    feet = int(ftString)
                    inches = int(inString)

                    # Calculate the height in inches
                    heightIN = feet * 12 + inches

                    # Convert height to metric units (cm)
                    heightCM = heightIN * 2.54

                    # Update the "height_cm" field with new conversions
                    row[1] = heightCM
                    cursor.updateRow(row)

                    # Get the weight in pounds from tuple
                    weightLB = row[2]

                    # Convert weight to metric units (kg)
                    weightKG = weightLB * 0.453592

                    # Update the "weight_kg" field with new conversions
                    row[3] = weightKG
                    cursor.updateRow(row)

        except Exception as e:
            print(f"Failed to process position {position}: {str(e)}")

        # Clean up feature layer and cursor
        finally:
            arcpy.Delete_management("PlayerPositionsLyr")
            del cursor

    # Print a success message when the shapefiles are created.
    print("Shapefiles for forward players from Sweden have been successfully created.")

except Exception as e:
    print(f"Failed to execute: {str(e)}")

# Clean up the feature layer for Sweden
finally:
    arcpy.Delete_management("SwedenLyr")