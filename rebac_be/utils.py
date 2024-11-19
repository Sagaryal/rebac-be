# Utility function to process resources and format them into nodes and edges
def format_resources(data):
    nodes = []
    edges = []

    for resource in data:
        resource_node_id = resource["key"]
        nodes.append({"id": resource_node_id, "label": resource["name"], "type": "resource"})

        # Add roles as nodes and create edges from resource to roles
        for role_key, role in resource["roles"].items():
            role_node_id = role_key
            nodes.append({"id": role_node_id, "label": role["name"], "type": "role"})
            edges.append({"source": resource_node_id, "target": role_node_id, "type": "has_role", "label": "has_role"})

            # Add permissions as nodes and create edges from roles to permissions
            for permission in role["permissions"]:
                permission_node_id = permission
                nodes.append({"id": permission_node_id, "label": permission, "type": "permission"})
                edges.append({"source": role_node_id, "target": permission_node_id, "type": "has_permission", "label": "has_permission"})

        # Add relations between resources as edges
        for relation_key, relation in resource["relations"].items():
            if relation.get("resource_id"):
                edges.append({
                    "source": resource_node_id,
                    "target": relation["resource"],
                    "type": "relation",
                    "label": relation_key,
                })

    return {"nodes": nodes, "edges": edges}