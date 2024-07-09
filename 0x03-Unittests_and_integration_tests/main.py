from example import access_nested_map
data = {
    'user': {
        'profile': {
            'name': 'Alice',
            'age': 30
        },
        'settings': {
            'theme': 'dark'
        }
    }
}
path = ['user', 'profile', 'age']
name = access_nested_map(data, path)
print(name)  # Output: Alice

