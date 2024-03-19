from http import HTTPStatus

import httpx
import respx

hiscore_mock = respx.mock(
    base_url="https://secure.runescape.com", assert_all_called=False
)

hiscore_mock.get(
    "/m=hiscore_oldschool/index_lite.json",
    name="get_hiscore",
).mock(return_value=httpx.Response(HTTPStatus.BAD_REQUEST))

hiscore_mock.get(
    "/m=hiscore_oldschool_ironman/index_lite.json",
    name="get_hiscore_ironman",
).mock(return_value=httpx.Response(HTTPStatus.BAD_REQUEST))
