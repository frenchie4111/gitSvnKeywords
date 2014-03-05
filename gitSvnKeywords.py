import sys
import os

def replace_id_tag( old_string, new_string ):
	return old_string.replace( "$Id$", "$Id " + new_string + " $" )

def replace_log_tag( old_string, new_string ):
	return old_string.replace( "$Log$", "$Log$ \n" + new_string + "\n" )

def add_comments( old_string ):
	return "\\\\ " + old_string.replace( "\n", "\n\\\\ " )

def annotate_file( file_name ):
	short_log_message = os.popen( "git log -n 1 --oneline -- " + file_name ).readline()
	long_log_message = os.popen( "git log -- " + file_name ).read()
	long_log_message_commented = add_comments( long_log_message )
	file = open( file_name )
	print( file_name + file.read() )

def get_file_list():
	file_list = list()
	file_list_stream = os.popen("git ls-tree --full-tree -r HEAD")
	for file_list_line in file_list_stream.read().split( "\n" ):
		if len( file_list_line ) > 0:
			file_list.append( file_list_line.split()[-1] )
	return file_list

# lines = sys.stdin.read()

# lines = replace_log_tag( lines, "This is the new log info" )

# file_list = get_file_list()
# for current_file in file_list:
# 	print( current_file + "\n" )
# 	annotate_file( current_file )

annotate_file( "test" )
