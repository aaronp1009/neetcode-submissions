class TimeMap:

    def __init__(self):
        self.store = {} # Key : [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if in hashmap or not
        if key not in self.store:
            # Add it
            self.store[key] = [] # Empty list to hold our value, timestamp
        
        # Now that our key exists, add our value and timestamp
        self.store[key].append([value, timestamp]) # Append a list [value, timestamp]

    def get(self, key: str, timestamp: int) -> str:
        res = "" # Return empty if no values exist

        # Check if this key exists, if so, get the list of values. Each value is a list [value, timestamp]
        values = self.store.get(key, []) # Default is an empty list, no value, timestamp found

        # We know timestamps increase, so we can do a binary search.
        l, r = 0, len(values)-1

        while l <= r:
            # Mid
            m = l + ((r - l) // 2)

            # Check if middle timestamp is correct, if so we can return
            if values[m][1] == timestamp:
                return values[m][0] # Return the associated value of [value, timestamp]
            elif values[m][1] < timestamp:
                # We know our middle is too small, need to search the right side
                l = m + 1
                # Store our most recent result in case we don't find anything for the timestamp provided
                res = values[m][0]
            else:
                # This is where the store contains a timestamp larger than the input timestamp
                r = m - 1
        
        return res

        
