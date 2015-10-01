#!/usr/bin/python

"""
viper.py
Data Science with python.

Author: Victor Green, vgreen@gds.org
Date: 09-30-2015

Goal: To create a universal template for data science workflow as it 
pertains to python. The purpose is to predifine as much boilerplate code
as possible subscribing to a functional programming paridigm allowing aspiring
and current data scientists to focus on data science while learning the particulars
of the python programming language. Use and modify this template as you see fit and please
fork this project on github. All improvements / suggestions are wellcome.
Many Thanks, Victor Green Data Engineer / Data Scientist
"""



#IMPORT NEEDED LIBRARIES

import sys
import getopt
import pygal




####BEGIN DATA PARSING AND CLEANING FUNCTIONS HERE
def get_parse_clean_data_as_csv_1( file_name ):
	"""PARSES CSV FILE INTO A SINGLE LIST THAT CONTAINS
	EACH ROW IN A SEPARATE LIST OF STRINGS CONTAINING EACH
	FIELD FOR THAT ROW. LIST OF LISTS
	"""

	with open( file_name, 'rU' ) as f:
		data = []
		for row in f:
			data.append( row.split(',') )

		return data


def convert_list_of_lists_to_list_of_dicts( k,values ):
	"""CONVERTS A LIST OF LISTS 
	TO A LIST OF DICTIONARIES CONTAINING
	USER SUPPLIED KEY VALUE PAIRS
	"""

	results = []

	for v in values:

		if len( k ) == 2:
			mydict = {k[0]:v[0],k[1]:v[1]}
			results.append(mydict)

		elif len( k ) == 3:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2]}
			results.append(mydict)

		elif len( k ) == 4:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3]}
			results.append(mydict)

		elif len( k ) == 5:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4]}
			results.append(mydict)

		elif len( k ) == 6:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4],k[5]:v[5]}
			results.append(mydict)

		elif len( k ) == 7:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4],k[5]:v[5],k[6]:v[6]}
			results.append(mydict)

		elif len( k ) == 8:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4],k[5]:v[5],k[6]:v[6],k[7]:v[7]}
			results.append(mydict)

		elif len( k ) == 9:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4],k[5]:v[5],k[6]:v[6],k[7]:v[7],k[8]:v[8]}
			results.append(mydict)

		elif len( k ) == 10:
			mydict = {k[0]:v[0],k[1]:v[1],k[2]:v[2],k[3]:v[3],k[4]:v[4],k[5]:v[5],k[6]:v[6],k[7]:v[7],k[8]:v[8],k[9]:v[9]}
			results.append(mydict)			

	return results
####END DATA PARSING AND CLEANING FUNCTIONS



####BEGIN DATA ANALYSIS FUNCTIONS HERE
def analyze_data_1( data ):
	"""PERFORMS 1ST LEG OF ANALYSIS
	AND RETURNS RESULTS AS A LIST OF TUPLES
	"""

	results = []

	for airline in data:

		avg_incidents = int( airline["incidents_85_99"] ) + int( airline["incidents_00_14"] ) / 30
		results.append( ( airline["airline"],avg_incidents) )

	return results
####END DATA ANALYSIS FUNCTIONS HERE



####BEGIN MACHINE LEARNING / DATA SCIENCE ALGORITHMS DEFINITIONS HERE
####END MACHINE LEARNING / DATA SCIENCE ALGORITHMS DEFINITIONS HERE



####BEGIN SAVE DATA TO FILE FUNCTIONS HERE
def save_data_1( data, output_file ):
	"""SAVES THE RESULTS OF YOUR
	ANALYSIS TO A FILE
	"""

	#CAN ALSO USE
	#FUNCTIONS
	#str( data )
	#repr( data )
	#INTERPOLATION
	#"%s" % ( data, )


	fo = open( output_file, "wb" )
	fo.write( str( data ) );
	fo.close()
####END SAVE DATA TO FILE FUNCTIONS



####BEGIN DATA VISUALIZATION FUNCTIONS HERE
def visualize_data_1( data,chart_name ):
	"""TAKES A LIST OF TUPLES
	CREATES A BAR CHART
	"""

	bar_chart = pygal.Bar()
	bar_chart.title = "Average Airline Incidents"

	for row in data:
		bar_chart.add(row[0],[ row[1] ])

	bar_chart.render_to_file(chart_name)
####END DATA VISUALIZATION FUNCTIONS



####BEGIN MAIN METHOD DEFINITION
def main( argv ):

	#DEFINE COMMAND LINE OPTIONS
	#SHOULD INITALIZE BECAUSE THESE
	#ARE OPTOINS HENCE OPTIONAL
	input_file = ''
	output_file = ''
	output_image = ''


	#PARSE COMMAND LINE OPTIONS
	#RAISE ERROR IF OPTION IS NOT VALID
	#OR IF REQUIRED ARGUMENT DOES FOLLOW OPTION
	try:
		opts, args = getopt.getopt( argv, "hi:o:v:",["help","inputfile=","outputfile=","outputimage="] )
	except getopt.GetoptError:
		print ''
		print 'viper.py -i <input_file> -o <output_file> -v <output_image>'
		print 'viper.py --inputfile <input_file> --outputfile <output_file> --outputimage <output_image>'
		print ''
		sys.exit(2)

	#LOOP THROUGH OPTIONS
	#SHOW HELP IF PASSED
	#OR SET OPTIONS 
	for opt, arg in opts:
		if opt == '-h' or opt == '--help':
			print ''
			print 'viper.py -i <input_file> -o <output_file> -v <output_image>'
			print 'viper.py --inputfile <input_file> --outputfile <output_file> --outputimage <output_image>'
			print ''
			sys.exit()

		#SHORT OPTION FORM OR LONG OPTION FORM 
		elif opt in ("-i","--inputfile"):
			input_file = arg
		elif opt in ("-o","--outputfile"):
			output_file = arg
		elif opt in ("-v","--outputimage"):
			output_image = arg


	#CHECK TO SEE IF ANY (REQUIRED) COMMAND LINE OPTION(S) HAVE BEEN SET
	if input_file == '' or output_image == '':
		print ''
		print 'viper.py -i <input_file> -v <output_image>'
		print 'viper.py --inputfile <input_file> --outputimage <output_image>'
		print ''
		sys.exit(3)



	#1: GET AND CLEAN DATA
	raw_data = get_parse_clean_data_as_csv_1( input_file )

	data_fields = []
	data_fields.append("airline")
	data_fields.append("avail_seat_km_per_week")
	data_fields.append("incidents_85_99")
	data_fields.append("fatal_accidents_85_99")
	data_fields.append("fatalities_85_99")
	data_fields.append("incidents_00_14")
	data_fields.append("fatal_accidents_00_14")
	data_fields.append("fatalities_00_14")

	clean_data = convert_list_of_lists_to_list_of_dicts( data_fields,raw_data[1:] )


	#2: ANALYZE DATA
	results = analyze_data_1( clean_data )


	#3: DISPLAY RESULTS
	#print results


	#4: SAVE RESULTS IF NAME OF OUTPUT FILE GIVE
	if output_file != '':
		save_data_1( results, output_file )


	#5: VISUALIZE DATA
	visualize_data_1( results,output_image )
####END MAIN DEFINITION



#CALL MAIN METHOD AND RUN CODE PASSING IN ARGUMENTS
if __name__ == "__main__":
 main(sys.argv[1:])
