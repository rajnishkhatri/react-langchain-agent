"""Setup file for react_langchain_agent package."""
from setuptools import setup, find_packages

setup(
    name="react_langchain_agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "openai",
        "python-dotenv",
        "black",
        "langchain-openai",
        "gradio>=4.0.0",
    ],
    python_requires=">=3.9",
) 