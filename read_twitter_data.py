from collections import defaultdict

def get_date_dict(filename):
	with open(filename) as f:
	    lines = f.readlines()
	    date_dict = {}
	    dates = ['2017-11-19', '2017-11-20', '2017-11-21', '2017-11-22', '2017-11-23', '2017-11-24', '2017-11-25', '2017-11-26', '2017-11-27', '2017-11-28']
	    for l in lines:
	    	#need to make a list
	    	for d in dates:
	    		if d in l:
			    	date_dict.setdefault(d, []).append(l[21:])
	        
	return date_dict

print(get_date_dict('data_collected.txt'))
