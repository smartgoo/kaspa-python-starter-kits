#!/usr/bin/env python
"""Post-generation hook for project setup."""


def main():
    print(f"\n✅ Project '{{ cookiecutter.project_name }}' created successfully!")
    print(f"\n📁 Next steps:")
    print(f"   cd {{ cookiecutter.project_slug }}")
    print(f"   python -m venv .venv")
    print(f"   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate")
    print(f"   pip install -r requirements.txt")
    print(f"\n   # Start the API server:")
    print(f"   fastapi dev main.py")
    print(f"\n   # View API docs at http://localhost:8000/docs")


if __name__ == "__main__":
    main()
