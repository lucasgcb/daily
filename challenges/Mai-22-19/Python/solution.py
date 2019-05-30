def decoder(input):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v',
             'x','w','y','z']
    keys = [str(key) for key in range(1,27)]
    dictio = dict(zip(keys,alpha))
    combos = []
    identify_combos(input,combos,[],dictio)

def _check_key_start(start,keys):
    lenght = len(start)
    possible_follow_ups = []
    for key in keys:
        try:
            if start == key[:lenght]:
                possible_follow_ups.append(key)
        except IndexError:
            pass
    return possible_follow_ups
        
def _potential_comboer(follow_up,buffer,combos,currcombo,dictionary):
    from copy import deepcopy
    currcombo = deepcopy(currcombo)
    follow_up = follow_up + buffer[0]
    buffer = buffer[1:]
    keys = list(dictionary.keys())
    
    try:
        currcombo.append(dictionary[follow_up])
    except KeyError:
        return


    try:
        keys.remove(follow_up)
    except Exception:
        pass

    possible_follow_ups = _check_key_start(follow_up,keys)
    if len(possible_follow_ups) != 0:
        for follow_up in possible_follow_ups:
            _potential_comboer(follow_up,buffer,combos,currcombo,dictionary)
    if len(buffer) == 0:
        combos.append(currcombo)
    else:
        identify_combos(buffer,combos,currcombo,dictionary)

def identify_combos(buffer,combos,currcombo,dictionary):
    popped = buffer[0]
    buffer = buffer[1:]
    keys = list(dictionary.keys())
    keys.remove(popped)
    possible_follow_ups = _check_key_start(popped,keys)
    if len(possible_follow_ups) != 0:
        for follow_up in possible_follow_ups:
            _potential_comboer(follow_up,buffer,combos,currcombo,dictionary)
    if len(buffer) == 0:
        combos.append(currcombo)
    else:
        currcombo.append(dictionary[popped])
        identify_combos(buffer,combos,currcombo,dictionary)