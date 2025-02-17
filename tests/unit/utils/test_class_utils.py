import os
import sys
import unittest

import monailabel.interfaces
import monailabel.transform.post
from monailabel.utils.others.class_utils import (
    class_args_to_exp,
    get_class_names,
    get_class_of_subclass_from_file,
    init_class_from_exp,
)


class MyTestCase(unittest.TestCase):
    base_dir = os.path.realpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    data_dir = os.path.join(base_dir, "tests", "data")
    app_dir = os.path.join(base_dir, "sample-apps", "deepedit")

    def test_get_class_names_1(self):
        names = get_class_names(monailabel.interfaces)
        assert "monailabel.interfaces.app.MONAILabelApp" in names

    def test_get_class_names_2(self):
        names = get_class_names(monailabel.transform.post)
        assert "monailabel.transform.post.Restored" in names

    def test_init_from_exp(self):
        c = init_class_from_exp("monai.transforms.LoadImaged(keys='image')")
        assert c

    def test_class_args_to_exp(self):
        str = {
            "name": "monai.transforms.LoadImaged",
            "args": {
                "keys": ["image", "label"],
                "image_only": True,
            },
        }
        c = class_args_to_exp(str)
        assert c

    def test_get_class_of_subclass_from_file(self):
        sys.path.append(self.app_dir)
        c = get_class_of_subclass_from_file("main", os.path.join(self.app_dir, "main.py"), "MONAILabelApp")
        assert c
