import xml.etree.ElementTree as ET

def load_fods(path):
    ns = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0'
    }

    tree = ET.parse(path)
    root = tree.getroot()
    data = {}

    for table in root.findall('.//table:table', ns):
        sheet_name = table.attrib.get(f'{{{ns["table"]}}}name')
        rows = []
        for row in table.findall('table:table-row', ns):
            row_data = []
            for cell in row.findall('table:table-cell', ns):
                text_p = cell.find('text:p', ns)
                value = text_p.text.strip() if text_p is not None and text_p.text else ''

                repeat_attr = cell.attrib.get(f'{{{ns["table"]}}}number-columns-repeated')
                repeat = int(repeat_attr) if repeat_attr else 1

                row_data.extend([value] * repeat)
            rows.append(row_data)
        data[sheet_name] = rows

    return data