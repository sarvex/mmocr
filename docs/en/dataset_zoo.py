#!/usr/bin/env python
import os
import os.path as osp
import re

import yaml

dataset_zoo_path = '../../dataset_zoo'
datasets = os.listdir(dataset_zoo_path)
datasets.sort()

table = '# Overview\n' + '## Supported Datasets\n'
table += '| Dataset Name | Text Detection | Text Recognition | Text Spotting | KIE |\n' \
         '|--------------|----------------|------------------|---------------|-----|\n'  # noqa: E501
details = '## Dataset Details\n'

for dataset in datasets:
    meta = yaml.safe_load(
        open(osp.join(dataset_zoo_path, dataset, 'metafile.yml')))
    dataset_name = meta['Name']
    detail_link = re.sub('[^A-Za-z0-9- ]', '',
                         dataset_name).replace(' ', '-').lower()
    paper = meta['Paper']
    data = meta['Data']

    table += f"| [{dataset}](#{detail_link}) | {'✓' if 'textdet' in data['Tasks'] else ''} | {'✓' if 'textrecog' in data['Tasks'] else ''} | {'✓' if 'textspotting' in data['Tasks'] else ''} | {'✓' if 'kie' in data['Tasks'] else ''} |\n"

    details += f'### {dataset_name}\n'
    details += f"""> \"{paper['Title']}\", *{paper['Venue']}*, {paper['Year']}. [PDF]({paper['URL']})\n\n"""

    # Basic Info
    details += 'A. Basic Info\n'
    details += f" - Official Website: [{dataset}]({data['Website']})\n"
    details += f" - Year: {paper['Year']}\n"
    details += f" - Language: {data['Language']}\n"
    details += f" - Scene: {data['Scene']}\n"
    details += f" - Annotation Granularity: {data['Granularity']}\n"
    details += f" - Supported Tasks: {data['Tasks']}\n"
    details += (
        f" - License: [{data['License']['Type']}]({data['License']['Link']})\n"
    )

    # Format
    details += '<details> <summary>B. Annotation Format</summary>\n\n</br>'
    sample_path = osp.join(dataset_zoo_path, dataset, 'sample_anno.md')
    if osp.exists(sample_path):
        with open(sample_path, 'r') as f:
            samples = f.readlines()
            samples = ''.join(samples)
            details += samples
    details += '</details>\n\n</br>'

    # Reference
    details += 'C. Reference\n'
    details += f"```bibtex\n{paper['BibTeX']}\n```\n"

datasetzoo = table + details

with open('user_guides/data_prepare/datasetzoo.md', 'w') as f:
    f.write(datasetzoo)
