from setuptools import setup, find_packages

setup(
    name="customer_support_chatbot",
    version="0.1.0",
    description="A prototype customer support chatbot for a computer products company.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "requests",
        # Uncomment the following line if using HuggingFace Transformers or OpenAI
        # "transformers",
        # "openai",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)