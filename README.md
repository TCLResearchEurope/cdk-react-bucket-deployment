# ReactBucketDeployment for AWS CDK

A custom AWS CDK construct that integrates node for building react projects, automating the process of dependency resolution, packaging, and deployment preparation to AWS S3.

## Features

TODO


## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [AWS CDK](https://github.com/aws/aws-cdk)
- [Node.JS](https://nodejs.org/en)

## Installation

To use ReactBucketDeployment in your CDK project, install it via pip:

```bash
pip install cdk-react-bucket-deployment
```

## Usage
TODO

## Configuration

TODO


## Local Development

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging, and it's recommended to use Poetry to run local development tasks to ensure consistency with the project's dependencies.

### Running tests
All the tests are based on [pytest](https://docs.pytest.org/) so running them boils down to executing one command:
```shell
poetry run pytest
```

### Running Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality and formatting standards. To set up pre-commit hooks within the Poetry environment, which ensures that the hooks are run automatically before each commit, execute the following command:

```bash
poetry run pre-commit install
```

This command installs pre-commit hooks as Git pre-commit hooks, so they are automatically executed before you commit changes. It's a convenient way to ensure your changes adhere to the project's standards without needing to manually run checks before each commit.

If you prefer to run pre-commit hooks manually, perhaps to check files before committing, you can use the following command:
```bash
poetry run pre-commit run --all-files
```
This will manually execute all configured pre-commit hooks on all files in the repository. It's useful for performing a one-time check or for scenarios where you haven't set up automatic pre-commit hooks with pre-commit install.


### Running Pyright
Pyright is used for static type checking to catch errors early in development. To run Pyright through Poetry, use the following command:

bash
```
poetry run pyright
```

This will execute Pyright type checking based on the project's pyrightconfig.json configuration. Running Pyright helps ensure type consistency and can catch common errors.


## Contributing
- Submitting bug reports and feature requests in the Issues section.
- Opening pull requests with improvements to code or documentation.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- Thanks to the AWS CDK team for providing the framework.
- Thanks to the Poetry team for simplifying Python package management.
