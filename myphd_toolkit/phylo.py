import networkx as nx
# /mnt/storage7/lwang/Projects/Philipine_tb_report/data/excel_analysis_part3.ipynb
def tgv_output(df_snp, output_file_name):
    # Create a dictionary to store the output JSON
    output_dict = {}
    # Add "data" key to the output dictionary
    output_dict['nodes'] = []
    output_dict['edges'] = []

    # Loop through each row in the data frame
    for index, row in df_snp.iterrows():
        # Create a dictionary for each "node" entry
        node1 = {
                "id": row['Sample1'],
                "properties": {
                "lineage": row['Sample1_lin'],
                "dr_type": row['Sample1_dr'],
                "Same_patient": str(df_jody[df_jody['id']==row['Sample1']]['Serial'].values[0])
                }
            }
        node2 = {
                "id": row['Sample2'],
                "properties": {
                "lineage": row['Sample2_lin'],
                "dr_type": row['Sample2_dr'],
                "Same_patient": str(df_jody[df_jody['id']==row['Sample2']]['Serial'].values[0])
                }
            }
        # Create a dictionary for each "edge" entry
        edge = {
                "id": index + 1,
                "source": row['Sample1'],
                "target": row['Sample2'],
                "properties": {
                "distance": row['snp_distance'],}
            }
        # Append the node and edge dictionaries to the output dictionary
        output_dict['nodes'].append(node1)
        output_dict['nodes'].append(node2)
        output_dict['edges'].append(edge)
        # print(edge['properties']['distance'])

    # Convert the output dictionary to JSON
    output_json = json.dumps(output_dict, indent=2)

    with open(f'{output_file_name}.json', 'w') as f:
        f.write(output_json)

    print(f"Output JSON saved to '{output_file_name}.json'")
    
    
def cluster_size(min_size,df_snp):
    min_size = min_size
    min_cluster_size = 2
    G = nx.Graph()
    G.add_nodes_from(np.unique(df_snp.iloc[:,0].values))
    for index, row in df_snp.iterrows():
        # print(row[2])
        if row[2] <= min_size:
            G.add_edge(row[0], row[1], weight=row[2])
        else:
            pass

    components = [c for c in nx.connected_components(G) if len(c)>= min_cluster_size]
    cluster_nodes = [c for c in nx.connected_components(G) if len(c)>= min_cluster_size]
    single_nodes = [c for c in nx.connected_components(G) if len(c)< min_cluster_size]

    snp10_cluster_node_id = []
    single_node_id = []
    for x in cluster_nodes:
        for y in x:
            if y in snp10_cluster_node_id:
                continue
            else:
                snp10_cluster_node_id.append(y)

    for x in single_nodes:
        for y in x:
            if y in single_node_id:
                continue
            else:
                single_node_id.append(y)
    snp10_cluster_node = cluster_nodes
    max_size = 0
    max_cluster = []
    for x in components:
        if len(x) > max_size:
            max_size = len(x)
            max_cluster = x
    len(components)
    print(max_cluster)
    return len(components), len(snp10_cluster_node_id), max_size, snp10_cluster_node_id, cluster_nodes