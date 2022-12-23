import tests.expected as expected


ARGS = [('file1.json', 'file2.json', 'json', expected.SMALL_JSON),
        ('big1.json', 'big2.json', 'json', expected.BIG_JSON),
        ('file1.yaml', 'file2.yaml', 'json', expected.SMALL_JSON),
        ('big1.yaml', 'big2.yaml', 'json', expected.BIG_JSON),
        ('file1.json', 'file2.json', 'plain', expected.SMALL_PLAIN),
        ('big1.json', 'big2.json', 'plain', expected.BIG_PLAIN),
        ('file1.yaml', 'file2.yaml', 'plain', expected.SMALL_PLAIN),
        ('big1.yaml', 'big2.yaml', 'plain', expected.BIG_PLAIN),
        ('file1.json', 'file2.json', 'stylish', expected.SMALL_STRING),
        ('big1.json', 'big2.json', 'stylish', expected.BIG_STRING),
        ('file1.yaml', 'file2.yaml', 'stylish', expected.SMALL_STRING),
        ('big1.yaml', 'big2.yaml', 'stylsih', expected.BIG_STRING),
        ]
