#!/usr/bin/env python
import os
import os.path as osp
import re

import yaml

dataset_zoo_path = '../../dataset_zoo'
datasets = os.listdir(dataset_zoo_path)
datasets.sort()

table = '# 支持数据集一览\n' + '## 支持的数据集\n'
table += '| 数据集名称 | 文本检测 | 文本识别 | 端到端文本检测识别 | 关键信息抽取 |\n' \
         '|----------|---------|--------|------------------|-----------|\n'
details = '## 数据集详情\n'

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
    details += 'A. 数据集基础信息\n'
    details += f" - 官方网址: [{dataset}]({data['Website']})\n"
    details += f" - 发布年份: {paper['Year']}\n"
    details += f" - 语言: {data['Language']}\n"
    details += f" - 场景: {data['Scene']}\n"
    details += f" - 标注粒度: {data['Granularity']}\n"
    details += f" - 支持任务: {data['Tasks']}\n"
    details += f" - 数据集许可证: [{data['License']['Type']}]({data['License']['Link']})\n\n"

    # Format
    details += '<details> <summary>B. 标注格式</summary>\n\n</br>'
    sample_path = osp.join(dataset_zoo_path, dataset, 'sample_anno.md')
    if osp.exists(sample_path):
        with open(sample_path, 'r') as f:
            samples = f.readlines()
            samples = ''.join(samples)
            details += samples
    details += '</details>\n\n</br>'

    # Reference
    details += 'C. 参考文献\n'
    details += f"```bibtex\n{paper['BibTeX']}\n```\n"

datasetzoo = table + details

with open('user_guides/data_prepare/datasetzoo.md', 'w') as f:
    f.write(datasetzoo)
