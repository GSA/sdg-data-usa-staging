import re

def alter_data(df, context):
    return df


def alter_meta(meta, context):
    def remove_global_numbers(input_string):
        """
        Global metadata includes numbers before the indicator/target/goal numbers.
        We would like to remove them, since they sometimes do not match the current
        indicator.
        """
        pattern = r'(Indicator .*\..*\..*|Target .*\.*|Goal .*): '
        return re.sub(pattern, '', input_string)

    
    # Remove the numbers from the global indicator/target/goal names.
    for key in ['SDG_GOAL__GLOBAL', 'SDG_TARGET__GLOBAL', 'SDG_INDICATOR__GLOBAL']:
        if key in meta:
            meta[key] = remove_global_numbers(meta[key])

    # If "actual_indicator_available" is populated, use it for
    # the indicator config settings: indicator_available and graph_title.
    if 'actual_indicator_available' in meta and meta['actual_indicator_available'] != '':
        meta['indicator_available'] = meta['actual_indicator_available']
        meta['graph_title'] = meta['actual_indicator_available']
    return meta
