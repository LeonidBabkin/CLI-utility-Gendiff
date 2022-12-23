import tests.expected as expected


ARGS = [('file1.json', 'file2.json', 'json', expected.SMALL_JSON),
        ('big1.json', 'big2.json', 'json', expected.BIG_JSON),
        ('file1.yaml', 'file2.yaml', 'yaml', expected.SMALL_JSON),
        ('big1.yaml', 'big2.yaml', 'yaml', expected.BIG_JSON),
        ]
