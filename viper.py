#!/usr/bin/python

"""
viper.py
Data Science with python.

Author: Victor Green, vgreen@gds.org
Date: 09-30-2015

Goal: To create a universal template for data science workflow as it 
pertains to python. The purpose is to predifine as much boilerplate code
as possible subscibing to a functional programming paridigm allowing aspiring
and current data scientists to focus on data science while learning the particulars
of the python programming language. Use and modify this template as you see fit and please
fork this project on github. All improvements / suggestions are wellcome.
Many Thanks, Victor Green Data Engineer / Data Scientist
"""



#IMPORT NEEDED LIBRARIES
import sys
import getopt



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
####END DATA PARSING AND CLEANING FUNCTIONS



####BEGIN DATA ANALYSIS FUNCTIONS HERE
def analyze_data_1( data ):
	"""PERFORMS 1ST LEG OF ANALYSIS
	AND RETURNS RESULTS AS A LIST OF TUPLES
	"""

	results = []

	for airline in data[1:]:

		name = airline[0]
		first_incident = airline[2]
		second_incident = airline[5]

		all_incidents = int(first_incident) + int(second_incident)
		avg_incidents = all_incidents / 30
		results.append( ( name,avg_incidents) )

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
####END DATA VISUALIZATION FUNCTIONS



####BEGIN MAIN METHOD DEFINITION
def main( argv ):

	#DEFINE COMMAND LINE OPTIONS
	#SHOULD INITALIZE BECAUSE THESE
	#ARE OPTOINS HENCE OPTIONAL
	input_file = ''
	output_file = ''


	#PARSE COMMAND LINE OPTIONS
	#RAISE ERROR IF OPTION IS NOT VALID
	#OR IF REQUIRED ARGUMENT DOES FOLLOW OPTION
	try:
		opts, args = getopt.getopt( argv, "hi:o:",["help","inputfile=","outputfile="] )
	except getopt.GetoptError:
		print ''
		print 'viper.py -i <input_file> -o <output_file>'
		print 'viper.py --inputfile <input_file> --outputfile <output_file>'
		print ''
		sys.exit(2)

	#LOOP THROUGH OPTIONS
	#SHOW HELP IF PASSED
	#OR SET OPTIONS 
	for opt, arg in opts:
		if opt == '-h' or opt == '--help':
			print ''
			print 'viper.py -i <input_file> -o <output_file>'
			print 'viper.py --inputfile <input_file> --outputfile <output_file>'
			print ''
			sys.exit()

		#SHORT OPTION FORM OR LONG OPTION FORM 
		elif opt in ("-i","--inputfile"):
			input_file = arg
		elif opt in ("-o","--outputfile"):
			output_file = arg


	#CHECK TO SEE IF ANY (REQUIRED) COMMAND LINE OPTION(S) HAVE BEEN SET
	if input_file == '':
		print ''
		print 'viper.py -i <input_file>'
		print 'viper.py --inputfile <input_file>'
		print ''
		sys.exit(3)


	#1: GET AND CLEAN DATA
	data = get_parse_clean_data_as_csv_1( input_file )
	#SLICE DATA SKIPPING FIRST ROW
	#print data[1:]


	#2: ANALYZE DATA
	results = analyze_data_1( data )


	#3: DISPLAY RESULTS
	print results


	#4: SAVE RESULTS IF NAME OF OUTPUT FILE GIVE
	if output_file != '':
		save_data_1( results, output_file )
####END MAIN DEFINITION



#CALL MAIN METHOD AND RUN CODE PASSING IN ARGUMENTS
if __name__ == "__main__":
 main(sys.argv[1:])
