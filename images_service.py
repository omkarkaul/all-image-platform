import json
import requests as r

from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from utilities import RequestError

class ImageService:
    def _is_valid(self, url):
        """ VALIDATE URL """
        valid_image_extensions = {"jpg", "png", "gif", "jpeg"}
        extension = url[url.rfind('.')+1:]

        parsed_url = urlparse(url)
        if extension not in valid_image_extensions:
            return False

        return bool(parsed_url.netloc) and bool(parsed_url.scheme)

    def _update_url_list(self, url, url_list, soup, tag, attribute):
        """ RUN THROUGH DOM TO FIND IMAGE URLS AND APPEND TO URL LIST BY REFERENCE """
        for image in soup.find_all(tag):
            image_url = image.attrs.get(attribute)
            
            if not image_url:
                continue
            absolute_image_url = urljoin(url, image_url)

            try:
                query_position = absolute_image_url.index("?")
                absolute_image_url = absolute_image_url[:query_position]
            except ValueError:
                pass

            if self._is_valid(absolute_image_url):
                url_list.append(absolute_image_url)

    def get_all(self, request):
        """ GET ALL IMAGE URL's FROM URL """
        url = request.args.get("url")
        if not url:
            return {"message": "Missing URL from request"}, 400
        
        response = r.get(url)
        soup = bs(response.content, "html.parser")

        url_list = []
        self._update_url_list(url, url_list, soup, "img", "src")
        self._update_url_list(url, url_list, soup, "a", "href")

        return {"image_url_list":url_list}, 200