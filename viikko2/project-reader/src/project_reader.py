import toml
from urllib import request
from project import Project



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        filtteröity = toml.loads(content)


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project_info = filtteröity["tool"]["poetry"]
        name = project_info.get("name", "Unknown name")
        description = project_info.get("description", "No description")
        dependencies = list(project_info.get("dependencies", {}).keys())
        dev_dependencies = list(project_info.get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        return Project(name, description, dependencies, dev_dependencies)
