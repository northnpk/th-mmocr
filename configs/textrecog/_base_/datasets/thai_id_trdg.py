thai_id_data_root = '/content/mmocr/ThaiID_from_stockdf/'

thai_rec_train = dict(
    type='OCRDataset',
    data_root=thai_id_data_root,
    data_prefix=dict(img_path='imgs/'),
    ann_file='labels.json',
    pipeline=None,
    test_mode=False)

thai_rec_test = dict(
    type='OCRDataset',
    data_root=thai_id_data_root,
    data_prefix=dict(img_path='imgs/'),
    ann_file='labels.json',
    pipeline=None,
    test_mode=True)
