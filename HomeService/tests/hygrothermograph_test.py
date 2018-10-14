from home_service.hygrothermograph_service import HygrothermographService

hygrothermograph_service = HygrothermographService()

find_test = hygrothermograph_service.find()

if find_test.is_ok():
    print(find_test.get_data())

create_test = hygrothermograph_service.create({'region': 'LIVING_ROOM', 'temperature': 25, 'humidity': 45})

if create_test.is_ok():
    print(create_test.get_data())
