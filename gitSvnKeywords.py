import sys
import os

def replace_id_tag( old_string, new_string ):
	return old_string.replace( "$Id$", "$Id: " + new_string + " $" )

def replace_log_tag( old_string, new_string ):
	return old_string.replace( "$Log$", "$Log: $ \n" + new_string + "\n" )

def add_comments( old_string ):
	return "// " + old_string.replace( "\n", "\n// " )

def annotate_file( file_name ):
	short_log_message = os.popen( "git log -n 1 --oneline -- " + file_name ).readline().replace("\n", "")
	long_log_message = os.popen( "git log -- " + file_name ).read()
	long_log_message_commented = add_comments( long_log_message )
	f = open( file_name )
	file_content = f.read()
	file_content = replace_id_tag( file_content, short_log_message )
	file_content = replace_log_tag( file_content, long_log_message_commented )

	f_write = open( file_name, "w" ) # w used to overwrite file
	f_write.write( file_content )

def get_file_list():
	file_list = list()
	file_list_stream = os.popen("git ls-tree --full-tree -r HEAD")
	for file_list_line in file_list_stream.read().split( "\n" ):
		if len( file_list_line ) > 0:
			file_list.append( file_list_line.split()[-1] )
	return file_list

file_list = get_file_list()
for current_file in file_list:
	if( current_file != "gitSvnKeywords.py" and current_file[0] != "." ):
		print( current_file + "\n" )
		annotate_file( current_file )
