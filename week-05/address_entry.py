contact_info = {
    "name": "Alex Rivera",
    "address": "123 Main Street",
    "city": "Boston",
    "state": "MA",
    "zip": "02110"
}

# Print the mailing address in one print statement.
print(
    f"{contact_info['name']}\n"
    f"{contact_info['address']}\n"
    f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"
)

# Remove the name entry.
del contact_info["name"]

# Add first and last name in a separate dictionary.
full_name = {
    "first name": "Alex",
    "last name": "Rivera"
}

# Add an honorific, then add full_name to contact_info.
full_name.update({"honorific": "Mx."})
contact_info.update({"full_name": full_name})

# Print the updated mailing address in one print statement.
print(
    f"{contact_info['full_name']['honorific']} "
    f"{contact_info['full_name']['first name']} "
    f"{contact_info['full_name']['last name']}\n"
    f"{contact_info['address']}\n"
    f"{contact_info['city']}, {contact_info['state']} {contact_info['zip']}"
)