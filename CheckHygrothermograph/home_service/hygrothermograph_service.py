from home_service.base_service import AlterService, RetrieveService
from home_service.config.api.hygrothermograph import hygrothermograph_config


class HygrothermographService(AlterService, RetrieveService):
    _api_config = hygrothermograph_config
