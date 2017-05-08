import fdp

parsemap = r"C:\Users\jwinsley\Downloads\inventories.xml"
inputfile = r"C:\Users\jwinsley\Downloads\Inventories_TEST.txt"


parser = fdp.FileParser(parsemap)

#print parser.root.debug()

result = parser.parse(inputfile)

print "Found {} inventories".format(len(result.keys()))
users_to_check = set(result["OUT"]["users"].keys())
for mnemonic in sorted(result.keys()):
	if "users" not in result[mnemonic]:
		continue # No users defined, so no access restriction
	users_in_inventory = set(result[mnemonic]["users"].keys())
	#print "Checking {} ({} users)".format(mnemonic, len(users))
	missing_users = users_to_check - users_in_inventory
	if len(missing_users):
		print "{}: add users ({})".format(mnemonic, ", ".join(missing_users))