# create. id: test_key, email: test@key
gpg --full-generate-key

# list
gpg --list-secret-keys

# save
gpg --output test_key.gpg --export test_key

# edit if needed
# gpg --edit-key id

# import
# gpg --import test_key.gpg
