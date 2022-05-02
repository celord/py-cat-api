import logging
from the_cat_api.rest_adapter import RestAdapter
from the_cat_api.exceptions import TheCatApiException
from the_cat_api.models import *


class TheCatApi:
    def __init__(self, hostname: str = 'api.thecatapi.com', api_key: str = '', ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(
            hostname, api_key, ver, ssl_verify, logger)

    def get_kitty(self) -> ImageShort:
        return self.get_clowder_of_kitties(amt=1)[0]

    def get_clowder_of_kitties(self, amt: int = 1) -> List[ImageShort]:
        params = {'limit': amt}
        result = self._rest_adapter.get(
            endpoint='/images/search', ep_params=params)
        kitty_img_list = [ImageShort(**datum) for datum in result.data]
        return kitty_img_list

    def fetch_image_data(self, image: ImageShort):
        image.data = self._rest_adapter.fetch_data(url=image.url)

    def get_kitties_paged(self, max_amt: int = 100) -> Iterator[ImageShort]:
        # Int variables
        amt_yielded = 0
        curr_page = last_page = 1
        endpoint = '/images/search'
        ep_params = {'limit': self._page_size, 'order': 'Desc'}

        # Keep fetching pages of kitties until the last page
        while curr_page <= last_page:
            ep_params['page'] = curr_page
            result = self._rest_adapter.get(
                endpoint=endpoint, ep_params=ep_params)

            # Increment curr_page by 1 and update the last_page based on header info returned
            last_page = int(result.headers.get('pagination-count', 1))
            curr_page = int(result.headers.get('pagination-page')) + 1

            # Yield 1 kitty from the page; break/end loop if beyond max_amt
            for datum in result.data:
                yield ImageShort(**datum)
                amt_yielded += 1
                if amt_yielded >= max_amt:
                    last_page = 0
                    break
