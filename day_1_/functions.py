def active_wc_rappers(westcost, eastcoast):
    results = westcost - eastcoast
    return results
print(active_wc_rappers(39,100))

def active_ec_rappers(eastcoast, westcost):
    results = eastcoast - westcost
    return results
print(active_ec_rappers(100,29))


quote = "The ability to speak does not make you intelligent"

def make_quote():
    quote = "This is not true"
    print(quote)

make_quote()
print(quote)
