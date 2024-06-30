import sdg
import os
import yaml

"""
This is a one-time script to recover some US-specific config.
"""

# Get the metadata for an indicator.
def get_metadata(filepath):
    with open(filepath, 'r') as stream:
        try:
            for doc in yaml.safe_load_all(stream):
                if hasattr(doc, 'items'):
                    return doc
        except yaml.YAMLError as e:
            print(e)

def write_metadata(filepath, metadata):
    yaml_string = yaml.dump(metadata,
        allow_unicode=True)
    with open(filepath, 'w') as outfile:
        outfile.write(yaml_string)

ids = sdg.path.get_ids()
for inid in ids:
    filepath = os.path.join('meta', inid + '.md')
    config_filepath = os.path.join('indicator-config', inid + '.yml')
    if os.path.isfile(filepath) and os.path.isfile(config_filepath):
        meta = get_metadata(filepath)
        indicator_config = get_metadata(config_filepath)
        if 'actual_indicator_available' in meta and meta['actual_indicator_available'] != '':
            indicator_config['graph_title'] = meta['actual_indicator_available']
            write_metadata(config_filepath, indicator_config)
