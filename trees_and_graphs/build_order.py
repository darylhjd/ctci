from collections import defaultdict


def build_order(projects_list, dependencies):
    """Find a build order that will allow all projects to be built given a list of projects and their dependencies
    which are in the form (dependency, project).
    If there is no valid order, return an error."""
    # Solution: O(V + E), V is number of projects and E is number of dependencies.

    projects_list = set(projects_list)
    # Create adjacency list where the project is the key and the dependencies are the neighbours.
    adj_list = defaultdict(set)
    for dep, proj in dependencies:
        adj_list[proj].add(dep)

    order = []
    # Keep looping through projects_list and check if they have dependencies,
    while len(projects_list) != 0:
        to_build = set()
        for project in projects_list:
            # If there are dependencies
            if len(adj_list[project]) == 0:
                to_build.add(project)

        # If there were no possible projects to build, that means we have hit a circular dependency.
        if len(to_build) == 0:
            return False, []

        # Remove the built projects.
        for built in to_build:
            adj_list.pop(built)
        # And also remove them as dependencies
        for project in adj_list:
            adj_list[project].difference_update(to_build)

        # Update the build order
        order.extend(to_build)
        projects_list.difference_update(to_build)
    return True, order


if __name__ == '__main__':
    projects = ["a", "b", "c", "d", "e", "f"]
    deps = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "c"), ("e", "f")]
    print(build_order(projects, deps))
