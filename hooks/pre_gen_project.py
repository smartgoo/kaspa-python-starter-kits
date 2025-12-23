#!/usr/bin/env python
"""Pre-generation hook for validating cookiecutter inputs."""

import re
import sys

# Get cookiecutter variables
project_slug = "{{ cookiecutter.project_slug }}"

# Validate project slug
SLUG_REGEX = r"^[a-z][a-z0-9_]*$"
if not re.match(SLUG_REGEX, project_slug):
    print(f"ERROR: '{project_slug}' is not a valid Python package name.")
    print("Package names must start with a letter and contain only lowercase letters, numbers, and underscores.")
    sys.exit(1)

print(f"✓ Creating API project: {project_slug}")
