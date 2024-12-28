import json
import os
import logging
from typing import Tuple, Union
import requests
from requests import RequestException, JSONDecodeError
from .exceptions import ERROR_CODES


logger = logging.getLogger("pyident").addHandler(logging.NullHandler())

class ZibalClient:
    """
    A client for interacting with the Zibal API.
    
    Documentation: https://help.zibal.ir/facilities
    """
    
    def __init__(
            self,
            api_token: str = os.environ.get("ZIBAL_TOKEN"),
            base_url: str = "https://api.zibal.ir/v1"
        ) -> None:
        self.base_url = base_url
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {api_token}"
        }
    
    def is_user_identified(self, mobile: str, national_code: str, raw: bool = False) -> Union[bool, requests.Response]:
        """
        Check if a user is identified using their mobile number and national code.
        
        Args:
            mobile: User's mobile number
            national_code: User's national code
            raw: If True, returns the raw response object
            
        Returns:
            bool: True if user is identified, False otherwise
            or
            Response: Raw response object if raw=True
            
        Raises:
            ValueError: If the request fails or response cannot be parsed

        Zibal Response:
        {
            "message": "موفق",
            "data": {
                "matched": true
            },
            "result": 1
        }
        """
        try:
            res = requests.post(
                url=f"{self.base_url}/facility/shahkarInquiry",
                headers=self.headers,
                data=json.dumps({
                    "nationalCode": national_code,
                    "mobile": mobile,
                })
            )
            logger.info(
                "Zibal is_user_identified",
                exc_info=True,
                extra={"response": res.text}
            )
            if (result_code := res.json()["result"]) == 1:
                return res if raw else res.json()["data"].get("matched", False)
            
            if result_code in ERROR_CODES:
                error_class, error_message = ERROR_CODES[result_code]
                raise error_class(error_message, result_code)

        except RequestException as ex:
            raise ValueError(f"Request failed: {ex}")
        except JSONDecodeError as ex:
            logger.warning(str(ex), exc_info=True)
            raise ValueError(f"Failed to parse response: {ex}")

    def get_user_identity(
        self, 
        birthday: str, 
        national_code: str, 
        raw: bool = False
    ) -> Union[Tuple[dict, int], requests.Response]:
        """
        Get user identity information using birthday and national code.
        
        Args:
            birthday: User's birthday in format 'YYYY/MM/DD'
            national_code: User's national code
            raw: If True, returns the raw response object
            
        Returns:
            tuple: (identity_data, status_code)
            or
            Response: Raw response object if raw=True
            
        Raises:
            ValueError: If the birthday format is invalid or request fails

        Zibal Response:
        {
            "result": 1,
            "message": "موفق",
            "data": {
                "matched": true,
                "firstName": "امير",
                "lastName": "صادقی بارانی",
                "fatherName": "حميد",
                "alive": true
            }
        }
        """
        self.validate_birthday(birthday)
        try:
            res = requests.post(
                url=f"{self.base_url}/facility/nationalIdentityInquiry/",
                headers=self.headers,
                data=json.dumps({
                    "nationalCode": national_code,
                    "birthDate": birthday,
                })
            )
            logger.info(
                "Zibal user identity",
                exc_info=True,
                extra={"response": res.text}
            )
            if (result_code := res.json()["result"]) == 1:
                return res if raw else (res.json()["data"], res.status_code)
            
            if result_code in ERROR_CODES:
                error_class, error_message = ERROR_CODES[result_code]
                raise error_class(error_message, result_code)
            
        except RequestException as ex:
            raise ValueError(f"Request failed: {ex}")
        except JSONDecodeError as ex:
            logger.warning(str(ex), exc_info=True)
            raise ValueError(f"Failed to parse response: {ex}")

    @staticmethod
    def validate_birthday(birthday: str) -> bool:
        """
        Validate birthday string format.
        
        Args:
            birthday: Date string in format 'YYYY/MM/DD'
            
        Returns:
            bool: True if valid
            
        Raises:
            ValueError: If format is invalid
        """
        if not birthday:
            raise ValueError("birthday is required")
        parts = birthday.split("/")
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            raise ValueError("birthday should be in the format 'YYYY/MM/DD'")

        return True
