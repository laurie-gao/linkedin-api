from linkedin import *

api = Linkedin('yaoming06061996@gmail.com', 'DARKenergy0-0')

# GET a school 
# res = api.get_school('columbia-university')

# GET a list of profiles
#res = api.search_people(keywords = 'Software', limit = 2)

#GET a user profile
res = api.get_profile(public_id = 'sydneylanders')

# GET a profiles contact info
# contact_info = api.get_profile_contact_info('laurie-gao')

# # GET 1st degree connections of a given profile
# connections = api.get_profile_connections('laurie-gao')

print(res)