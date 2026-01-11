# Optional: Development Container (GitHub Codespaces)

This repository includes an **optional development container** configuration.

It provides a ready-to-run cloud-based development environment
using GitHub Codespaces[1]().

The same configuration can also be used locally with VS Code Dev Containers[2]().

The workflow inside the dev container mirrors the local workflow.

**Local development is still recommended.**
This option exists as a fallback when:

- there are difficulties installing locally
- working on a restricted machine
- using a temporary, browser-based environment

## Dev Container

A dev container:

- runs a Linux environment
- includes Python (with the version specified in the configuration file)
- installs project dependencies using the **same commands** used locally
- enables running code, tests, and tools in a terminal

A dev container is **not**:

- required
- a replacement for learning local setup

## This Dev Container

- Uses a standard Python base image
- Runs the same dependency install command used locally:

```bash
  uv sync --extra dev --extra docs --upgrade
```

- Does not add databases, services, or exposed ports
- Is intentionally simple and predictable

## Editor Settings and Extensions

VS Code settings and extensions inside the dev container are
aligned with the repository root configuration at `.vscode/extensions.json`.

When updating the root `.vscode/` folder, update the dev container configuration to stay in sync.

This avoids:

- conflicting editor behavior
- different tooling expectations

## How to Use (Optional)

This option is disabled by default to keep the project local-first.

If you choose to try this option:

1. Rename the file from `.devcontainer/devcontainer_OPTION.json` to `.devcontainer/devcontainer.json`.
2. In `.vscode/extensions.json`, uncomment or add "ms-vscode-remote.remote-containers" to recommendations.
3. Reopen VS Code to accept recommendations.
4. Push the repository to your GitHub account
5. Open the repository on GitHub
6. Click Code / Codespaces / Create codespace
7. Wait for the environment to build
8. Use the same commands shown in the README.md

## GitHub Codespaces

GitHub Codespaces provides a cloud-based development environment that runs in a
web browser or in VS Code, hosted by GitHub.

- Free usage may be available for verified students
- Usage limits may apply
- This course does not require Codespaces

## VS Code Dev Containers

VS Code Dev Containers use the same configuration to run the project inside
a container on your local machine.
