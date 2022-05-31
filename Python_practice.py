###***********************************************************###
#               Module 3 Python Practice                        #
###***********************************************************###

# counties = ["Arapahoe","Denver","Jefferson"]
# # if counties[1] == 'Denver':
# #     print(counties[1])

# if counties[3] != 'Jefferson':

#    print(counties[2])

# Membership Operators      in          not in
###***********************************************************###

counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")




# Logical Operators     and             or         not 
###***********************************************************###

## AND checks if both "arapahoe" and "el paso" are in counties

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")


# ## OR checks if at least one of them is in counties

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")


if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")



# count-controlled loop         for
###***********************************************************###

## For runs the look for a specified number of times


for county in counties:
    print(county)

## using index works as well

for i in range(len(counties)):  ## range will be integer 3, 
    print(counties[i])  ##the loop will run until all three counties are printed


# to pirnt a dictionary in voting_data use the standard format for iterating over the list of dictionaries
###***********************************************************###

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)