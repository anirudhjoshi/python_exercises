def median( number ):

	# Check if even
	if even( number ):
		return number / 2
	# Add one up - so rounding is unnecessary
	else:
		return ( number + 1 ) / 2

def even( number ):

	# Check remainder of dividing by 2 - if 1 - odd
	# if 0 - even
	# As 0 is even, return not, to make 1 - true
	return not number % 2

def pascal( row ):

	# Store states
	median_value = median ( row )  

	previous = 1

	denominator = 1
	numerator = row 

	# Store return
	level_array = [ 1 ]
	
	# Calculate row by only calculating half of it
	# via fraction formula

	while numerator != median_value:

		# Formula

		new = previous * numerator / denominator

		# State change of fraction, store of value
		level_array.append( new )
		previous = new
		numerator -= 1
		denominator += 1

	if even( row ):
	# Even rows don't require the first part of the reversal
	# double up
		reverse = level_array[::-1][1:]
	else:
		reverse = level_array[::-1]

	return	level_array + reverse

if __name__ == "__main__":
	for number in xrange( 0, 10 ):
		print pascal( number )
