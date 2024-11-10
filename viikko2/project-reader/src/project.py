class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors):
        self.name = name
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"Authors: {self.authors}"
            f"\nDescription: {self.description or '-'}"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
