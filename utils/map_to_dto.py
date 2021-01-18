def map_to_dto(dict):
    return {
        'id': dict['Id'],
        'title': dict['Title'],
        'poster': dict['Poster']
    }
