# Cururo: Automated Review Tool

## Description

Based on [Condor](https://github.com/CarloGauss33/Condor) (automated PR review tool) this tool leverages the power of generative AI to offer insightful and constructive feedback. This CLI software is designed to facilitate item reviews using OpenAI's services. It allows users to specify an item for review, authenticate with OpenAI, and customize the review process through various command-line arguments.

## Features

- **AI-Powered Review Process**: Cururo uses generative AI to offer constructive criticism and suggestions.
- **CI/CD Integration (Coming Soon)**: Cururo will soon support integration with Continuous Integration/Continuous Deployment (CI/CD) systems, allowing automated reviews to be triggered by events such as PR creation or code push.

## Usage

To use Cururo, you must have an OpenAI API key. You can obtain an API key by signing up for an account on the [OpenAI website](https://platform.openai.com/).

To run Cururo, you need to specify the input arguments:

- `--item`: The item you want to review.
- `--openai-key`: Your OpenAI API key.
- `--assistant-id`: The ID of the OpenAI assistant you want to use.
- `--action` (callable, optional): A custom action to perform on the OpenAI response.
- `--publisher` (Publisher, optional): The publisher to use for the review.

## Requirements

- Python 3.6 or higher
- OpenAI Python client
- PyGithub

You can install the required Python packages using pip:
`pip install openai PyGithub`
