import requests

class APIHelper:
    @staticmethod
    def get_request(url, headers=None, params=None):
        """
        Gửi generic GET request
        """
        response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def post_request(url, headers=None, json_data=None, data=None):
        """
        Gửi generic POST request
        """
        response = requests.post(url, headers=headers, json=json_data, data=data)
        return response