def format_resources(data):
    nodes = []
    edges = []
    node_ids = set()  # Set to track existing node IDs

    for resource in data:
        resource_node_id = resource["key"]
        
        # Only add resource node if it is not already in the set
        if resource_node_id not in node_ids:
            nodes.append({"id": resource_node_id, "label": resource["name"], "type": "resource"})
            node_ids.add(resource_node_id)

        # Add roles as nodes and create edges from resource to roles
        for role_key, role in resource["roles"].items():
            role_node_id = role_key
            
            # Only add role node if it is not already in the set
            if role_node_id not in node_ids:
                nodes.append({"id": role_node_id, "label": role["name"], "type": "role"})
                node_ids.add(role_node_id)
            
            edges.append({"source": resource_node_id, "target": role_node_id, "type": "has_role", "label": "has_role"})

            # Add permissions as nodes and create edges from roles to permissions
            for permission in role["permissions"]:
                permission_node_id = permission
                
                # Only add permission node if it is not already in the set
                if permission_node_id not in node_ids:
                    nodes.append({"id": permission_node_id, "label": permission, "type": "permission"})
                    node_ids.add(permission_node_id)

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
