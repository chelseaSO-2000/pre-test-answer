token_store = {}

def ingest(input_tokenSet):
    if input_tokenSet not in token_store:
        token_store[input_tokenSet] = 1
    else:
        token_store[input_tokenSet] += 1

def appearance(prefix):
    total_matched_tokenSet = sum([token_store[tokenSet] for tokenSet in token_store.keys() if tokenSet.startswith(prefix)])
    total_tokenSets = sum(token_store.values())
    appearance = total_matched_tokenSet / total_tokenSets
    return appearance

ingest('oursky:uk:dev')
ingest('oursky:hk:design')
ingest('oursky:hk:pm')
ingest('oursky:hk:dev')
ingest('skymaker')

appearance('oursky')
appearance('oursky:hk')

ingest('skymaker:london:ealing:dev')
ingest('skymaker:london:croydon')
ingest('skymaker:london:design')
ingest('skymaker:man:pm')
ingest('skymaker:man:pm')

appearance('skymaker:man')

'''
Space Complexity: O(N) because we store each unique token set as a key in the token_store dictionary.

Time Complexity (ingest function): O(1) on average, as it involves dictionary lookup and insertion, typically O(1) operations.

Time Complexity (appearance function): O(N) as it iterates through all unique token sets in token_store to find those starting with the given prefix.
'''
