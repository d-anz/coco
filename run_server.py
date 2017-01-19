#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from __future__ import absolute_import
import os

from core import Coco


os.environ.setdefault('COCO_CONFIG_MODULE', 'coco.config')
coco = Coco()

if __name__ == '__main__':
    try:
        os.mkdir('logs')
        os.mkdir('keys')
    except:
        pass
    coco.run_forever()
