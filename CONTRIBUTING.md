# Contributing to [Project Name]

We welcome and encourage all forms of contribution! This guide will help you understand our process and expectations.

## Code of Conduct

Please review the Code of Conduct. It is in effect at all times. We expect it to be honored by everyone who contributes to this project. Disrespectful behavior will not be tolerated.

## GitFlow Workflow

We use the GitFlow branching model for development. Here's a quick overview:

1. `prod` branch contains production code
2. `develop` branch is for ongoing development
3. Feature branches are created from `develop`
4. Hotfix branches are created from `prod`(Very unlikely)
5. When creating a branch on a feature, create using the suffix "feat/<name of your feature>"

## Commit Messages

We use conventional commit messages. Each commit message should have a type and a short description:

- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, missing semi-colons, etc)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks, dependency updates, etc

Example: `feat: add user authentication API`

Additionally, please follow these guidelines for commit messages:

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at about 72 characters
- Use the body to explain why, not what and how

## Pull Requests

When submitting a pull request:

1. Create your feature branch from `develop`
2. Make your changes and commit using conventional commit messages
3. Push your branch and create a pull request against `develop`
4. Fill out the pull request template, providing a clear description of your changes

Your pull request description should include:
- What the change does
- Why the change is needed
- Any potential risks or considerations

Remember: Code reviews are about the code, not the coder. Don't take feedback personally, and be respectful when giving feedback to others.

## Code Review Process

1. At least one core team member must review and approve your PR
2. Address any comments or requested changes
3. Once approved, a maintainer will merge your PR

## Best Practices

- Smaller is better. Submit one pull request per bug fix or feature.
- Coordinate bigger changes. For large changes, open an issue to discuss strategy with maintainers first.
- Prioritize understanding over cleverness. Write clear, concise code.
- Follow existing coding style and conventions.
- Include test coverage. Add unit tests or UI tests when possible.
- Update documentation for your changes.
- Update the CHANGELOG for all enhancements and bug fixes.
- Resolve any merge conflicts that occur.
- Promptly address any CI failures.

## Asking Questions

Before opening an issue, please check if you're using the latest version of the project and if updating resolves your issue. For debugging help, please refer to our Support Guide.

## Reporting Security Issues

Please review our Security Policy. Do not file a public issue for security vulnerabilities.

## Development Setup

Kindly refer to README.md to get instructions on how to setup the development server.

## Running Tests

For running tests. After activating the enviroment of this reposotory. In the terminal.

Run the following command.

```
tox -e py
```


Thank you for contributing!

🖤
