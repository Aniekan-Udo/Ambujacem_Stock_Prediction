# Config.py content

"""This module extracts information from your `.env` file so that
you can use your AplhaVantage API key in other parts of the application.
"""

# The os library allows you to communicate with a computer's
# operating system: https://docs.python.org/3/library/os.html
import os

# pydantic used for data validation: https://pydantic-docs.helpmanual.io/
from pydantic_settings import BaseSettings


def return_full_path(filename: str = ".env") -> str:
    """Uses os to return the correct path of the `.env` file."""
    absolute_path = os.path.abspath(__file__)
    directory_name = os.path.dirname(absolute_path)
    full_path = os.path.join(directory_name, filename)
    return full_path


class Settings(BaseSettings):
    """Uses pydantic to define settings for project."""

    alpha_api_key: str
    db_name: str
    models_directory: str

    class Config:
        env_file = return_full_path(".env")


# Create instance of `Settings` class that will be imported
# in lesson notebooks and the other modules for application.
settings = Settings(alpha_api_key="0b3ec2f2fa22b9e73e5c3fda5d7536cbf91897baa804efe3456002971673f8490520fa6dc476b27b9ea758a7f6a422d2b57aff95b0b12fb42eeeae2a767a60b010523c61e14faf552eedf52c68493d022d037474557ad1f36689ce2a25369843fbd96ca5df7e41bab698fa0c754db3c99c8a085ee00158e12ad0d29ea544f87f", db_name="db_name", models_directory="models_directory")
