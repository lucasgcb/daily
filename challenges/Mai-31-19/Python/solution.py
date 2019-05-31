class Log:
    def __init__(self,logs={}):
        # Keep logs in a dictionary
        self.entries = logs
    
    def record(self,order_id):
        # Keep keys linearly increasing with log size
        next_entry = len(self.entries)+1
        self.entries[next_entry]=order_id

    def get_last(self,i=1):
        # Retrieve value from key
        key_list = list(set(self.entries.keys()))
        try:
            last_key = key_list[-i]
            result = self.entries[last_key]
        except IndexError:
            print("Entry does not exist")
            return None
        return result