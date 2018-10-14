hygrothermograph_config = {
    'find': {
        'prefix': '',
        'url': '/hygrothermographs',
        'method': 'GET',
        'contentsType': 'application/hal+json'
    },
    'find_one': {
        'prefix': '',
        'url': '/hygrothermographs/:id',
        'method': 'GET',
        'contentsType': 'application/hal+json'
    },
    'create': {
        'prefix': '',
        'url': '/hygrothermographs',
        'method': 'POST',
        'contentsType': 'application/hal+json'
    },
    'update': {
        'prefix': '',
        'url': '/hygrothermographs/:id',
        'method': 'PUT',
        'contentsType': 'application/hal+json'
    },
    'delete': {
        'prefix': '',
        'url': '/hygrothermographs/:id',
        'method': 'DELETE',
        'contentsType': 'application/hal+json'
    }
}
