import query

def decode_int(string):
	"""Decode an integer"""
	result = 0
	for n, c in enumerate(string):
		if isinstance(c, str):
			c = ord(c)
		result |= c << (8 * n)
	return result
  
def get_player_count(address, port):
	"""Get player count by I query"""
	req = query.send_query(address, port, 'i')
	return f'{decode_int(req[1:3])}/{decode_int(req[3:5])}'

if __name__ == "__main__":
	try:
		print(f'Players: {get_player_count("51.254.21.27", 7777)}')
		
	except:
		print('The server is offline')