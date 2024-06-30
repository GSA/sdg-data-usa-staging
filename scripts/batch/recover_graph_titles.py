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
    filepath = os.path.join('indicator-config', inid + '.yml')
    if os.path.isfile(filepath):
        meta = get_metadata(filepath)
        old_filepath = os.path.join('..', 'sdg-data-usa', 'meta', inid + '.md')
        old_meta = get_metadata(old_filepath)

        # In some cases the US graph_title was different from the
        # global indicator name.
        if old_meta['indicator_name'] != old_meta['graph_title']:
            meta['indicator_available'] = old_meta['graph_title']
            meta['graph_title'] = old_meta['graph_title']
            write_metadata(filepath, meta)
