import query

def decode_int(string):
    result = 0
    for n, c in enumerate(string):
        if isinstance(c, str):
            c = ord(c)
        result |= c << (8 * n)
    return result
  
  def GetPlayersCount(address, port):
    req = query.SendQueryRequest(address, port, 'i')

    if req == 0:
        return 'Offline'
    else:
        return f'{decode_int(req[1:3])}/{decode_int(req[3:5])}'
